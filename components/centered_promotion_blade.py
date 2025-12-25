from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade


class CenteredPromotionBlade(BaseBlade):
    """Centered Promotion blade component"""
    
    # Locators

    LINKS = (By.CSS_SELECTOR, "[data-testid='links']")
    CTA_PRIMARY = (By.CSS_SELECTOR, "[data-testid='cta-0']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
    
    # Links section methods

    def has_links_section(self):
        """Check if blade has links section"""
        return self.has_element(self.LINKS)
    
    # CTA methods - using inherited generic methods from BaseBlade
    
    def get_primary_cta_element(self):
        """Get primary CTA element"""
        return self.get_cta_element(self.CTA_PRIMARY)
    
    def get_primary_cta_text(self):
        """Get primary CTA text"""
        return self.get_cta_text(self.CTA_PRIMARY)
    
    def is_primary_cta_visible(self):
        """Check if primary CTA is visible"""
        return self.is_cta_visible(self.CTA_PRIMARY)