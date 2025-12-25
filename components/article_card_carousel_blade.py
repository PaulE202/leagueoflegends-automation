from selenium.webdriver.common.by import By
from components.base_blade import BaseBlade


class ArticleCardCarouselBlade(BaseBlade):
    """Article Card Carousel blade component"""
    
    def __init__(self, driver, blade_element):
        """
        Args:
            driver: WebDriver instance
            blade_element: The WebElement representing this blade
        """
        super().__init__(driver, blade_element)
       