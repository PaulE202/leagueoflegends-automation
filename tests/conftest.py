import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Viewport configurations for responsive testing
VIEWPORTS = {
    'desktop': (1920, 1080),
    'tablet': (768, 1024),
    'mobile': (375, 667)
}


def pytest_addoption(parser):
    """Add command line options for test execution"""
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser to run tests on: firefox or edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="function")
def browser(request):
    """
    Browser fixture - initializes and closes browser for each test
    Usage: Run with --browser=firefox or --browser=edge
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    
    if browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    
    # Maximize window by default
    driver.maximize_window()
    
    # Implicit wait
    driver.implicitly_wait(10)
    
    yield driver

    # Teardown - close browser after all tests in class complete
    try:
        driver.quit()
    except Exception as e:
        # Browser may have already closed - that's okay
        print(f"\nNote: Browser cleanup encountered: {type(e).__name__}")
        pass

@pytest.fixture(scope="class")
def class_browser(request):
    """
    Class-scoped browser fixture - one browser instance for entire test class
    More efficient for smoke tests and related test groups
    Usage: Use in test classes for better performance
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    
    if browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown - close browser after all tests in class complete
    driver.quit()

@pytest.fixture(scope="session")
def session_browser(request):
    """Session-scoped browser - one browser for entire test run"""
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    
    if browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    try:
        driver.quit()
    except:
        pass

@pytest.fixture(scope="session")
def home_page(session_browser):
    """Shared homepage fixture - loads once for all tests"""
    from pages.home_page import HomePage
    home = HomePage(session_browser)
    home.load()
    home.dismiss_cookie_banner()
    home.dismiss_riot_alert()
    return home

@pytest.fixture(params=['firefox', 'edge'])
def multi_browser(request):
    """
    Multi-browser fixture - runs tests on both Firefox and Edge
    Use this fixture when you want a test to run on both browsers automatically
    """
    browser_name = request.param
    headless = request.config.getoption("--headless")
    driver = None
    
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture(params=VIEWPORTS.keys())
def responsive_browser(request, browser):
    """
    Responsive fixture - runs test across desktop, tablet, mobile viewports
    Returns tuple: (driver, viewport_name)
    """
    viewport_name = request.param
    width, height = VIEWPORTS[viewport_name]
    
    browser.set_window_size(width, height)
    
    yield browser, viewport_name


@pytest.fixture
def desktop_browser(browser):
    """Desktop viewport (1920x1080)"""
    browser.set_window_size(1920, 1080)
    return browser


@pytest.fixture
def tablet_browser(browser):
    """Tablet viewport (768x1024)"""
    browser.set_window_size(768, 1024)
    return browser


@pytest.fixture
def mobile_browser(browser):
    """Mobile viewport (375x667)"""
    browser.set_window_size(375, 667)
    return browser


@pytest.fixture(scope="session", autouse=True)
def create_reports_folders():
    """Create necessary folders for reports and screenshots"""
    import os
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)