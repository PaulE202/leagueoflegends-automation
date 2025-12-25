import pytest
from pages.home_page import HomePage

class TestCenteredPromotion:
    """Tests for Centered Promotion blade on the Homepage"""

    @pytest.fixture(scope="session")
    def centered_promotion(self, home_page):
        """Get blade once for all tests"""
        return home_page.get_centered_promotion()
    
    @pytest.fixture(scope="class")
    def video_element(self, centered_promotion):
        """Get video element from backdrop background"""
        background = centered_promotion.get_backdrop_background()
        try:
            return background.find_element("tag name", "video")
        except:
            pytest.fail("Video element not found in backdrop background")
    
    # Structural tests
    
    def test_centered_promotion_is_visible(self, centered_promotion):
        """Verify blade is visible on page"""
        assert centered_promotion.is_visible(), "Blade should be visible"
    
    def test_backdrop_exists(self, centered_promotion):
        """Verify blade has backdrop"""
        assert centered_promotion.has_backdrop(), "Blade should have backdrop"
    
    def test_backdrop_has_background(self, centered_promotion):
        """Verify backdrop has background layer"""
        assert centered_promotion.has_backdrop_background(), \
            "Blade backdrop should have background layer"
        
    # Video tests

    def test_video_has_src(self, video_element):
        """Verify video has valid source"""
        sources = video_element.find_elements("tag name", "source")
        direct_src = video_element.get_attribute("src")
    
        has_source_src = any(s.get_attribute("src") not in (None, "") for s in sources)
        has_direct_src = direct_src not in (None, "")
    
        assert has_source_src or has_direct_src, \
            "Video should have non-empty source"

    def test_video_is_autoplaying(self, video_element):
        """Verify video has autoplay attribute"""
        assert video_element.get_attribute("autoplay") is not None, \
            "Video should have autoplay attribute"

    def test_video_is_muted(self, video_element):
        """Verify video is muted"""
        assert video_element.get_attribute("muted") is not None, \
            "Video should be muted"
        
    def test_video_is_looping(self, video_element):
        """Verify video is looping"""
        assert video_element.get_attribute("loop") is not None, \
            "Video should be looping"
    
    # CTA tests
    
    def test_links_section_exists(self, centered_promotion):
        """Verify links section exist"""
        assert centered_promotion.has_links_section(), "Blade should have links section"

    def test_primary_cta_is_visible(self, centered_promotion):
        """Verify primary CTA is visible"""
        assert centered_promotion.is_primary_cta_visible(), "Blade primary CTA should be visible"
    
    def test_primary_cta_text(self, centered_promotion):
        """Verify primary CTA has correct text"""
        primary_cta_text = centered_promotion.get_primary_cta_text()
        expected_primary_cta_text = "PLAY FOR FREE"
        
        assert primary_cta_text == expected_primary_cta_text, \
            f"Blade primary CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, centered_promotion):
        """Verify primary CTA has correct href"""
        primary_cta = centered_promotion.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, \
            f"Blade primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, centered_promotion):
        """Verify primary CTA opens new tab"""
        primary_cta = centered_promotion.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Blade primary CTA target should be '{expected_target}', got '{target}'"
