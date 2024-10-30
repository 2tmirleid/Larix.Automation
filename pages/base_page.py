import os

from dotenv import load_dotenv, find_dotenv
from pywinauto import Application

from utils.enums.env_vars.env_vars_enum import EnvVarsEnum
from utils.enums.timeouts.timeouts_enum import TimeoutsEnum

class BasePage:
    def __init__(self):
        self.timeouts = TimeoutsEnum
        self.env_vars = EnvVarsEnum

        load_dotenv(find_dotenv())

        self.env_vars_exists()

        self.exe_path = os.environ["EXE_PATH"]
        self.title    = os.environ['WINDOW_TITLE']

        self.app    = Application(backend="uia").start(self.exe_path)
        self.window = self.app.window(title=self.title)

    def env_vars_exists(self) -> None:
        for env_var in self.env_vars:
            if not os.environ.get(str(env_var.value)):
                raise Exception(f"Env var {env_var.value} not found")


    def wait_until_visible(self, timeout: int = None) -> None:
        if timeout is None:
            timeout = self.timeouts.IMPLICIT.value

        self.window.wait('visible', timeout=timeout)
