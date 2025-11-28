from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade


class GameSimpleMastheadBlade(BaseBlade):
    """Game Simple Masthead blade component"""
    
    # Locators
    BLADE_CONTENT = (By.CSS_SELECTOR, "[data-testid='blade-content']")
    MASTHEAD_LOGO = (By.CSS_SELECTOR, "[data-testid='masthead-logo']")
    H1_TITLE = (By.TAG_NAME, "h1")
    CTA_PRIMARY = (By.CSS_SELECTOR, "[data-testid='cta-primary']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
    
    # Note: Backdrop methods inherited from BaseBlade
    
    # Content section methods
    def has_content_section(self):
        """Check if blade has content section"""
        return self.element_exists_in_blade(self.BLADE_CONTENT)
    
    def get_content_section(self):
        """Get content section element"""
        try:
            return self.find_element_in_blade(self.BLADE_CONTENT)
        except:
            return None
    
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
        try:
            blade_header = self.get_blade_header_element()
            if blade_header:
                h1 = blade_header.find_element(*self.H1_TITLE)
                return h1.text
        except:
            pass
        return None
    
    # CTA methods - using inherited generic methods from BaseBlade
    def has_primary_cta(self):
        """Check if masthead has primary CTA"""
        return self.has_cta(self.CTA_PRIMARY)
    
    def get_primary_cta_element(self):
        """Get primary CTA element"""
        return self.get_cta_element(self.CTA_PRIMARY)
    
    def get_primary_cta_text(self):
        """Get CTA button text"""
        return self.get_cta_text(self.CTA_PRIMARY)
    
    def click_primary_cta(self):
        """Click primary CTA button"""
        self.click_cta(self.CTA_PRIMARY)
    
    def is_primary_cta_visible(self):
        """Check if CTA is visible"""
        return self.is_cta_visible(self.CTA_PRIMARY)