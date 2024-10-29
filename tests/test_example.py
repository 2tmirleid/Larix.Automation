import os

import pytest
from dotenv import find_dotenv, load_dotenv
from pywinauto import Application

from pages.main_window_page import MainWindowPage


@pytest.fixture
def app():
    load_dotenv(find_dotenv())

    application = Application(backend="uia").start(os.environ["EXE_PATH"])
    yield application
    application.kill()

def test_example(app):
    main_window = MainWindowPage()
    main_window.open_file_context_menu()
    main_window.open_project_manager()
