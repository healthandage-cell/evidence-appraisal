@echo off
REM Double-click to repackage the evidence-appraisal skill.
cd /d "%~dp0"
python repackage.py
echo.
pause
