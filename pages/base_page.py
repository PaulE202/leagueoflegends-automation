from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import requests


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
    
    def wait_for_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not visible after {timeout}s")
    
    def click_element(self, locator, timeout=10):
        """Wait for element to be clickable and click it"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.wait_for_element(locator)
        return element.text
    
    def is_displayed(self, locator, timeout=5):
        """Check if element is displayed"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def get_element(self, locator):
        """Get element without waiting"""
        return self.driver.find_element(*locator)
    
    def get_elements(self, locator):
        """Get multiple elements"""
        return self.driver.find_elements(*locator)
    
    # Page load methods
    def wait_for_page_load(self, timeout=30):
        """Wait for page to be fully loaded"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    def get_page_load_time(self):
        """Get total page load time in milliseconds"""
        try:
            load_time = self.driver.execute_script(
                "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
            )
            return load_time if load_time > 0 else None
        except:
            return None
    
    def get_performance_metrics(self):
        """Get detailed performance timing breakdown"""
        metrics = self.driver.execute_script(
            """
            const timing = performance.timing;
            return {
                'dns_lookup': timing.domainLookupEnd - timing.domainLookupStart,
                'tcp_connection': timing.connectEnd - timing.connectStart,
                'server_response': timing.responseEnd - timing.requestStart,
                'dom_processing': timing.domComplete - timing.domLoading,
                'total_load': timing.loadEventEnd - timing.navigationStart
            };
            """
        )
        return metrics
    
    # Link checking methods
    def get_all_links(self):
        """Get all links on the page"""
        links = self.driver.find_elements(By.TAG_NAME, "a")
        return [(link.text.strip(), link.get_attribute("href")) 
                for link in links if link.get_attribute("href")]
    
    def check_link_status(self, url, timeout=5):
        """Check if a link is broken - returns (status_code, is_broken, error_message)"""
        try:
            response = requests.head(url, timeout=timeout, allow_redirects=True)
            
            if response.status_code == 405:
                response = requests.get(url, timeout=timeout, allow_redirects=True)
            
            is_broken = response.status_code >= 400
            return (response.status_code, is_broken, None)
            
        except requests.exceptions.Timeout:
            return (None, True, "Timeout")
        except requests.exceptions.ConnectionError:
            return (None, True, "Connection Error")
        except requests.exceptions.RequestException as e:
            return (None, True, str(e))
    
    def find_broken_links(self, exclude_external=False):
        """Find all broken links on the page"""
        all_links = self.get_all_links()
        broken_links = []
        
        current_domain = self.driver.execute_script("return window.location.hostname")
        
        for text, href in all_links:
            if not href or href.startswith('javascript:') or href.startswith('mailto:'):
                continue
            
            if exclude_external and current_domain not in href:
                continue
            
            status_code, is_broken, error = self.check_link_status(href)
            
            if is_broken:
                broken_links.append({
                    'text': text,
                    'url': href,
                    'status_code': status_code,
                    'error': error
                })
        
        return broken_links
    
    # Utility methods
    def take_screenshot(self, name):
        """Take screenshot for debugging"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filepath)
        return filepath
    
    def scroll_to_element(self, locator):
        """Scroll element into view"""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

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
            # Wait for and click the close button
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='riotbar:banner:button-close']"))
            )
            close_button.click()
        
            # Wait for alert to actually disappear
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-testid='riotbar:banner']"))
            )
            return True
        except:
            # Alert not present or already dismissed
            return False       
