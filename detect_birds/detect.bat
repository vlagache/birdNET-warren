@echo off
set TF_CPP_MIN_LOG_LEVEL=3
set TF_ENABLE_ONEDNN_OPTS=0

cd /d "%~dp0\.."

title BirdNET Analyzer

uv run python detect_birds/run.py

pause
