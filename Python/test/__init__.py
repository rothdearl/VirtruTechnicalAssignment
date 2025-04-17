# __init__.py

"""
Initialization file for the top-level classes in the test automation framework.
"""

from dotenv import load_dotenv

from .test_groups import TestGroups

# Load environment variables.
load_dotenv()
