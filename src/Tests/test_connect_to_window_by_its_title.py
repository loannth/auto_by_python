import time

from pywinauto import Application

"""Connecting to the window"""

# Start then connect to it
def open_then_connect_to_window(file_name='CocCocSetup.exe'):
    # start file name
    try:
        Application(backend='uia').start(f'C:\\Users\\loan.nth\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
        # interface with window
        app = Application(backend='uia').connect(
            title_re='Đang chạy..., Trình cài đặt Cốc Cốc',
            timeout=30)
        print(app.window())

    except Exception as e:
        print(e)

def test_open_then_connect_to_window():
    open_then_connect_to_window()

# connect to the opening window
def connect_to_opening_window():
    # Start file setup
    try:
        app = Application(backend="uia").connect(
            class_name="#32770",
            control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        # print(app.window())
        return app
    except Exception as e:
        print(e)

def test_connect_to_opening_window():
    connect_to_opening_window()

"""Closing the window"""

def close_window_by_kill():
    open_then_connect_to_window()
    window = open_then_connect_to_window()
    window.kill()

def test_close_window_by_kill():
    close_window_by_kill()

# Close the window

def close_the_window_by_title():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                               retry_interval=2, timeout=30)
        time.sleep(5)
    except Exception as e:
        print(e)
        app.window(title_re='Thẻ mới - Cốc Cốc').close()

def test_close_the_window_by_title():
    close_the_window_by_title()