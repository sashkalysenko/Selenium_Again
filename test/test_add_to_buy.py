def test_add_to_cart(app):
    for i in range(1, 4):
        app.home_page.open_product_page(category='most-popular', index=i)
        app.product_page.select_product_size(size='medium')
        products_in_cart = app.product_page.amount_products_in_cart()
        app.product_page.add_to_cart()
        assert products_in_cart + 1 == app.product_page.amount_products_in_cart()
        app.product_page.open_home_page()
    app.product_page.open_cart()
    while app.cart_page.amount_products_in_table() >= 1:
        amount_in_table_before = app.cart_page.amount_products_in_table()
        app.cart_page.remove_first_product()
        assert amount_in_table_before - 1 == app.cart_page.amount_products_in_table()
