import pytest
from fixture.adminka.app_adminka import AdminApplication
from fixture.app import Application


@pytest.fixture
def app_adm(request):
    wd = AdminApplication()
    print(wd.wd.capabilities)
    wd.open_login_page()
    wd.login_as(username="admin", password="admin")
    request.addfinalizer(wd.destroy)
    return wd


@pytest.fixture
def app(request):
    wd = Application()
    print(wd.wd.capabilities)
    wd.open_home_page()
    request.addfinalizer(wd.destroy)
    return wd
