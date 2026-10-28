@echo off
TITLE Apple Inc. - Profitability Decline Investigation Dashboard (Port 5013)
echo ==============================================================================
echo  PROJECT - 13: PROFITABILITY DECLINE INVESTIGATION
echo  Apple Inc. - AI Business Analyst Cross-Functional Telemetry Engine
echo ==============================================================================

set PYTHON_CMD=python
where python >nul 2>nul
if %errorlevel% neq 0 (
    set PYTHON_CMD="C:\Users\hp\AppData\Local\Programs\Orange\python.exe"
)

echo Starting Executive Decision Intelligence Server on Port 5013...
%PYTHON_CMD% run_project.py
pause

