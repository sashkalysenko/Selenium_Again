def test_open_all_topics(app_adm):
    amount_apps = app_adm.home_page.amount_apps()
    for entry in range(1, amount_apps + 1):
        app_adm.home_page.click_app_by_index(entry)
        assert app_adm.home_page.is_header_exists() is True
        sub_apps_list = app_adm.home_page.get_children_names()
        if len(sub_apps_list) == 0:
            continue
        else:
            for sub_app in range(len(sub_apps_list) - 1):
                app_adm.home_page.click_children_by_index(sub_app + 2)
                assert app_adm.home_page.is_header_exists() is True
