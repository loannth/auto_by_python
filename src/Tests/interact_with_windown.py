# Start then connect to it
import time

from pywinauto import Application


def get_window_title(file_name='CocCocSetup.exe'):
    # start file name
    try:
        Application(backend='uia').start(f'C:\\Users\\loan.nth\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
        # interact with windown
        app = Application(backend='uia').connect(
            # class_name= '#32770',
            title_re='Đang chạy..., Trình cài đặt Cốc Cốc',
            timeout=30)
        print(app.window(title_re='Đang chạy..., Trình cài đặt Cốc Cốc').window_text())
    except Exception as e:
        print(e)


def test_get_window_title():
    get_window_title()


def check_window_exit(file_name='CocCocSetup.exe'):
    # start file name
    try:
        Application(backend='uia').start(f'C:\\Users\\loan.nth\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
        app = Application(backend='uia').connect(
            class_name='#32770',
            # title_re='Đang chạy..., Trình cài đặt Cốc Cốc',
            timeout=30)
        print(app.window(class_name='#32770').exists())
        print(app.window(class_name='#32770').is_visible())
    except Exception as e:
        print(e)


def test_check_window_exit():
    check_window_exit()


# Maximize
def maximize_window():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                               retry_interval=2, timeout=30)
        time.sleep(5)
        app = Application(backend='uia').connect(
            title_re='Thẻ mới - Cốc Cốc',
            timeout=30)

    except Exception as e:
        print(e)
    app.window(title_re='Thẻ mới - Cốc Cốc').set_focus()
    time.sleep(3)
    app.window(title_re='Thẻ mới - Cốc Cốc').maximize()

def test_maximize_window():
    maximize_window()
