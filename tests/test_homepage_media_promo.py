import pytest
from pages.home_page import HomePage

class TestMediaPromo:
    """Tests for Media Promo blade on Homepage"""

    @pytest.fixture(scope="session")
    def media_promo(self, home_page):
        """Get Media Promo blade and scroll into view"""
        blade = home_page.get_media_promo()
        blade.scroll_into_view()
        return blade
    
    # Structural tests

    def test_media_promo_is_displayed(self, media_promo):
        """Verify blade is displayed on page"""
        assert media_promo.is_visible(), "Media Promo blade should be visible"
    
    def test_backdrop_exists(self, media_promo):
        """Verify backdrop exists"""
        assert media_promo.has_backdrop(), "Media Promo blade should have backdrop"
    
    def test_backdrop_background_has_image(self, media_promo):
        """Verify backdrop background contains image"""
        assert media_promo.backdrop_background_has_image(), "Media Promo backdrop background should contain image"

    # Heading tests

    def test_heading_exists(self, media_promo):
        """Verify heading section exists"""
        assert media_promo.has_heading(), "Media Promo blade should have heading section"
    
    def test_supertitle_text(self, media_promo):
        """Verify supertitle has expected content"""
        super_title_text = media_promo.get_supertitle_text()
        expected_supertitle_text = "SLAY WITH"

        assert super_title_text == expected_supertitle_text, f"Supertitle should be '{expected_supertitle_text}', got '{super_title_text}'"

    def test_title_text(self, media_promo):
        """Verify title has expected content"""
        title_text = media_promo.get_title_text()
        expected_title = "STYLE"

        assert title_text == expected_title, f"Title should be '{expected_title}', got '{title_text}'"

    def test_description_has_text(self, media_promo):
        """Verify description is displayed"""
        description_text = media_promo.get_description_text()
        assert description_text is not None, "Description should exist"
        assert len(description_text) > 0, "Description should have text"
    
    # CTA tests

    def test_links_section_exists(self, media_promo):
        """Verify Media Promo has links section"""
        assert media_promo.has_links_section(), "Media Promo should have links section"
    
    def test_primary_cta_exists(self, media_promo):
        """Verify primary CTA is displayed"""
        assert media_promo.has_primary_cta(), "Media Promo should have primary CTA"
    
    def test_primary_cta_text(self, media_promo):
        """Verify primary CTA has correct text"""
        primary_cta_text = media_promo.get_primary_cta_text()
        expected_primary_cta_text = "PLAY NOW"
        
        assert primary_cta_text == expected_primary_cta_text, f"CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, media_promo):
        """Verify primary CTA has correct href"""
        primary_cta = media_promo.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, f"CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, media_promo):
        """Verify primary CTA opens new tab"""
        primary_cta = media_promo.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, f"CTA target should be '{expected_target}', got '{target}'"

    # Featured media tests

    def test_featured_media_exists(self, media_promo):
        """Verify featured media section exists"""
        assert media_promo.has_featured_media(), "Media Promo should have a featured media section"
    
    def test_featured_media_is_image(self, media_promo):
        """Verify featured media is an image"""
        assert media_promo.featured_media_is_image(), "Media Promo should have an image as the featured media"
    
    def test_featured_media_is_displayed(self, media_promo):
        """Verify featured image is displayed"""
        assert media_promo.is_featured_media_visible(), "Media Promo featured media should be displayed"