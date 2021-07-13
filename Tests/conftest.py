import pytest
from selenium import webdriver


from TestData.ContactPageData import ContactPageData
from TestData.ShopPageData import ShopPageData
driver = None

#Command line arguments
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")    # pulling value inside the methods

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome("C:\\Users\\kalmazan\\SeleniumDrivers\\Chromedriver.exe", options=chrome_options)
        driver.implicitly_wait(10)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)

    elif browser_name == "safari":

        print("safari")

    driver.get("https://jupiter.cloud.planittesting.com/#/home")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.fixture(params=ContactPageData.test_ContactPage_data)
def contactPageData(request):
    return request.param

@pytest.fixture(params=ShopPageData.test_ShopPage_data)
def shopPageData(request):
    return request.param