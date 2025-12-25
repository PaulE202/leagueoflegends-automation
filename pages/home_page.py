from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.game_simple_masthead_blade import GameSimpleMastheadBlade
from components.article_card_carousel_blade import ArticleCardCarouselBlade
from components.icon_tab_blade import IconTabBlade
from components.media_promo_blade import MediaPromoBlade
from components.centered_promotion_blade import CenteredPromotionBlade


class HomePage(BasePage):
    """League of Legends homepage"""
    
    # Page URL
    URL = "https://www.leagueoflegends.com/en-us/"
    
    # Blade locators (by ID since blades use IDs)
    GAME_SIMPLE_MASTHEAD = (By.ID, "section-home-hero")
    ARTICLE_CARD_CAROUSEL = (By.ID, "article-carousel-featured-news")
    ICON_TAB_CHOOSE_CHAMPION = (By.ID, "icon-tab-choose-your-champion")
    ICON_TAB_MULTIPLE_WAYS = (By.ID, "section-home-multiplewaystoplay")
    MEDIA_PROMO = (By.ID, "home-section-slaywithstyle")
    CENTERED_PROMOTION = (By.ID, "centered-promotion-play-for-free")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def load(self):
        """Navigate to homepage and wait for page load"""
        self.driver.get(self.URL)
        self.wait_for_page_load()
    
    def is_loaded(self):
        """Verify homepage is loaded"""
        return self.driver.current_url == self.URL
    
    # Blade retrieval methods - return blade component instances
    
    def get_game_simple_masthead(self):
        """Get Game Simple Masthead blade component"""
        blade_element = self.wait_for_element(self.GAME_SIMPLE_MASTHEAD)
        return GameSimpleMastheadBlade(self.driver, blade_element)
    
    def get_article_card_carousel(self):
        """Get Article Card Carousel blade component"""
        blade_element = self.wait_for_element(self.ARTICLE_CARD_CAROUSEL)
        return ArticleCardCarouselBlade(self.driver, blade_element)
    
    def get_icon_tab_choose_champion(self):
        """Get Icon Tab (Choose Your Champion) blade component"""
        blade_element = self.wait_for_element(self.ICON_TAB_CHOOSE_CHAMPION)
        return IconTabBlade(self.driver, blade_element)
    
    def get_icon_tab_multiple_ways(self):
        """Get Icon Tab (Multiple Ways to Play) blade component"""
        blade_element = self.wait_for_element(self.ICON_TAB_MULTIPLE_WAYS)
        return IconTabBlade(self.driver, blade_element)
    
    def get_media_promo(self):
        """Get Media Promo blade component"""
        blade_element = self.wait_for_element(self.MEDIA_PROMO)
        return MediaPromoBlade(self.driver, blade_element)
    
    def get_centered_promotion(self):
        """Get Centered Promotion blade component"""
        blade_element = self.wait_for_element(self.CENTERED_PROMOTION)
        return CenteredPromotionBlade(self.driver, blade_element)