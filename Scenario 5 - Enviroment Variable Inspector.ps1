#Source
#Week 4 PowerPoint
#Week 4 Tool Dev Walkthrough

#program header
Write-Host "These are your enviroment variables:"
# hyphens to make a clear break for formatted output
Write-Host ("-"*50)
# gets the username of the user
Write-Host "Username: $env:USERNAME"
#gets the users domain
Write-Host "User Domain: $env:USERDOMAIN"
#gets the users computer name
Write-Host "Computer Name: $env:COMPUTERNAME"
#gets the users file path
Write-Host "System Path: $env:Path"
