def test_countries_and_timezones(app_adm):
    app_adm.home_page.open_countries()
    country_page = app_adm.country_page
    countries_list = country_page.get_countries()
    sorted_countries = sorted(countries_list)
    for country in range(len(countries_list)):
        assert countries_list[country] == sorted_countries[country]
        if country_page.amount_tzs_by_index(country + 1) > 0:
            timezones = country_page.get_timezones_for_country(country + 1)
            sorted_timezones = sorted(timezones)
            for timezone in range(len(timezones)):
                assert timezones[timezone] == sorted_timezones[timezone]

