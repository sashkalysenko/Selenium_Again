def test_registration(app):
    email = "sashka.lysenko@gmail.com"
    password = "Password01"
    app.home_page.create_new_customer(first_name="Alex", last_name="Lysenko", address_1="street", postcode="43095",
                                      city="Dnepr", email=email, password=password, phone="+380951783383")
    assert app.home_page.is_logged_in() is True
    app.home_page.logout()
    assert app.home_page.is_logged_in() is False
    app.home_page.login_as(email=email, password=password)
    assert app.home_page.is_logged_in() is True
