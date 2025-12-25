from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class BaseBlade:
    """Base class for all blade/component objects"""
    
    # Common selectors used across blades

    CAROUSEL = (By.CSS_SELECTOR, "[data-testid='carousel']")
    SLIDES = (By.CSS_SELECTOR, "[data-testid='slide']")
    CONTROLS_CONTAINER = (By.CSS_SELECTOR, "[data-testid='controls-container']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "[data-testid='progress-bar']")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "[data-testid='previous-button']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[data-testid='next-button']")
    BLADE_HEADER = (By.CSS_SELECTOR, "[data-testid='bladeheader']")
    CTA_PRIMARY = (By.CSS_SELECTOR, "[data-testid='cta-primary']")
    CTA_SECONDARY = (By.CSS_SELECTOR, "[data-testid='cta-secondary']")
    CTA_TERTIARY = (By.CSS_SELECTOR, "[data-testid='cta-tertiary']")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        self.driver = driver
        self.blade = blade_element
        self.wait = WebDriverWait(driver, 10)
    
    # Element finding within blade

    def find_element_in_blade(self, locator):
        """Find element within this specific blade only"""
        return self.blade.find_element(*locator)
    
    def find_elements_in_blade(self, locator):
        """Find all elements within this blade"""
        return self.blade.find_elements(*locator)
    
    def element_exists_in_blade(self, locator):
        """Check if element exists in blade"""
        try:
            self.find_element_in_blade(locator)
            return True
        except NoSuchElementException:
            return False
    
    # Element visibility

    def is_element_visible(self, locator):
        """Check if element within blade is visible"""
        try:
            element = self.find_element_in_blade(locator)
            return element.is_displayed()
        except:
            return False

    
    # Blade visibility

    def is_visible(self):
        """Check if blade is visible"""
        return self.blade.is_displayed()

    def scroll_into_view(self):
        """Scroll blade into viewport"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.blade)
    
    # Backdrop methods

    def has_backdrop(self):
        """Check if blade has backdrop"""
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid*='backdrop']"))
    
    def has_backdrop_background(self):
        """Check if backdrop has background layer"""
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-background']"))
    
    def get_backdrop_background(self):
        """Get backdrop background element"""
        try:
            return self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-background']"))
        except NoSuchElementException:
            return None
    
    def backdrop_background_has_video(self):
        """Check if backdrop background contains video"""
        background = self.get_backdrop_background()
        if background:
            try:
                background.find_element(By.TAG_NAME, "video")
                return True
            except NoSuchElementException:
                pass
        return False
    
    def backdrop_background_has_image(self):
        """Check if backdrop background contains image"""
        background = self.get_backdrop_background()
        if background:
            try:
                background.find_element(By.TAG_NAME, "img")
                return True
            except NoSuchElementException:
                pass
        return False
    
    # Header methods

    def has_blade_header(self):
        """Check if blade has header section

        NOTE: Currently searches entire blade. If future blades need to differentiate
        between blade headers at different nesting levels, implement:
        - has_blade_header_direct_child() - for direct children of section
        - has_blade_header_in_content() - for headers within blade-content
        """
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid='bladeheader']"))

    def get_blade_header_element(self):
        """Get blade header element"""
        try:
            return self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='bladeheader']"))
        except NoSuchElementException:
            return None
    
    def get_title(self):
        """Get main title"""
        try:
            element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='title']"))
            return element.text if element.text.strip() else None
        except NoSuchElementException:
            return None
    
    def get_super_title(self):
        """Get super title (text above main title)"""
        try:
            element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='supertitle']"))
            return element.text if element.text.strip() else None
        except NoSuchElementException:
            return None
    
    def get_description(self):
        """Get description from blade header"""
        try:
            desc_element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='description']"))
            text = desc_element.text.strip()
            return text if text else None
        except NoSuchElementException:
            return None
    
    # Generic CTA methods (accept locator as parameter)

    def has_cta(self, locator):
        """Check if blade has CTA at given locator"""
        return self.element_exists_in_blade(locator)
    
    def get_cta_element(self, locator):
        """Get CTA element at given locator"""
        try:
            return self.find_element_in_blade(locator)
        except NoSuchElementException:
            return None
    
    def get_cta_text(self, locator):
        """Get CTA text at given locator"""
        cta = self.get_cta_element(locator)
        return cta.text if cta else None
    
    def is_cta_visible(self, locator):
        """Check if CTA at given locator is visible"""
        cta = self.get_cta_element(locator)
        return cta.is_displayed() if cta else False
    
    def is_primary_cta_visible(self):
        """Check if primary CTA is visible"""
        return self.is_cta_visible(self.CTA_PRIMARY)

    def is_secondary_cta_visible(self):
        """Check if secondary CTA is visible"""
        return self.is_cta_visible(self.CTA_SECONDARY)
    
    def get_primary_cta_element(self):
        """Get primary CTA element"""
        return self.get_cta_element(self.CTA_PRIMARY)
    
    def get_secondary_cta_element(self):
        """Get secondary CTA element"""
        return self.get_cta_element(self.CTA_SECONDARY)
    
    def get_primary_cta_text(self):
        """Get primary CTA text"""
        return self.get_cta_text(self.CTA_PRIMARY)
    
    def get_secondary_cta_text(self):
        """Get secondary CTA text"""
        return self.get_cta_text(self.CTA_SECONDARY)
    
    def is_tertiary_cta_visible(self):
        """Check if tertiary CTA is visible"""
        return self.is_cta_visible(self.CTA_TERTIARY)
    
    def get_tertiary_cta_element(self):
        """Get tertiary CTA element"""
        return self.get_cta_element(self.CTA_TERTIARY)
    
    def get_tertiary_cta_text(self):
        """Get tertiary CTA text"""
        return self.get_cta_text(self.CTA_TERTIARY)
    
    
    # Generic title/text methods

    def has_element(self, locator):
        """Check if element exists at given locator"""
        return self.element_exists_in_blade(locator)
    
    def get_element_text(self, locator):
        """Get text from element at given locator"""
        try:
            element = self.find_element_in_blade(locator)
            return element.text if element.text.strip() else None
        except NoSuchElementException:
            return None
    
    # Carousel methods (common across multiple blades)

    def has_carousel(self):
        """Check if blade contains carousel"""
        return self.element_exists_in_blade(self.CAROUSEL)
    
    def get_all_slides(self):
        """Get all slide elements"""
        return self.find_elements_in_blade(self.SLIDES)
    
    def get_slide_count(self):
        """Get total number of slides"""
        return len(self.get_all_slides())
    
    def has_controls(self):
        """Check if carousel has controls container"""
        return self.element_exists_in_blade(self.CONTROLS_CONTAINER)
    
    def has_progress_bar(self):
        """Check if carousel has progress bar"""
        return self.element_exists_in_blade(self.PROGRESS_BAR)
    
    def has_previous_button(self):
        """Check if carousel has previous button"""
        return self.element_exists_in_blade(self.PREVIOUS_BUTTON)
    
    def has_next_button(self):
        """Check if carousel has next button"""
        return self.element_exists_in_blade(self.NEXT_BUTTON)