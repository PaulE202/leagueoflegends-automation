from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MediaPromoBlade(BaseBlade):
    """Media Promo blade component"""
   
    # Heading locators

    MEDIAPROMO_HEADING = (By.CSS_SELECTOR, ".mediapromo-heading")
    SUPERTITLE = (By.CSS_SELECTOR, "[data-testid='mediapromo-supertitle']")
    TITLE = (By.CSS_SELECTOR, "[data-testid='mediapromo-title']")
    DESCRIPTION = (By.CSS_SELECTOR, "[data-testid='mediapromo-description']")
    
    # CTA locators

    MEDIAPROMO_LINKS = (By.CSS_SELECTOR, "[data-testid='mediapromo-links']")
    HEADER_PRIMARY_CTA = (By.CSS_SELECTOR, "[data-testid='header-primary-cta']")

    # Media locators

    FEATURED_MEDIA = (By.CSS_SELECTOR, "[data-testid='featured-media']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
    
    # Heading methods - using inherited generic methods

    def has_heading(self):
        """Check if blade has heading section"""
        return self.has_element(self.MEDIAPROMO_HEADING)
    
    def get_supertitle_text(self):
        """Get supertitle text"""
        return self.get_element_text(self.SUPERTITLE)
    
    def get_title_text(self):
        """Get title text"""
        return self.get_element_text(self.TITLE)
    
    def get_description_text(self):
        """Get description rich text"""
        try:
            desc_element = self.find_element_in_blade(self.DESCRIPTION)
            return desc_element.text
        except:
            return None
    
    # CTA methods - using inherited generic methods from BaseBlade

    def has_links_section(self):
        """Check if blade has links section"""
        return self.has_element(self.MEDIAPROMO_LINKS)
    
    def has_primary_cta(self):
        """Check if blade has primary CTA"""
        return self.has_cta(self.HEADER_PRIMARY_CTA)
    
    def is_primary_cta_visible(self):
        """Check if primary CTA is visible"""
        return self.is_cta_visible(self.HEADER_PRIMARY_CTA)
    
    def get_primary_cta_element(self):
        """Get primary CTA element"""
        return self.get_cta_element(self.HEADER_PRIMARY_CTA)
    
    def get_primary_cta_text(self):
        """Get primary CTA text"""
        return self.get_cta_text(self.HEADER_PRIMARY_CTA)
    
    # Featured media methods

    def has_featured_media(self):
        """Check if blade has featured media"""
        return self.has_element(self.FEATURED_MEDIA)
    
    def get_featured_media_element(self):
        """Get featured media element"""
        try:
            return self.find_element_in_blade(self.FEATURED_MEDIA)
        except:
            return None
    
    def featured_media_is_image(self):
        """Check if featured media is image"""
        media = self.get_featured_media_element()
        if media:
            return media.tag_name == "img"
        return False

    def is_featured_media_visible(self):
        """Check if featured media is visible (waits for lazy loading)"""
        try:
            media_element = self.get_featured_media_element()
        
            # Wait for lazy-loaded image to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(media_element)
            )
            return True
        except:
            return False