from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MediaPromoBlade(BaseBlade):
    """Media Promo blade component"""
    
    # Locators
    MEDIAPROMO_MAIN_CONTAINER = (By.CSS_SELECTOR, "[data-testid='mediapromo-main-container']")
    CONTENT_CONTAINER = (By.CSS_SELECTOR, ".content-container")
    MEDIA_CONTAINER = (By.CSS_SELECTOR, ".media-container")
    
    # Heading locators
    MEDIAPROMO_HEADING = (By.CSS_SELECTOR, ".mediapromo-heading")
    SUPERTITLE = (By.CSS_SELECTOR, "[data-testid='mediapromo-supertitle']")
    TITLE = (By.CSS_SELECTOR, "[data-testid='mediapromo-title']")
    DESCRIPTION = (By.CSS_SELECTOR, "[data-testid='mediapromo-description']")
    RICH_TEXT_HTML = (By.CSS_SELECTOR, "[data-testid='rich-text-html']")
    
    # CTA locators
    MEDIAPROMO_LINKS = (By.CSS_SELECTOR, "[data-testid='mediapromo-links']")
    HEADER_PRIMARY_CTA = (By.CSS_SELECTOR, "[data-testid='header-primary-cta']")
    CTA_CONTENT = (By.CSS_SELECTOR, "[data-testid='cta-content']")
    
    # Media locators
    FEATURED_MEDIA = (By.CSS_SELECTOR, "[data-testid='featured-media']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
    
    # Note: Backdrop methods inherited from BaseBlade
    
    # Container methods
    def has_main_container(self):
        """Check if blade has main container"""
        return self.element_exists_in_blade(self.MEDIAPROMO_MAIN_CONTAINER)
    
    def has_content_container(self):
        """Check if blade has content container"""
        return self.element_exists_in_blade(self.CONTENT_CONTAINER)
    
    def has_media_container(self):
        """Check if blade has media container"""
        return self.element_exists_in_blade(self.MEDIA_CONTAINER)
    
    # Heading methods - using inherited generic methods
    def has_heading(self):
        """Check if blade has heading section"""
        return self.has_element(self.MEDIAPROMO_HEADING)
    
    def has_supertitle(self):
        """Check if heading has supertitle"""
        return self.has_element(self.SUPERTITLE)
    
    def get_supertitle_text(self):
        """Get supertitle text"""
        return self.get_element_text(self.SUPERTITLE)
    
    def has_title(self):
        """Check if heading has title"""
        return self.has_element(self.TITLE)
    
    def get_title_text(self):
        """Get title text"""
        return self.get_element_text(self.TITLE)
    
    def has_description(self):
        """Check if heading has description"""
        return self.has_element(self.DESCRIPTION)
    
    def get_description_text(self):
        """Get description rich text"""
        try:
            desc_element = self.find_element_in_blade(self.DESCRIPTION)
            rich_text = desc_element.find_element(*self.RICH_TEXT_HTML)
            return rich_text.text
        except:
            return None
    
    # CTA methods - using inherited generic methods from BaseBlade
    def has_links_section(self):
        """Check if blade has links section"""
        return self.has_element(self.MEDIAPROMO_LINKS)
    
    def has_primary_cta(self):
        """Check if blade has primary CTA"""
        return self.has_cta(self.HEADER_PRIMARY_CTA)
    
    def get_primary_cta_element(self):
        """Get primary CTA element"""
        return self.get_cta_element(self.HEADER_PRIMARY_CTA)
    
    def get_primary_cta_text(self):
        """Get primary CTA text"""
        return self.get_cta_text(self.HEADER_PRIMARY_CTA)
    
    def click_primary_cta(self):
        """Click primary CTA"""
        self.click_cta(self.HEADER_PRIMARY_CTA)
    
    def is_primary_cta_visible(self):
        """Check if primary CTA is visible"""
        return self.is_cta_visible(self.HEADER_PRIMARY_CTA)
    
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
            return media.tag_name.lower() == "img"
        return False
    
    def featured_media_is_video(self):
        """Check if featured media is video"""
        media = self.get_featured_media_element()
        if media:
            return media.tag_name.lower() == "video"
        return False   

    def is_featured_media_visible(self):
        """Check if featured media is visible (waits for lazy loading)"""
        try:
            media_element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='featured-media']"))
        
            # Wait for lazy-loaded image to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(media_element)
            )
            return True
        except:
            return False