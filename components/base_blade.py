from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class BaseBlade:
    """Base class for all blade/component objects"""
    
    # Common selectors used across blades
    CAROUSEL = (By.CSS_SELECTOR, "[data-testid='carousel']")
    VIEWPORT = (By.CSS_SELECTOR, "[data-testid='viewport']")
    SLIDES_CONTAINER = (By.CSS_SELECTOR, "[data-testid='slides-container']")
    SLIDES = (By.CSS_SELECTOR, "[data-testid='slide']")
    CONTROLS_CONTAINER = (By.CSS_SELECTOR, "[data-testid='controls-container']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "[data-testid='progress-bar']")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "[data-testid='previous-button']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[data-testid='next-button']")
    BLADE_HEADER = (By.CSS_SELECTOR, "[data-testid='bladeheader']")
    
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
    
    # Blade visibility
    def is_visible(self):
        """Check if blade is displayed"""
        return self.blade.is_displayed()
    
    def scroll_into_view(self):
        """Scroll blade into viewport"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.blade)
    
    # Backdrop methods
    def has_backdrop(self):
        """Check if blade has backdrop"""
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid*='backdrop']"))
    
    def get_backdrop_element(self):
        """Get backdrop element if exists"""
        try:
            return self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid*='backdrop']"))
        except NoSuchElementException:
            return None
    
    def has_backdrop_background(self):
        """Check if backdrop has background layer"""
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-background']"))
    
    def has_backdrop_foreground(self):
        """Check if backdrop has foreground layer"""
        return self.element_exists_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-foreground']"))
    
    def get_backdrop_background(self):
        """Get backdrop background element"""
        try:
            return self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-background']"))
        except NoSuchElementException:
            return None
    
    def get_backdrop_foreground(self):
        """Get backdrop foreground element"""
        try:
            return self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='backdrop-foreground']"))
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
    
    def backdrop_foreground_has_video(self):
        """Check if backdrop foreground contains video"""
        foreground = self.get_backdrop_foreground()
        if foreground:
            try:
                foreground.find_element(By.TAG_NAME, "video")
                return True
            except NoSuchElementException:
                pass
        return False
    
    def backdrop_foreground_has_image(self):
        """Check if backdrop foreground contains image"""
        foreground = self.get_backdrop_foreground()
        if foreground:
            try:
                foreground.find_element(By.TAG_NAME, "img")
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
    
    def get_sub_title(self):
        """Get sub title (text below main title) - PLACEHOLDER: Need actual selector"""
        # TODO: Get actual data-testid for subtitle from website
        return None
    
    def get_description(self):
        """Get description from blade header"""
        try:
            desc_element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='description']"))
            return desc_element.text if desc_element.text.strip() else None
        except NoSuchElementException:
            return None
    
    # Content section methods
    def get_content_sections(self):
        """Get all content sections in blade"""
        return self.find_elements_in_blade((By.CSS_SELECTOR, "[data-testid='blade-content']"))
    
    def get_content_count(self):
        """Count number of content sections"""
        return len(self.get_content_sections())
    
    def has_content(self):
        """Check if blade has content sections"""
        return self.get_content_count() > 0
    
    # Media methods (images, videos)
    def get_all_images(self):
        """Get all images in blade"""
        return self.find_elements_in_blade((By.TAG_NAME, "img"))
    
    def get_all_videos(self):
        """Get all videos in blade"""
        return self.find_elements_in_blade((By.TAG_NAME, "video"))
    
    def has_images(self):
        """Check if blade contains images"""
        return len(self.get_all_images()) > 0
    
    def has_videos(self):
        """Check if blade contains videos"""
        return len(self.get_all_videos()) > 0
    
    # Link/Button methods
    def get_all_links(self):
        """Get all links (a tags) in blade"""
        return self.find_elements_in_blade((By.TAG_NAME, "a"))
    
    def get_all_buttons(self):
        """Get all buttons in blade"""
        buttons = self.find_elements_in_blade((By.TAG_NAME, "button"))
        button_links = self.find_elements_in_blade((By.CSS_SELECTOR, "a[role='button']"))
        return buttons + button_links
    
    def get_hyperlinks(self):
        """Get text hyperlinks (excluding buttons)"""
        all_links = self.get_all_links()
        buttons = self.get_all_buttons()
        button_elements = set(buttons)
        return [link for link in all_links if link not in button_elements]
    
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
    
    def click_cta(self, locator):
        """Click CTA at given locator"""
        cta = self.get_cta_element(locator)
        if cta:
            cta.click()
    
    def is_cta_visible(self, locator):
        """Check if CTA at given locator is visible"""
        cta = self.get_cta_element(locator)
        return cta.is_displayed() if cta else False
    
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
    
    def get_carousel_element(self):
        """Get carousel element"""
        try:
            return self.find_element_in_blade(self.CAROUSEL)
        except NoSuchElementException:
            return None
    
    def get_viewport_element(self):
        """Get carousel viewport element"""
        try:
            return self.find_element_in_blade(self.VIEWPORT)
        except NoSuchElementException:
            return None
    
    def get_slides_container(self):
        """Get slides container element"""
        try:
            return self.find_element_in_blade(self.SLIDES_CONTAINER)
        except NoSuchElementException:
            return None
    
    def get_all_slides(self):
        """Get all slide elements"""
        return self.find_elements_in_blade(self.SLIDES)
    
    def get_slide_count(self):
        """Get total number of slides"""
        return len(self.get_all_slides())
    
    def get_active_slide(self):
        """Get currently active slide"""
        slides = self.get_all_slides()
        for slide in slides:
            if slide.get_attribute("data-slide-active") == "true":
                return slide
        return None
    
    def get_active_slide_index(self):
        """Get index of active slide"""
        active = self.get_active_slide()
        if active:
            return int(active.get_attribute("data-slide-index"))
        return None
    
    def has_controls(self):
        """Check if carousel has controls container"""
        return self.element_exists_in_blade(self.CONTROLS_CONTAINER)
    
    def get_controls_container(self):
        """Get controls container element"""
        try:
            return self.find_element_in_blade(self.CONTROLS_CONTAINER)
        except NoSuchElementException:
            return None
    
    def has_progress_bar(self):
        """Check if carousel has progress bar"""
        return self.element_exists_in_blade(self.PROGRESS_BAR)
    
    def has_previous_button(self):
        """Check if carousel has previous button"""
        return self.element_exists_in_blade(self.PREVIOUS_BUTTON)
    
    def has_next_button(self):
        """Check if carousel has next button"""
        return self.element_exists_in_blade(self.NEXT_BUTTON)
    
    def get_previous_button(self):
        """Get previous button element"""
        try:
            return self.find_element_in_blade(self.PREVIOUS_BUTTON)
        except NoSuchElementException:
            return None
    
    def get_next_button(self):
        """Get next button element"""
        try:
            return self.find_element_in_blade(self.NEXT_BUTTON)
        except NoSuchElementException:
            return None
    
    def is_previous_button_enabled(self):
        """Check if previous button is enabled"""
        button = self.get_previous_button()
        if button:
            return button.get_attribute("disabled") is None
        return False
    
    def is_next_button_enabled(self):
        """Check if next button is enabled"""
        button = self.get_next_button()
        if button:
            return button.get_attribute("disabled") is None
        return False
    
    def click_previous(self):
        """Click previous button if enabled"""
        button = self.get_previous_button()
        if button and self.is_previous_button_enabled():
            button.click()
    
    def click_next(self):
        """Click next button if enabled"""
        button = self.get_next_button()
        if button and self.is_next_button_enabled():
            button.click()