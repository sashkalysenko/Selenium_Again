def test_task_10(app):
    home_item_info = app.home_page.get_product_info('campaigns', 1)
    app.home_page.open_product_page('campaigns', 1)
    product_item_info = app.product_page.get_product_info()
    for key in product_item_info.keys():
        assert home_item_info[key] == product_item_info[key]
