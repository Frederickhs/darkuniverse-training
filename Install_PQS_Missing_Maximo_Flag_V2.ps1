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

if ($Text.Contains('work_orders = ("Missing Maximo Data",)')) {
    Write-Host "The Missing Maximo Data logic is already installed." -ForegroundColor Yellow
} else {
    $Pattern = '(?ms)(^[ \t]*work_orders[ \t]*=[ \t]*unique_in_order\([ \t]*\r?\n[ \t]*\[result\.work_order for result in module_results if result\.work_order\][ \t]*\r?\n[ \t]*\)[ \t]*\r?\n)([ \t]*status[ \t]*=[ \t]*"COMPLETE" if not incomplete else "INCOMPLETE")'
    $Replacement = @'
${1}    if not work_orders and any(
        result.result == "No Maximo Record" for result in module_results
    ):
        work_orders = ("Missing Maximo Data",)
${2}
'@
    $Updated = [System.Text.RegularExpressions.Regex]::Replace(
        $Text,
        $Pattern,
        $Replacement,
        [System.Text.RegularExpressions.RegexOptions]::Multiline
    )
    if ($Updated -eq $Text) {
        throw "The venue-summary code structure was not recognized. No source file was changed."
    }
    $Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($SummaryFile, $Updated, $Utf8NoBom)
}

if (Test-Path -LiteralPath $BusinessRules -PathType Leaf) {
    $Rules = [System.IO.File]::ReadAllText($BusinessRules)
    $Heading = "## Missing Maximo Display"
    if (-not $Rules.Contains($Heading)) {
        $Addition = @'

## Missing Maximo Display

- When a current roster employee has no applicable Maximo records for unresolved modules, the applicable venue Work Order(s) field displays `Missing Maximo Data`.
- The module status remains `No Maximo Record`.
- The employee remains in the population sheet, dashboard totals, and employee action list.
'@
        $Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::WriteAllText($BusinessRules, $Rules.TrimEnd() + $Addition + "`r`n", $Utf8NoBom)
    }
}

& $Python -m py_compile $SummaryFile
if ($LASTEXITCODE -ne 0) {
    Copy-Item -LiteralPath (Join-Path $BackupFolder "employee_summary_processor.py") -Destination $SummaryFile -Force
    throw "Python validation failed. The original source file was restored."
}

$Verification = [System.IO.File]::ReadAllText($SummaryFile)
if (-not $Verification.Contains('work_orders = ("Missing Maximo Data",)')) {
    throw "Post-install verification failed."
}

Write-Host ""
Write-Host "PQS MISSING MAXIMO FLAG INSTALLED." -ForegroundColor Green
Write-Host "- Module result: No Maximo Record"
Write-Host "- Venue Work Order(s): Missing Maximo Data"
Write-Host "- Dashboard action category: No Maximo Record"
Write-Host "Backup: $BackupFolder"
Write-Host ""
Write-Host "Run the PQS Dark Universe Report and verify a known missing-Maximo SSO." -ForegroundColor Cyan
