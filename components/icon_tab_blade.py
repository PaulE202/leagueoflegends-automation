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
    SUPERTITLE = (By.CSS_SELECTOR, "[data-testid='supertitle']")
    TITLE = (By.CSS_SELECTOR, "[data-testid='title']")
    DESCRIPTION = (By.CSS_SELECTOR, "[data-testid='description']")
    HEADER_LINKS = (By.CSS_SELECTOR, ".icon-tab-header-centered-links")
    CTA_PRIMARY = (By.CSS_SELECTOR, "[data-testid='cta-primary']")
    CTA_SECONDARY = (By.CSS_SELECTOR, "[data-testid='cta-secondary']")
    CTA_CONTENT = (By.CSS_SELECTOR, "[data-testid='cta-content']")
    
    # Tabs carousel locators
    ICON_TAB_TABS = (By.CSS_SELECTOR, ".icon-tab--tabs")
    TAB_LABEL = (By.CSS_SELECTOR, ".icon-tab-label")
    
    # Media section locators
    MEDIA_POSITION = (By.CSS_SELECTOR, ".icon-tab-media-position")
    ICON_TAB_MEDIA_ELEMENT = (By.CSS_SELECTOR, "[data-testid='icon-tab-media']")
    MEDIA_CONTENT = (By.CSS_SELECTOR, ".icon-tab-media-content")
    MEDIA_CONTENT_HEADER = (By.CSS_SELECTOR, ".icon-tab-media-content-header")
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
    
    # Note: Backdrop methods inherited from BaseBlade
    # Note: All carousel methods inherited from BaseBlade
    
    # Main sections
    def has_main_section(self):
        """Check if blade has icon-tab--main section"""
        return self.element_exists_in_blade(self.ICON_TAB_MAIN)
    
    def has_media_section(self):
        """Check if blade has icon-tab--media section"""
        return self.element_exists_in_blade(self.ICON_TAB_MEDIA)
    
    # Blade header methods - using inherited and specific methods
    
    def has_description(self):
        """Check if header has description"""
        return self.has_element(self.DESCRIPTION)
    
    def get_description_text(self):
        """Get description rich text"""
        try:
            desc_element = self.find_element_in_blade(self.DESCRIPTION)
            return desc_element.text
        except:
            return None
    
    # CTA methods - using inherited generic methods from BaseBlade
    def has_header_links(self):
        """Check if header has CTA links section"""
        return self.has_element(self.HEADER_LINKS)
    
    def has_primary_cta(self):
        """Check if header has primary CTA"""
        return self.has_cta(self.CTA_PRIMARY)
    
    def is_primary_cta_visible(self):
        """Check if primary CTA is visible"""
        return self.is_cta_visible(self.CTA_PRIMARY)
    
    def is_secondary_cta_visible(self):
        """Check if secondary CTA is visible"""
        return self.is_cta_visible(self.CTA_SECONDARY)
    
    def has_secondary_cta(self):
        """Check if header has secondary CTA"""
        return self.has_cta(self.CTA_SECONDARY)
    
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
    
    def click_primary_cta(self):
        """Click primary CTA"""
        self.click_cta(self.CTA_PRIMARY)
    
    def click_secondary_cta(self):
        """Click secondary CTA"""
        self.click_cta(self.CTA_SECONDARY)
    
    # Tabs carousel specific methods (blade-specific logic)
    def has_tabs_carousel(self):
        """Check if blade has tabs carousel"""
        return self.element_exists_in_blade(self.ICON_TAB_TABS)
    
    def get_tab_labels(self):
        """Get all tab label texts"""
        labels = self.find_elements_in_blade(self.TAB_LABEL)
        return [label.text for label in labels]
    
    # Tab interaction methods
    def click_tab_by_index(self, index):
        """Click tab slide by index"""
        slides = self.get_all_slides()
        if 0 <= index < len(slides):
         slides[index].click()
        else:
            raise IndexError(f"Tab index {index} out of range (0-{len(slides)-1})")

    def click_tab_by_label(self, label_text):
        """Click tab slide by its label text"""
        slides = self.get_all_slides()
        labels = self.get_tab_labels()
    
        for i, label in enumerate(labels):
            if label.lower() == label_text.lower():
                slides[i].click()
                return True
    
        raise ValueError(f"Tab with label '{label_text}' not found. Available: {labels}")

    def get_current_media_title(self):
        """Get current media title (changes when tab is clicked)"""
        return self.get_media_title_text()

    def get_current_media_subtitle(self):
        """Get current media subtitle (changes when tab is clicked)"""
        return self.get_media_subtitle_text()

    def verify_media_changed(self, previous_title, previous_subtitle):
        """
        Verify media content changed after tab interaction
        Returns: True if either title or subtitle changed
        """
        current_title = self.get_current_media_title()
        current_subtitle = self.get_current_media_subtitle()
    
        return current_title != previous_title or current_subtitle != previous_subtitle       
    
    # Media section methods (blade-specific)
    def has_media_element(self):
        """Check if blade has media element"""
        return self.element_exists_in_blade(self.ICON_TAB_MEDIA_ELEMENT)
    
    def get_media_element(self):
        """Get media element (image or video)"""
        try:
            return self.find_element_in_blade(self.ICON_TAB_MEDIA_ELEMENT)
        except:
            return None
    
    def media_is_video(self):
        """Check if media is video"""
        media = self.get_media_element()
        if media:
            return media.tag_name.lower() == "video"
        return False
    
    def media_is_image(self):
        """Check if media is image"""
        media = self.get_media_element()
        if media:
            return media.tag_name.lower() == "img"
        return False
    
    def has_media_title(self):
        """Check if media section has title"""
        return self.has_element(self.MEDIA_TITLE)
    
    def get_media_title_text(self):
        """Get media title text"""
        return self.get_element_text(self.MEDIA_TITLE)
    
    def has_media_subtitle(self):
        """Check if media section has subtitle"""
        return self.has_element(self.MEDIA_SUBTITLE)
    
    def get_media_subtitle_text(self):
        """Get media subtitle text"""
        return self.get_element_text(self.MEDIA_SUBTITLE)
    
    def has_media_description(self):
        """Check if media section has description"""
        return self.has_element(self.MEDIA_DESCRIPTION)
    
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
    
    def get_icon_tab_main_backdrop_element(self):
        """Get backdrop element if exists"""
        try:
            return self.find_element_in_blade(self.BACKDROP)
        except NoSuchElementException:
            return None
    
    def has_icon_tab_full_backdrop_background(self):
        """Check if backdrop has background layer"""
        return self.element_exists_in_blade(self.BACKGROUND)
    
    
    def get_icon_tab_full_backdrop_background(self):
        """Get backdrop background element"""
        try:
            return self.find_element_in_blade(self.BACKGROUND)
        except NoSuchElementException:
            return None  
    
    def icon_tab_full_backdrop_background_has_image(self):
        """Check if backdrop background contains image"""
        background = self.get_icon_tab_full_backdrop_background()
        if background:
            try:
                background.find_element(By.TAG_NAME, "img")
                return True
            except NoSuchElementException:
                pass
        return False
