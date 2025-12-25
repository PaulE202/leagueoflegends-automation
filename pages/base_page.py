from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Element interaction methods

    def wait_for_element(self, locator, timeout=10):
        """Wait for element to be present"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not found after {timeout}s")
    
    def is_displayed(self, locator, timeout=5):
        """Check if element is displayed"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    # Page load methods

    def wait_for_page_load(self, timeout=30):
        """Wait for page to be fully loaded"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    # Utility methods

    def take_screenshot(self, name):
        """Take screenshot for debugging"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filepath)
        return filepath

    # Banner methods

    def dismiss_cookie_banner(self):
        """Dismiss Osano cookie banner if present"""
        try:
            # Wait for and click the "Accept All" button
            accept_all_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".osano-cm-accept-all"))
            )
            accept_all_button.click()
        
            # Wait for banner to actually disappear
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".osano-cm-dialog"))
            )
            return True
        except:
            # Banner not present or already dismissed
            return False
        
    def dismiss_riot_alert(self):
        """Dismiss Riot alert if present"""
        try:
            # Try the close button first
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='riotbar:banner:button-close']"))
            )
            close_button.click()
        
            # Wait for the blocking element to disappear
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".riotbar-alert-content-inner"))
            )
            return True
        except:
            # If button not found, try dismissing by class
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".riotbar-alert-content-inner"))
                )
                return True
            except:
                return False
