$ErrorActionPreference = "Stop"

$Project = "G:\Dev\darkuniverse-training\Reports\PQS Dark Universe Report"
$SummaryFile = Join-Path $Project "Scripts\employee_summary_processor.py"
$BusinessRules = Join-Path $Project "Documentation\BUSINESS_RULES.md"
$Python = Join-Path $Project ".venv\Scripts\python.exe"
$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$BackupFolder = Join-Path $Project "Code_Backups\Missing_Maximo_$Timestamp"

foreach ($Path in @($SummaryFile, $Python)) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file not found: $Path"
    }
}

New-Item -ItemType Directory -Path $BackupFolder -Force | Out-Null
Copy-Item -LiteralPath $SummaryFile -Destination (Join-Path $BackupFolder "employee_summary_processor.py") -Force
if (Test-Path -LiteralPath $BusinessRules -PathType Leaf) {
    Copy-Item -LiteralPath $BusinessRules -Destination (Join-Path $BackupFolder "BUSINESS_RULES.md") -Force
}

$Text = [System.IO.File]::ReadAllText($SummaryFile)
$Old = @'
    work_orders = unique_in_order(
        [result.work_order for result in module_results if result.work_order]
    )
    status = "COMPLETE" if not incomplete else "INCOMPLETE"
'@
$New = @'
    work_orders = unique_in_order(
        [result.work_order for result in module_results if result.work_order]
    )
    if not work_orders and any(
        result.result == "No Maximo Record" for result in module_results
    ):
        work_orders = ("Missing Maximo Data",)
    status = "COMPLETE" if not incomplete else "INCOMPLETE"
'@

if (-not $Text.Contains($Old)) {
    throw "Expected venue-summary block was not found. No source file was changed."
}

$Updated = $Text.Replace($Old, $New)
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($SummaryFile, $Updated, $Utf8NoBom)

if (Test-Path -LiteralPath $BusinessRules -PathType Leaf) {
    $Rules = [System.IO.File]::ReadAllText($BusinessRules)
    $RuleLine = "- When a current roster employee has no applicable Maximo records for unresolved modules, the applicable venue Work Order(s) field displays `Missing Maximo Data`."
    if (-not $Rules.Contains($RuleLine)) {
        $Rules = $Rules.TrimEnd() + "`r`n`r`n## Missing Maximo Display`r`n`r`n$RuleLine`r`n- The module status remains `No Maximo Record`.`r`n- The employee remains in the population sheet, dashboard totals, and employee action list.`r`n"
        [System.IO.File]::WriteAllText($BusinessRules, $Rules, $Utf8NoBom)
    }
}

& $Python -m py_compile $SummaryFile
if ($LASTEXITCODE -ne 0) {
    Copy-Item -LiteralPath (Join-Path $BackupFolder "employee_summary_processor.py") -Destination $SummaryFile -Force
    throw "Python validation failed. The original source file was restored."
}

Write-Host ""
Write-Host "PQS MISSING MAXIMO FLAG INSTALLED." -ForegroundColor Green
Write-Host ""
Write-Host "New behavior:" -ForegroundColor Cyan
Write-Host "- Line Schedule employees remain in the report."
Write-Host "- Required modules without any applicable Maximo record remain No Maximo Record."
Write-Host "- The applicable venue Work Order(s) field shows Missing Maximo Data."
Write-Host "- The employee remains in the Dashboard employee action list."
Write-Host ""
Write-Host "Backup folder: $BackupFolder"
Write-Host "Run the PQS Dark Universe Report and verify a known missing-Maximo SSO." -ForegroundColor Yellow
