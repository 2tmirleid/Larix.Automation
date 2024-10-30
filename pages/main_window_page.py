from utils.enums.main_toolbar.file_toolbar.file_toolbar_buttons_enum import FileToolbarButtonsEnum
from utils.enums.main_toolbar.main_toolbar_buttons_enum import MainToolbarButtonsEnum
from pages.base_page import BasePage


class MainWindowPage(BasePage):
    def __init__(self):

        super().__init__()

        self.main_toolbar = MainToolbarButtonsEnum
        self.file_toolbar = FileToolbarButtonsEnum

        self.wait_until_visible(timeout=self.timeouts.EXPLICIT.value)

    #EXAMPLE
    def open_file_context_menu(self) -> None:
        file_menu_btn_title = self.main_toolbar.FILE.value

        if self.window.exists():
            file_menu_btn = self.window.child_window(
                title=file_menu_btn_title,
                control_type="MenuItem"
            )

            if file_menu_btn.exists(timeout=self.timeouts.IMPLICIT.value):
                file_menu_btn.click_input()
            else:
                raise Exception(f"Element {file_menu_btn_title} not found")

    #EXAMPLE
    def open_project_manager(self) -> None:
        project_manager_title = self.file_toolbar.PROJECT_MANAGER.value

        if self.window.exists():
            project_manager_btn = self.window.child_window(
                title=project_manager_title,
                control_type="MenuItem"
            )

            if project_manager_btn.exists(timeout=self.timeouts.IMPLICIT.value):
                project_manager_btn.click_input()
            else:
                raise Exception(f"Element {project_manager_title} not found")


if __name__ == "__main__":
    temp = MainWindowPage()
    temp.open_file_context_menu()
    temp.open_project_manager()
