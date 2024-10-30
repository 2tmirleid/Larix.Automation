import os

import pytest
from dotenv import find_dotenv, load_dotenv
from pywinauto import Application

from pages.main_window_page import MainWindowPage

def test_example():
    main_window = MainWindowPage()
    main_window.open_file_context_menu()
    main_window.open_project_manager()
