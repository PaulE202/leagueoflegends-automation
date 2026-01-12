import pytest
from pages.home_page import HomePage


class TestGameSimpleMasthead:
    """Tests for Game Simple Masthead blade on Homepage"""
    
    @pytest.fixture(scope="session")
    def masthead(self, home_page):
        """Get blade once for all tests"""
        return home_page.get_game_simple_masthead()
    
    @pytest.fixture(scope="class")
    def video_element(self, masthead):
        """Get video element from backdrop background"""
        background = masthead.get_backdrop_background()
        try:
            return background.find_element("tag name", "video")
        except:
            pytest.fail("Video element not found in backdrop background")
    
    # Structural tests
    
    def test_masthead_is_visible(self, masthead):
        """Verify masthead blade is visible on page"""
        assert masthead.is_visible(), "Blade should be visible"
    
    def test_backdrop_exists(self, masthead):
        """Verify masthead has backdrop"""
        assert masthead.has_backdrop(), "Blade should have backdrop"
    
    def test_backdrop_has_background(self, masthead):
        """Verify backdrop has background layer"""
        assert masthead.has_backdrop_background(), "Backdrop should have background layer"
    
    # Video tests

    def test_video_is_displayed(self, video_element):
        """Verify video element is dispalyed"""
        assert video_element.is_displayed(), \
            "Video should be displayed"
    
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
    
    # Logo tests
    
    def test_logo_is_visible(self, masthead):
        """Verify logo is visible"""
        assert masthead.is_logo_visible(), "Logo should be visible"
    
    def test_logo_has_src(self, masthead):
        """Verify logo has valid source"""
        logo = masthead.get_logo_element()
        src = logo.get_attribute("src")
    
        assert src not in (None, ""), "Logo should have non-empty src"
    
    # Blade header tests
    
    def test_blade_header_exists(self, masthead):
        """Verify blade header existst"""
        assert masthead.has_blade_header(), "Blade should have blade header"
    
    def test_h1_title_text(self, masthead):
        """Verify title has expected text"""
        h1_text = masthead.get_h1_title()
        expected_text = "LEAGUE OF LEGENDS — A 5V5 MOBA WHERE TEAMS BATTLE TO DESTROY THE ENEMY NEXUS"
        
        assert h1_text == expected_text, f"Title should be '{expected_text}', got '{h1_text}'"
    
    # CTA tests
    
    def test_primary_cta_is_visible(self, masthead):
        """Verify primary CTA is visible"""
        assert masthead.is_primary_cta_visible(), "Blade primary CTA should be visible"
    
    def test_primary_cta_text(self, masthead):
        """Verify primary CTA has correct text"""
        cta_text = masthead.get_primary_cta_text()
        expected_text = "PLAY FOR FREE"
        
        assert expected_text in cta_text, f"Blade primary CTA should contain '{expected_text}', got '{cta_text}'"
    
    def test_primary_cta_href(self, masthead):
        """Verify primary CTA has correct href"""
        cta = masthead.get_primary_cta_element()
        href = cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/en-us/signup/redownload"
        
        assert href == expected_href, f"Blade primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, masthead):
        """Verify primary CTA opens in new tab"""
        cta = masthead.get_primary_cta_element()
        target = cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Blade primary CTA target should be '{expected_target}', got '{target}'"