#!/usr/bin/env python3
"""
Digital Twin Application Entry Point.

This is the main entry point for the Digital Twin application.
Run this file with: streamlit run main.py
"""

import sys
import os
from dotenv import load_dotenv

print("🔍 Testing .env loading...")
print(f"Current directory: {os.getcwd()}")
print(f".env file exists: {os.path.exists('.env')}")

# Try loading .env
load_dotenv()
# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.digital_twin.ui.app import main

if __name__ == "__main__":
    main()
