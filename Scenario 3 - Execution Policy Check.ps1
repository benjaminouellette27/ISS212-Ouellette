#Sources
#Week 4 PowerPoint
#Week 3 PowerPoint
#Week 4 Tool Dev Walkthrough

#gets current execution policy
Write-Host "Current Execution Policy: $(Get-ExecutionPolicy)"
#prints a warnning if the current policy is unrestricted or bypass
#or displays a message that policy is restricted and scripts cannot be run on the system.
if ((Get-ExecutionPolicy) -in "Unrestricted", "Bypass") {
    Write-Host"Warning: Your execution policy allows all scripts to run. Ensure you trust the source."
} elseif ((Get-ExecutionPolicy) -eq "Restricted") {
    Write-Host"Scripts cannot be executed on this system."
}
