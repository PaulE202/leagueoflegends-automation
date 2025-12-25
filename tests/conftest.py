import base64
import pytest
import os
import time
import pytest_html
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



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

@pytest.fixture(scope="session", autouse=True)
def create_reports_folders():
    """Create necessary folders for reports and screenshots"""
    import os
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach to HTML report"""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    
    if report.when == "call" and report.failed:
        driver = None
        blade = None
        
        # Get driver from fixtures
        if "session_browser" in item.funcargs:
            driver = item.funcargs["session_browser"]
        elif "home_page" in item.funcargs:
            driver = item.funcargs["home_page"].driver
        
        # Get blade fixture
        blade_fixture_names = [
            "masthead",
            "carousel_blade", 
            "icon_tab_choose_champion",
            "icon_tab_multiple_ways_to_play",
            "media_promo",
            "centered_promotion"
        ]
        
        for fixture_name in blade_fixture_names:
            if fixture_name in item.funcargs:
                blade = item.funcargs[fixture_name]
                break
        
        # Scroll to blade before screenshot
        if blade and hasattr(blade, 'scroll_into_view'):
            try:
                blade.scroll_into_view()
                time.sleep(0.7)
            except:
                pass
        
        # Take screenshot
        if driver:
            test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join("screenshots", f"{test_name}_{timestamp}.png")
            
            try:
                driver.save_screenshot(screenshot_path)
                print(f"\n📸 Screenshot saved: {screenshot_path}")
                
                # Read image and encode to base64 STRING
                with open(screenshot_path, 'rb') as f:
                    image_bytes = f.read()
                
                import base64
                image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                
                # Pass base64 string to pytest-html
                extras.append(pytest_html.extras.png(image_base64))
                print(f"✓ Attached to HTML report")
                    
            except Exception as e:
                print(f"\n❌ Screenshot error: {e}")
    
    report.extras = extras