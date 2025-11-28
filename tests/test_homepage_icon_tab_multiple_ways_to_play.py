import pytest
from pages.home_page import HomePage


class TestIconTabMultipleWaysToPlay:
    """Tests for Icon Tab (Multiple Ways to Play) blade on the Homepage"""

    @pytest.fixture(scope="session")
    def icon_tab_multiple_ways_to_play(self, home_page):
        """Get Icon Tab (Multiple Ways to Play) once for all tests"""
        return home_page.get_icon_tab_multiple_ways()

    # Structural tests
    
    def test_icon_tab_multiple_ways_to_play_is_displayed(self, icon_tab_multiple_ways_to_play):
        """Verify blade is displayed on page"""
        assert icon_tab_multiple_ways_to_play.is_visible(), "Icon Tab (Multiple Ways to Play) should be visible"
    
    def test_backdrop_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has backdrop"""
        assert icon_tab_multiple_ways_to_play.has_icon_tab_main_backdrop(), "Icon Tab (Multiple Ways to Play) should have backdrop"
    
    def test_backdrop_has_background(self, icon_tab_multiple_ways_to_play):
        """Verify backdrop has background layer"""
        assert icon_tab_multiple_ways_to_play.has_icon_tab_full_backdrop_background(), \
            "Icon Tab (Multiple Ways to Play) backdrop should have background layer"

    def test_main_section_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has main section"""
        assert icon_tab_multiple_ways_to_play.has_main_section(), "Icon Tab (Multiple Ways to Play) should have main section"

    def test_media_section_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has media section"""
        assert icon_tab_multiple_ways_to_play.has_media_section(), "Icon Tab (Multiple Ways to Play) should have media section"
    
    # Blade header tests

    def test_blade_header_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade header exists"""
        assert icon_tab_multiple_ways_to_play.has_blade_header(), "Icon Tab (Multiple Ways to Play) should have blade header"
    
    
    def test_supertitle_text(self, icon_tab_multiple_ways_to_play):
        """Verify supertitle has expected text"""
        super_title_text = icon_tab_multiple_ways_to_play.get_super_title()
        expected_supertitle_text = "MULTIPLE WAYS TO"

        assert super_title_text == expected_supertitle_text, \
            f"Icon Tab (Multiple Ways to Play) supertitle should be '{expected_supertitle_text}', got '{super_title_text}'"

    def test_title_text(self, icon_tab_multiple_ways_to_play):
        """Verify title has expected text"""
        title_text = icon_tab_multiple_ways_to_play.get_title()
        expected_title = "PLAY"

        assert title_text == expected_title, f"Icon Tab (Multiple Ways to Play) title should be '{expected_title}', got '{title_text}'"

    def test_description_has_text(self, icon_tab_multiple_ways_to_play):
        """Verify description is displayed"""
        description_text = icon_tab_multiple_ways_to_play.get_description()
        assert description_text is not None, "Icon Tab (Multiple Ways to Play) description should exist"
        assert len(description_text) > 0, "Icon Tab (Multiple Ways to Play) description should have text"

    # CTA tests
    
    def test_header_links_exists(self, icon_tab_multiple_ways_to_play):
        """Verify header links exist"""
        assert icon_tab_multiple_ways_to_play.has_header_links(), "Icon Tab (Multiple Ways to Play) should have header links section"

    def test_primary_cta_exists(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA exists"""
        assert icon_tab_multiple_ways_to_play.has_primary_cta(), "Icon Tab (Multiple Ways to Play) should have primary CTA"

    def test_primary_cta_is_displayed(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA is displayed"""
        assert icon_tab_multiple_ways_to_play.is_primary_cta_visible(), "Icon Tab (Multiple Ways to Play) primary CTA should be visible"
    
    def test_primary_cta_text(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA has correct text"""
        primary_cta_text = icon_tab_multiple_ways_to_play.get_primary_cta_text()
        expected_primary_cta_text = "PLAY NOW"
        
        assert primary_cta_text == expected_primary_cta_text, \
            f"Icon Tab (Multiple Ways to Play) primary CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA has correct href"""
        primary_cta = icon_tab_multiple_ways_to_play.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, \
            f"Icon Tab (Multiple Ways to Play) primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA opens new tab"""
        primary_cta = icon_tab_multiple_ways_to_play.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Icon Tab (Multiple Ways to Play) primary CTA target should be '{expected_target}', got '{target}'"
    
    
    # Carousels tests

    def test_carousel_exists(self, icon_tab_multiple_ways_to_play):
        """Verify carousel exists"""
        assert icon_tab_multiple_ways_to_play.has_carousel(), "Icon Tab (Multiple Ways to Play) should have carousel"
    
    def test_carousel_has_three_slides(self, icon_tab_multiple_ways_to_play):
        """Verify carousel has exactly 3 slides"""
        slide_count = icon_tab_multiple_ways_to_play.get_slide_count()
        expected_slide_count = 3
        
        assert slide_count == expected_slide_count, \
            f"Icon Tab (Multiple Ways to Play) carousel should have '{expected_slide_count}' slides, found '{slide_count}'"
    
    def test_all_tabs_have_labels(self, icon_tab_multiple_ways_to_play):
        """Verify each tab has a valid label"""
        labels = icon_tab_multiple_ways_to_play.get_tab_labels()
        
        for i, label in enumerate(labels):
    
            assert label.strip(), \
                f"Icon Tab (Multiple Ways to Play) carousel tab {i} label should not be empty or whitespace"
    
    def test_tab_labels_are_correct(self, icon_tab_multiple_ways_to_play):
        """Verify each tab has the expected label"""
        labels = icon_tab_multiple_ways_to_play.get_tab_labels()
        expected_labels = ["SUMMONER'S RIFT", "ARAM", "TEAMFIGHT TACTICS"]

        for i, label in enumerate(labels):
    
            assert label == expected_labels[i], \
                f"Icon Tab (Multiple Ways to Play) carousel tab {i}'s label should be '{expected_labels[i]}', got '{label}'"

    def test_tabs_have_images_displayed(self, icon_tab_multiple_ways_to_play):
        """Verify each tab has an image displayed"""
        slides = icon_tab_multiple_ways_to_play.get_all_slides()
    
        for i, slide in enumerate(slides):
            # Each slide contains an img element
            try:
                img = slide.find_element("tag name", "img")
                assert img is not None, f"Icon Tab (Multiple Ways to Play) carousel tab {i} should have an image"
                assert img.is_displayed(), f"Icon Tab (Multiple Ways to Play) carousel tab {i} image should be visible"
            except:
                pytest.fail(f"Tab {i} does not have an image element")


    # Tab interaction & media tests

    def test_media_section_has_media_element(self, icon_tab_multiple_ways_to_play):
        """Verify media section has media element"""
        assert icon_tab_multiple_ways_to_play.has_media_element(), \
            "Icon Tab (Multiple Ways to Play) media section should have media element"
    
    def test_initial_media_element_is_displayed(self, icon_tab_multiple_ways_to_play):
        """Verify initial media element is displayed"""
        assert icon_tab_multiple_ways_to_play.is_visible(), \
            "Icon Tab (Multiple Ways to Play) initial media element should be visible"
        
    def test_initial_media_title(self, icon_tab_multiple_ways_to_play):
        """Verify initial media title is displayed"""
        title_text = icon_tab_multiple_ways_to_play.get_media_title_text()
        expected_title = "THE MOST POPULAR GAME MODE"

        assert title_text == expected_title, \
            f"Icon Tab (Multiple Ways to Play) initial media title should be '{expected_title}', got '{title_text}'"

    def test_initial_media_description_has_text(self, icon_tab_multiple_ways_to_play):
        """Verify initial media description is displayed"""
        description_text = icon_tab_multiple_ways_to_play.get_media_description_text()
        assert description_text is not None, \
            "Icon Tab (Multiple Ways to Play) initial media description should exist"
        assert description_text.strip(), \
            "Icon Tab (Multiple Ways to Play) initial media description should have non-whitespace text"

    def test_clicking_tab_changes_media_title_and_subtitle(self, icon_tab_multiple_ways_to_play):
        """Verify title & subtitle change"""
        index = 2
        previous_title = icon_tab_multiple_ways_to_play.get_media_title_text()
        previous_description= icon_tab_multiple_ways_to_play.get_media_description_text()
        icon_tab_multiple_ways_to_play.click_tab_by_index(index)

        assert icon_tab_multiple_ways_to_play.verify_media_changed(previous_title, previous_description), \
            "Icon Tab (Multiple Ways to Play) media title and description should change after clicking different tab"


