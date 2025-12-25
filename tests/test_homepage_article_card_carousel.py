import pytest
from pages.home_page import HomePage


class TestArticleCardCarousel:
    """Tests for Article Card Carousel (Featured News) blade on Homepage"""
    
    @pytest.fixture(scope="session")
    def carousel_blade(self, home_page):
        """Get blade once for all tests"""
        return home_page.get_article_card_carousel()
    
    # Structural tests
    
    def test_blade_is_visible(self, carousel_blade):
        """Verify blade is visible on page"""
        assert carousel_blade.is_visible(), "Blade should be visible"
    
    def test_backdrop_exists(self, carousel_blade):
        """Verify blade has backdrop"""
        assert carousel_blade.has_backdrop(), "Blade should have backdrop"
    
    def test_backdrop_has_background(self, carousel_blade):
        """Verify backdrop has background layer"""
        assert carousel_blade.has_backdrop_background(), "Blade backdrop should have background layer"
    
    # Title tests
    
    def test_title_text(self, carousel_blade):
        """Verify title has correct text"""
        title_text = carousel_blade.get_title()
        expected_title = "FEATURED NEWS"

        assert title_text == expected_title, f"Blade title should be '{expected_title}', got '{title_text}'"
    
    # CTA tests
    
    def test_tertiary_cta_is_visible(self, carousel_blade):
        """Verify tertiary CTA is visible"""
        assert carousel_blade.is_tertiary_cta_visible(), "Blade should have tertiary CTA"
    
    def test_tertiary_cta_text(self, carousel_blade):
        """Verify tertiary CTA has correct text"""
        cta_text = carousel_blade.get_tertiary_cta_text()
        expected_text = "VIEW ALL"
    
        assert expected_text in cta_text, f"CTA should contain '{expected_text}', got '{cta_text}'"
    
    def test_tertiary_cta_href(self, carousel_blade):
        """Verify tertiary CTA has correct href"""
        cta = carousel_blade.get_tertiary_cta_element()
        href = cta.get_attribute("href")
        expected_href = "https://www.leagueoflegends.com/en-us/news/"
        
        assert href == expected_href, f"CTA href should be '{expected_href}', got '{href}'"
    
    def test_tertiary_cta_opens_same_tab(self, carousel_blade):
        """Verify tertiary CTA opens in the same tab (no target attribute)"""
        tertiary_cta = carousel_blade.get_tertiary_cta_element()
        target = tertiary_cta.get_attribute("target")
        
        assert not target, \
            f"Blade tertiary CTA should have no target attribute, got '{target}'"
    
    # Carousel tests

    def test_carousel_exists(self, carousel_blade):
        """Verify carousel exists"""
        assert carousel_blade.has_carousel(), "Blade should have carousel"
    
    def test_carousel_has_three_slides(self, carousel_blade):
        """Verify carousel has exactly 3 slides"""
        slide_count = carousel_blade.get_slide_count()
        expected_silde_count = 3
        
        assert slide_count == expected_silde_count, f"Carousel should have '{expected_silde_count}' slides, found '{slide_count}'"
    
    def test_slides_have_valid_links(self, carousel_blade):
        """Verify each slide has a valid href"""
        slides = carousel_blade.get_all_slides()
        assert slides, "Should have slides"  # Prevent silent pass
        
        for i, slide in enumerate(slides):
            try:
                link = slide.find_element("tag name", "a")
                href = link.get_attribute("href")

                assert href and href.startswith("http"), \
                f"Slide {i} should have valid http/https URL, got '{href}'"    
            except:
                pytest.fail(f"Slide {i} does not have an anchor tag")

    
    # Controls tests
    
    def test_controls_exist(self, carousel_blade):
        """Verify carousel controls container exists"""
        assert carousel_blade.has_controls(), "Carousel should have controls container"
    
    def test_progress_bar_exists(self, carousel_blade):
        """Verify progress bar exists"""
        assert carousel_blade.has_progress_bar(), "Carousel should have progress bar"
    
    def test_previous_button_exists(self, carousel_blade):
        """Verify previous button exists"""
        assert carousel_blade.has_previous_button(), "Carousel should have previous button"
    
    def test_next_button_exists(self, carousel_blade):
        """Verify next button exists"""
        assert carousel_blade.has_next_button(), "Carousel should have next button"