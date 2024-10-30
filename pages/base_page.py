import os

from dotenv import load_dotenv, find_dotenv
from pywinauto import Application

from utils.enums.timeouts.timeouts_enum import TimeoutsEnum

class BasePage:
    def __init__(self):
        self.timeouts = TimeoutsEnum

        load_dotenv(find_dotenv())

        self.exe_path = os.environ["EXE_PATH"]
        self.title    = os.environ['WINDOW_TITLE']

        self.app    = Application(backend="uia").start(self.exe_path)
        self.window = self.app.window(title=self.title)

    def env_vars_are_exists(self):
        #TODO Функция, которая запускается при наследовании класса и проверяет наличие переменных окружения
        ...

    def wait_until_visible(self, timeout: int = 10) -> None:
        self.window.wait('visible', timeout=timeout)

