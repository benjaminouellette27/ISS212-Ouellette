#Sources
#Week 4 Tool Dev Walkthrough

#if else statement that checks if the current user is an administrator
if (([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups-contains "S-1-5-32-544"){
    Write-Host "Administrator Privileges: Yes"
} else{
    Write-Host "Administrator Privileges: No"
}