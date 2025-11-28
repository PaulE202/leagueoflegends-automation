import pytest
from pages.home_page import HomePage


class TestGameSimpleMasthead:
    """Tests for Game Simple Masthead blade on Homepage"""
    
    @pytest.fixture(scope="session")
    def masthead(self, home_page):
        """Get Game Simple Masthead blade once for all tests"""
        return home_page.get_game_simple_masthead()
    
    # Structural tests
    
    def test_masthead_is_displayed(self, masthead):
        """Verify masthead blade is displayed on page"""
        assert masthead.is_visible(), "Game Simple Masthead should be visible"
    
    def test_backdrop_exists(self, masthead):
        """Verify masthead has backdrop"""
        assert masthead.has_backdrop(), "Masthead should have backdrop"
    
    def test_backdrop_has_background(self, masthead):
        """Verify backdrop has background layer"""
        assert masthead.has_backdrop_background(), "Backdrop should have background layer"
    
    # Video tests
    
    def test_video_is_displayed(self, masthead):
        """Verify backdrop background contains video"""
        assert masthead.backdrop_background_has_video(), "Backdrop background should contain video"
    
    def test_video_has_src(self, masthead):
        """Verify video has source"""
        background = masthead.get_backdrop_background()
        video = background.find_element("tag name", "video")
        
        # Check for source element or src attribute
        sources = video.find_elements("tag name", "source")
        has_src = len(sources) > 0 or video.get_attribute("src")
        
        assert has_src, "Video should have source"
    
    def test_video_is_autoplaying(self, masthead):
        """Verify video has autoplay attribute"""
        background = masthead.get_backdrop_background()
        video = background.find_element("tag name", "video")
        
        autoplay = video.get_attribute("autoplay")
        assert autoplay is not None, "Video should have autoplay attribute"
    
    def test_video_is_muted(self, masthead):
        """Verify video is muted"""
        background = masthead.get_backdrop_background()
        video = background.find_element("tag name", "video")
        
        muted = video.get_attribute("muted")
        assert muted is not None, "Video should be muted"
    
    # Logo tests
    
    def test_logo_is_displayed(self, masthead):
        """Verify logo is displayed"""
        assert masthead.has_logo(), "Masthead should have logo"
        assert masthead.is_logo_visible(), "Logo should be visible"
    
    # Blade header tests
    
    def test_blade_header_exists(self, masthead):
        """Verify blade header exists in content"""
        assert masthead.has_blade_header(), "Masthead should have blade header"
    
    def test_h1_title_is_displayed(self, masthead):
        """Verify H1 title is displayed"""
        h1_text = masthead.get_h1_title()
        assert h1_text is not None, "H1 title should exist"
        assert len(h1_text) > 0, "H1 title should have text"
    
    def test_h1_title_content(self, masthead):
        """Verify H1 title has expected content"""
        h1_text = masthead.get_h1_title()
        expected_text = "LEAGUE OF LEGENDS — A 5V5 MOBA WHERE TEAMS BATTLE TO DESTROY THE ENEMY NEXUS"
        
        assert h1_text == expected_text, f"H1 title should be '{expected_text}', got '{h1_text}'"
    
    # CTA tests
    
    def test_primary_cta_is_displayed(self, masthead):
        """Verify primary CTA is displayed"""
        assert masthead.has_primary_cta(), "Masthead should have primary CTA"
        assert masthead.is_primary_cta_visible(), "Primary CTA should be visible"
    
    def test_primary_cta_text(self, masthead):
        """Verify primary CTA has correct text"""
        cta_text = masthead.get_primary_cta_text()
        expected_text = "PLAY FOR FREE"
        
        assert expected_text in cta_text, f"CTA should contain '{expected_text}', got '{cta_text}'"
    
    def test_primary_cta_href(self, masthead):
        """Verify primary CTA has correct href"""
        cta = masthead.get_primary_cta_element()
        href = cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/en-us/signup/redownload"
        
        assert href == expected_href, f"CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, masthead):
        """Verify primary CTA opens in new tab"""
        cta = masthead.get_primary_cta_element()
        target = cta.get_attribute("target")
        
        assert target == "_blank", f"CTA should open in new tab (target='_blank'), got target='{target}'"