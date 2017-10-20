import time


def test_open_in_new_window(app_adm):
    app_adm.home_page.open_countries()
    app_adm.country_page.add_new_country()
    for element in app_adm.country_page.links_in_separate_window():
        current_window = app_adm.wd.current_window_handle
        old_windows = app_adm.wd.window_handles
        app_adm.wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        new_windows = []
        time.sleep(3)
        while len(old_windows) + 1 != len(new_windows):
            new_windows = app_adm.wd.window_handles
        for window in old_windows:
            if window in new_windows:
                new_windows.remove(window)
        app_adm.wd.switch_to_window(new_windows[0])
        app_adm.wd.close()
        app_adm.wd.switch_to_window(current_window)
