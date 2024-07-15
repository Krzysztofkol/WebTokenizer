@echo off
cd /d "%~dp0"

REM Start the Flask server
start python web-tokenizer-backend.py

REM Wait for the server to start (adjust the timeout if needed)
timeout /t 5

REM Open the frontend in the default browser
start "" "http://localhost:2137"