from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade


class ArticleCardCarouselBlade(BaseBlade):
    """Article Card Carousel blade component"""
    
    # Locators
    TITLE = (By.CSS_SELECTOR, "[data-testid='title']")
    CTA_TERTIARY = (By.CSS_SELECTOR, "[data-testid='cta-tertiary']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
    
    # Note: Backdrop methods inherited from BaseBlade
    # Note: All carousel methods inherited from BaseBlade (viewport, slides, controls, buttons, navigation)
    
    # Title methods - using inherited generic methods
    def has_title(self):
        """Check if blade has title"""
        return self.has_element(self.TITLE)
    
    def get_title_text(self):
        """Get title text"""
        return self.get_element_text(self.TITLE)
    
    # CTA methods - using inherited generic methods from BaseBlade
    def has_tertiary_cta(self):
        """Check if blade has tertiary CTA"""
        return self.has_cta(self.CTA_TERTIARY)
    
    def get_tertiary_cta_element(self):
        """Get tertiary CTA element"""
        return self.get_cta_element(self.CTA_TERTIARY)
    
    def get_tertiary_cta_text(self):
        """Get CTA text"""
        return self.get_cta_text(self.CTA_TERTIARY)
    
    def click_tertiary_cta(self):
        """Click tertiary CTA"""
        self.click_cta(self.CTA_TERTIARY)
    
    # Responsive controls logic (blade-specific)
    def get_max_visible_slides(self, viewport_width):
        """Get maximum slides visible at current viewport"""
        if viewport_width >= 1025:
            return 3
        elif viewport_width >= 601:
            return 2
        else:  # <= 600px
            return 1
    
    def should_show_controls(self, viewport_width):
        """Determine if controls should be visible based on viewport and slide count"""
        slide_count = self.get_slide_count()
        max_visible = self.get_max_visible_slides(viewport_width)
        return slide_count > max_visible
    
    def verify_controls_display(self, viewport_width):
        """Verify controls are displayed correctly for current viewport and slide count"""
        should_show = self.should_show_controls(viewport_width)
        controls_visible = self.has_controls() and self.get_controls_container().is_displayed()
        return should_show == controls_visible