$ErrorActionPreference = "Stop"
$repo = "G:\Dev\darkuniverse-training"
$target = Join-Path $repo "Hub\Scripts\search_sso_hub.py"
$backup = "$target.backup-before-pqs-work-orders"
if (-not (Test-Path $target)) { throw "File not found: $target" }
Copy-Item $target $backup -Force
Write-Host "Backup created: $backup"
Write-Host "No code changes were applied by this safety file."
Write-Host "Use the attached replacement Python file workflow in the next step."
