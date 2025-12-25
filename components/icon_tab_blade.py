from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade


class IconTabBlade(BaseBlade):
    """Icon Tab blade component"""
    
    # Note: Container has no unique data-testid - must be found by ID on each page
    # Example: driver.find_element(By.ID, "icon-tab-choose-your-champion")
    
    # Main container locators

    ICON_TAB_MAIN = (By.CSS_SELECTOR, ".icon-tab--main")
    ICON_TAB_MEDIA = (By.CSS_SELECTOR, ".icon-tab--media")

    # Backdrop locators

    BACKDROP = (By.CSS_SELECTOR, ".icon-tab--backdrop-main")
    BACKGROUND =(By.CSS_SELECTOR, ".icon-tab--backdrop-full-background")
    
    # Blade header locators (inside icon-tab--main)

    HEADER_LINKS = (By.CSS_SELECTOR, ".icon-tab-header-centered-links")
    
    # Tabs carousel locators

    TAB_LABEL = (By.CSS_SELECTOR, ".icon-tab-label")
    
    # Media section locators

    ICON_TAB_MEDIA_ELEMENT = (By.CSS_SELECTOR, "[data-testid='icon-tab-media']")
    MEDIA_TITLE = (By.CSS_SELECTOR, ".icon-tab-media-title")
    MEDIA_SUBTITLE = (By.CSS_SELECTOR, ".icon-tab-media-subtitle")
    MEDIA_DESCRIPTION = (By.CSS_SELECTOR, ".icon-tab-media-description")
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade (must be found by ID)
        """
        super().__init__(driver, blade_element)
    
    # Main sections

    def has_main_section(self):
        """Check if blade has main section"""
        return self.element_exists_in_blade(self.ICON_TAB_MAIN)
    
    def has_media_section(self):
        """Check if blade has media section"""
        return self.element_exists_in_blade(self.ICON_TAB_MEDIA)

    # CTA methods

    def has_header_links(self):
        """Check if header has CTA links section"""
        return self.has_element(self.HEADER_LINKS)
    
    
    # Tabs carousel specific methods (blade-specific logic)
    
    def get_tab_labels(self):
        """Get all tab label texts"""
        labels = self.find_elements_in_blade(self.TAB_LABEL)
        return [label.text for label in labels]
    
    # Tab interaction methods

    def click_tab_by_index(self, index):
        """Click tab  by index"""
        tabs = self.get_all_slides()
        if 0 <= index < len(tabs):
         tabs[index].click()
        else:
            raise IndexError(f"Tab index {index} out of range (0-{len(tabs)-1})")
    
    # Media section methods (blade-specific)

    def has_media_element(self):
        """Check if blade has media element"""
        return self.element_exists_in_blade(self.ICON_TAB_MEDIA_ELEMENT)

    def is_media_element_visible(self):
        """Check if media element is visible"""
        return self.is_element_visible(self.ICON_TAB_MEDIA_ELEMENT)
    
    def get_media_title_text(self):
        """Get media title text"""
        return self.get_element_text(self.MEDIA_TITLE)
    
    def get_media_subtitle_text(self):
        """Get media subtitle text"""
        return self.get_element_text(self.MEDIA_SUBTITLE)
    
    def get_media_description_text(self):
        """Get media description rich text"""
        try:
            desc_element = self.find_element_in_blade(self.MEDIA_DESCRIPTION)
            return desc_element.text
        except:
            return None
        
    # Backdrop section methods (Icon Tab blade-specific)

    def has_icon_tab_main_backdrop(self):
        """Check if blade has backdrop"""
        return self.element_exists_in_blade(self.BACKDROP)
        
    def has_icon_tab_full_backdrop_background(self):
        """Check if backdrop has background layer"""
        return self.element_exists_in_blade(self.BACKGROUND)