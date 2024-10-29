from pywinauto.application import Application

app = Application(backend="uia").start(r"C:\Program Files\iBIM\Larix\Manager.exe")

main_window = app.window(title="Larix.Manager - Новый проект")

main_window.wait('visible', timeout=20)

file_menu = main_window.child_window(title="Файл", control_type="MenuItem")

if file_menu.exists(timeout=10):
    file_menu.click_input()
else:
    print("Элемент 'Файл' не найден")

project_manager_menu = main_window.child_window(title="Диспетчер проектов...", control_type="MenuItem")

if project_manager_menu.exists(timeout=10):
    project_manager_menu.click_input()
else:
    print("Элемент 'Диспетчер проектов' не найден")


