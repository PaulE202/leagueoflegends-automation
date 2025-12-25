from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade
from selenium.common.exceptions import NoSuchElementException


class GameSimpleMastheadBlade(BaseBlade):
    """Game Simple Masthead blade component"""
    
    # Locators

    MASTHEAD_LOGO = (By.CSS_SELECTOR, "[data-testid='masthead-logo']")
    H1_TITLE = (By.TAG_NAME, "h1")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
       
    # Logo methods

    def has_logo(self):
        """Check if masthead has logo"""
        return self.element_exists_in_blade(self.MASTHEAD_LOGO)
    
    def get_logo_element(self):
        """Get logo element"""
        try:
            return self.find_element_in_blade(self.MASTHEAD_LOGO)
        except:
            return None
    
    def is_logo_visible(self):
        """Check if logo is visible"""
        logo = self.get_logo_element()
        return logo.is_displayed() if logo else False
    
    def get_h1_title(self):
        """Get H1 title text from blade header"""
        blade_header = self.get_blade_header_element()
        if not blade_header:
            return None
    
        try:
            h1 = blade_header.find_element(*self.H1_TITLE)
            return h1.text if h1.text.strip() else None
        except NoSuchElementException:
            return None