from pages.main_window_page import MainWindowPage

def test_example():
    main_window = MainWindowPage()
    main_window.open_file_context_menu()
    main_window.open_project_manager()
