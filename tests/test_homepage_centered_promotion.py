import pytest
from pages.home_page import HomePage

class TestCenteredPromotion:
    """Tests for Centered Promotion blade on the Homepage"""

    @pytest.fixture(scope="session")
    def centered_promotion(self, home_page):
        """Get Centered Promotion once for all tests"""
        return home_page.get_centered_promotion()
    
    # Structural tests
    
    def test_centered_promotion_is_displayed(self, centered_promotion):
        """Verify blade is displayed on page"""
        assert centered_promotion.is_visible(), "Centered Promotion should be visible"
    
    def test_backdrop_exists(self, centered_promotion):
        """Verify blade has backdrop"""
        assert centered_promotion.has_backdrop(), "Centered Promotion should have backdrop"
    
    def test_backdrop_has_background(self, centered_promotion):
        """Verify backdrop has background layer"""
        assert centered_promotion.has_backdrop_background(), \
            "Centered Promotion backdrop should have background layer"
    
    # CTA tests
    
    def test_links_section_exists(self, centered_promotion):
        """Verify links section exist"""
        assert centered_promotion.has_links_section(), "Centered Promotion should have links section"

    def test_primary_cta_exists(self, centered_promotion):
        """Verify primary CTA exists"""
        assert centered_promotion.has_primary_cta(), "Centered Promotion should have primary CTA"

    def test_primary_cta_is_displayed(self, centered_promotion):
        """Verify primary CTA is displayed"""
        assert centered_promotion.is_primary_cta_visible(), "Centered Promotion primary CTA should be visible"
    
    def test_primary_cta_text(self, centered_promotion):
        """Verify primary CTA has correct text"""
        primary_cta_text = centered_promotion.get_primary_cta_text()
        expected_primary_cta_text = "PLAY FOR FREE"
        
        assert primary_cta_text == expected_primary_cta_text, \
            f"Centered Promotion primary CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, centered_promotion):
        """Verify primary CTA has correct href"""
        primary_cta = centered_promotion.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, \
            f"Centered Promotion primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, centered_promotion):
        """Verify primary CTA opens new tab"""
        primary_cta = centered_promotion.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Centered Promotion primary CTA target should be '{expected_target}', got '{target}'"
