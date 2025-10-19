#!/usr/bin/env python3
"""
Digital Twin Application Entry Point.

This is the main entry point for the Digital Twin application.
Run this file with: streamlit run main.py
"""

from src.digital_twin.ui.app import main
from dotenv import load_dotenv

print(f".env file exists: {os.path.exists('.env')}")

# Try loading .env
load_dotenv()

if __name__ == "__main__":
    main()
