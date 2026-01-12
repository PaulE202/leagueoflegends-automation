import pytest
from pages.home_page import HomePage


class TestIconTabMultipleWaysToPlay:
    """Tests for Icon Tab (Multiple Ways to Play) blade on the Homepage"""

    @pytest.fixture(scope="session")
    def icon_tab_multiple_ways_to_play(self, home_page):
        """Get blade once for all tests"""
        return home_page.get_icon_tab_multiple_ways()

    # Structural tests
    
    def test_icon_tab_multiple_ways_to_play_is_visible(self, icon_tab_multiple_ways_to_play):
        """Verify blade is visible on page"""
        assert icon_tab_multiple_ways_to_play.is_visible(), "Blade should be visible"
    
    def test_backdrop_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has backdrop"""
        assert icon_tab_multiple_ways_to_play.has_icon_tab_main_backdrop(), "Blade should have backdrop"
    
    def test_backdrop_has_background(self, icon_tab_multiple_ways_to_play):
        """Verify backdrop has background layer"""
        assert icon_tab_multiple_ways_to_play.has_icon_tab_full_backdrop_background(), \
            "Blade backdrop should have background layer"

    def test_main_section_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has main section"""
        assert icon_tab_multiple_ways_to_play.has_main_section(), "Blade should have main section"

    def test_media_section_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade has media section"""
        assert icon_tab_multiple_ways_to_play.has_media_section(), "Blade should have media section"
    
    # Blade header tests

    def test_blade_header_exists(self, icon_tab_multiple_ways_to_play):
        """Verify blade header exists"""
        assert icon_tab_multiple_ways_to_play.has_blade_header(), "Blade should have blade header"
    
    def test_supertitle_text(self, icon_tab_multiple_ways_to_play):
        """Verify supertitle has expected text"""
        super_title_text = icon_tab_multiple_ways_to_play.get_super_title()
        expected_supertitle_text = "MULTIPLE WAYS TO"

        assert super_title_text == expected_supertitle_text, \
            f"Blade supertitle should be '{expected_supertitle_text}', got '{super_title_text}'"

    def test_title_text(self, icon_tab_multiple_ways_to_play):
        """Verify title has expected text"""
        title_text = icon_tab_multiple_ways_to_play.get_title()
        expected_title = "PLAY"

        assert title_text == expected_title, f"Blade title should be '{expected_title}', got '{title_text}'"

    def test_description_has_text(self, icon_tab_multiple_ways_to_play):
        """Verify description has text"""
        description_text = icon_tab_multiple_ways_to_play.get_description()
        assert description_text is not None, "Blade description should have text"

    # CTA tests
    
    
    def test_header_links_exists(self, icon_tab_multiple_ways_to_play):
        """Verify header links exists"""
        assert icon_tab_multiple_ways_to_play.has_header_links(), "Blade should have header links section"

    def test_primary_cta_is_visible(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA is visible"""
        assert icon_tab_multiple_ways_to_play.is_primary_cta_visible(), "Blade primary CTA should be visible"
    
    def test_primary_cta_text(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA has correct text"""
        primary_cta_text = icon_tab_multiple_ways_to_play.get_primary_cta_text()
        expected_primary_cta_text = "PLAY NOW"
        
        assert primary_cta_text == expected_primary_cta_text, \
            f"Blade primary CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA has correct href"""
        primary_cta = icon_tab_multiple_ways_to_play.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, \
            f"Blade primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, icon_tab_multiple_ways_to_play):
        """Verify primary CTA opens new tab"""
        primary_cta = icon_tab_multiple_ways_to_play.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Blade primary CTA target should be '{expected_target}', got '{target}'"
    
    
    # Carousels tests

    def test_carousel_exists(self, icon_tab_multiple_ways_to_play):
        """Verify carousel exists"""
        assert icon_tab_multiple_ways_to_play.has_carousel(), "Blade should have carousel"
    
    def test_carousel_has_three_tabs(self, icon_tab_multiple_ways_to_play):
        """Verify carousel has exactly 3 tabs"""
        tab_count = icon_tab_multiple_ways_to_play.get_slide_count()
        expected_tab_count = 3
        
        assert tab_count == expected_tab_count, \
            f"Blade carousel should have '{expected_tab_count}' tabs, found '{tab_count}'"
    
    def test_tab_labels_are_correct(self, icon_tab_multiple_ways_to_play):
        """Verify tab labels have correct text"""
        labels = icon_tab_multiple_ways_to_play.get_tab_labels()
        expected_labels = ["SUMMONER'S RIFT", "ARAM", "TEAMFIGHT TACTICS"]

        # Prevent silent pass
        assert len(labels) == len(expected_labels), \
            f"Blade carousel should have {len(expected_labels)} labels, found {len(labels)}"

        for i, label in enumerate(labels):
    
            assert label == expected_labels[i], \
                f"Tab {i}'s label should be '{expected_labels[i]}', got '{label}'"

    def test_tabs_have_images_displayed(self, icon_tab_multiple_ways_to_play):
        """Verify each tab has an image displayed"""
        tabs = icon_tab_multiple_ways_to_play.get_all_slides()

        # Prevent silent pass
        assert tabs, "Blade carousel should have tabs"
    
        for i, tab in enumerate(tabs):
            try:
                img = tab.find_element("tag name", "img")
                assert img is not None, f"Tab {i} should have an image"
                assert img.is_displayed(), f"Tab {i} image should be displayed"
            except:
                pytest.fail(f"Tab {i} does not have an image element")


    # Tab interaction & media tests

    def test_media_section_has_media_element(self, icon_tab_multiple_ways_to_play):
        """Verify media section has media element"""
        assert icon_tab_multiple_ways_to_play.has_media_element(), \
            "Blade media section should have media element"
    
    def test_initial_media_element_is_visible(self, icon_tab_multiple_ways_to_play):
        """Verify initial media element is visible"""
        assert icon_tab_multiple_ways_to_play.is_media_element_visible(), \
            "Blade initial media element should be visible"
   
    def test_initial_media_title(self, icon_tab_multiple_ways_to_play):
        """Verify initial media title is correct"""
        title_text = icon_tab_multiple_ways_to_play.get_media_title_text()
        expected_title = "THE MOST POPULAR GAME MODE"

        assert title_text == expected_title, \
            f"Blade initial media title should be '{expected_title}', got '{title_text}'"

    def test_initial_media_description_has_text(self, icon_tab_multiple_ways_to_play):
        """Verify initial media description is correct"""
        description_text = icon_tab_multiple_ways_to_play.get_media_description_text()

        assert description_text is not None, \
            "Blade initial media description should exist"
        assert description_text.strip(), \
            "Blade initial media description should have non-whitespace text"

    def test_clicking_tab_changes_media_title_and_description(self, icon_tab_multiple_ways_to_play):
        """Verify title and description change when clicking different tab"""
        tab_index = 2

        previous_title = icon_tab_multiple_ways_to_play.get_media_title_text()
        previous_description = icon_tab_multiple_ways_to_play.get_media_description_text()
    
        icon_tab_multiple_ways_to_play.click_tab_by_index(tab_index)
    
        current_title = icon_tab_multiple_ways_to_play.get_media_title_text()
        current_description = icon_tab_multiple_ways_to_play.get_media_description_text()
    
        assert current_title != previous_title, "Media title should change"
        assert current_description != previous_description, "Media description should change"


