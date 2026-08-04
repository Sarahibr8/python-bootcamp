#Greet Message
Write-Host "Setting up Python project..."

* Create project folders
#New-Item -ItemType Directory -Path "src", "tests" -Force | Out-Nu11 
mkdir src
mkdir tests

#Creating Virtual environment 
python -m venv venv

#Activating the virtual environemtnt 
& " Ivenv\Scripts\Activate.ps1"

# Install requests
python -m pip install requests

# Save installed packages
python -m pip freeze › requirements.txt

# Create starter files
#New-Item -ItemType File -Path "sre\main.py", "README. md" - Force | Out-Null 
ni src\main-py
ni README.md

* Initialize Git 
git init

Write-Host "Project setup completed!"
Write-Host "Virtual environment created and requests installed. "