import pytest
from pages.home_page import HomePage


class TestIconTabChooseChampion:
    """Tests for Icon Tab (Choose Champion) blade on Homepage"""

    @pytest.fixture(scope="session")
    def icon_tab_choose_champion(self, home_page):
        """Get Icon Tab (Choose Champion) once for all tests"""
        return home_page.get_icon_tab_choose_champion()

    # Structural tests
    
    def test_icon_tab_choose_champion_is_displayed(self, icon_tab_choose_champion):
        """Verify blade is displayed on page"""
        assert icon_tab_choose_champion.is_visible(), "Icon Tab (Choose Champion) should be visible"
    
    def test_backdrop_exists(self, icon_tab_choose_champion):
        """Verify blade has backdrop"""
        assert icon_tab_choose_champion.has_icon_tab_main_backdrop(), "Icon Tab (Choose Champion) should have backdrop"
    
    def test_backdrop_has_background(self, icon_tab_choose_champion):
        """Verify backdrop has background layer"""
        assert icon_tab_choose_champion.has_icon_tab_full_backdrop_background(), \
            "Icon Tab (Choose Champion) backdrop should have background layer"

    def test_main_section_exists(self, icon_tab_choose_champion):
        """Verify blade has main section"""
        assert icon_tab_choose_champion.has_main_section(), "Icon Tab (Choose Champion) should have main section"

    def test_media_section_exists(self, icon_tab_choose_champion):
        """Verify blade has media section"""
        assert icon_tab_choose_champion.has_media_section(), "Icon Tab (Choose Champion) should have media section"
    
    # Blade header tests

    def test_blade_header_exists(self, icon_tab_choose_champion):
        """Verify blade header exists"""
        assert icon_tab_choose_champion.has_blade_header(), "Icon Tab (Choose Champion) should have blade header"
    
    
    def test_supertitle_text(self, icon_tab_choose_champion):
        """Verify supertitle has expected text"""
        super_title_text = icon_tab_choose_champion.get_super_title()
        expected_supertitle_text = "CHOOSE YOUR"

        assert super_title_text == expected_supertitle_text, \
            f"Icon Tab (Choose Champion) supertitle should be '{expected_supertitle_text}', got '{super_title_text}'"

    def test_title_text(self, icon_tab_choose_champion):
        """Verify title has expected text"""
        title_text = icon_tab_choose_champion.get_title()
        expected_title = "CHAMPION"

        assert title_text == expected_title, f"Icon Tab (Choose Champion) title should be '{expected_title}', got '{title_text}'"

    def test_description_has_text(self, icon_tab_choose_champion):
        """Verify description is displayed"""
        description_text = icon_tab_choose_champion.get_description()
        assert description_text is not None, "Icon Tab (Choose Champion) description should exist"
        assert len(description_text) > 0, "Icon Tab (Choose Champion) description should have text"

    # CTA tests
    
    def test_header_links_exists(self, icon_tab_choose_champion):
        """Verify header links exist"""
        assert icon_tab_choose_champion.has_header_links(), "Icon Tab (Choose Champion) should have header links section"
    
    def test_primary_cta_is_displayed(self, icon_tab_choose_champion):
        """Verify primary CTA is displayed"""
        assert icon_tab_choose_champion.has_primary_cta(), "Icon Tab (Choose Champion) should have primary CTA"
    
    def test_primary_cta_text(self, icon_tab_choose_champion):
        """Verify primary CTA has correct text"""
        primary_cta_text = icon_tab_choose_champion.get_primary_cta_text()
        expected_primary_cta_text = "DISCOVER MORE CHAMPIONS"
        
        assert primary_cta_text == expected_primary_cta_text, \
            f"Icon Tab (Choose Champion) primary CTA should contain '{expected_primary_cta_text}', got '{primary_cta_text}'"
    
    def test_primary_cta_href(self, icon_tab_choose_champion):
        """Verify primary CTA has correct href"""
        primary_cta = icon_tab_choose_champion.get_primary_cta_element()
        href = primary_cta.get_attribute("href")
        expected_href = "https://www.leagueoflegends.com/en-us/champions/"
        
        assert href == expected_href, \
            f"Icon Tab (Choose Champion) primary CTA href should be '{expected_href}', got '{href}'"
    
    def test_primary_cta_opens_new_tab(self, icon_tab_choose_champion):
        """Verify primary CTA opens new tab"""
        primary_cta = icon_tab_choose_champion.get_primary_cta_element()
        target = primary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Icon Tab (Choose Champion) primary CTA target should be '{expected_target}', got '{target}'"
    
    def test_secondary_cta_is_displayed(self, icon_tab_choose_champion):
        """Verify secondary CTA is displayed"""
        assert icon_tab_choose_champion.has_secondary_cta(), \
            "Icon Tab (Choose Champion) should have secondary CTA"
    
    def test_secondary_cta_text(self, icon_tab_choose_champion):
        """Verify secondary CTA has correct text"""
        secondary_cta_text = icon_tab_choose_champion.get_secondary_cta_text()
        expected_secondary_cta_text = "PLAY NOW"
        
        assert secondary_cta_text == expected_secondary_cta_text, \
            f"Icon Tab (Choose Champion) secondary CTA should contain '{expected_secondary_cta_text}', got '{secondary_cta_text}'"
    
    def test_secondary_cta_href(self, icon_tab_choose_champion):
        """Verify secondary CTA has correct href"""
        secondary_cta = icon_tab_choose_champion.get_secondary_cta_element()
        href = secondary_cta.get_attribute("href")
        expected_href = "https://signup.leagueoflegends.com/"
        
        assert href == expected_href, \
            f"Icon Tab (Choose Champion) secondary CTA href should be '{expected_href}', got '{href}'"
    
    def test_secondary_cta_opens_new_tab(self, icon_tab_choose_champion):
        """Verify secondary CTA opens new tab"""
        secondary_cta = icon_tab_choose_champion.get_secondary_cta_element()
        target = secondary_cta.get_attribute("target")
        expected_target = "_blank"
        
        assert target == expected_target, \
            f"Icon Tab (Choose Champion) secondary CTA target should be '{expected_target}', got '{target}'"
    
    # Carousels tests

    def test_carousel_exists(self, icon_tab_choose_champion):
        """Verify carousel exists"""
        assert icon_tab_choose_champion.has_carousel(), "Icon Tab (Choose Champion) should have carousel"
    
    def test_carousel_has_six_slides(self, icon_tab_choose_champion):
        """Verify carousel has exactly 6 slides"""
        slide_count = icon_tab_choose_champion.get_slide_count()
        expected_slide_count = 6
        
        assert slide_count == expected_slide_count, \
            f"Icon Tab (Choose Champion) carousel should have '{expected_slide_count}' slides, found '{slide_count}'"
    
    def test_all_tabs_have_labels(self, icon_tab_choose_champion):
        """Verify each tab has a valid label"""
        labels = icon_tab_choose_champion.get_tab_labels()
        
        for i, label in enumerate(labels):
    
            assert label.strip(), \
                f"Icon Tab (Choose Champion) carousel tab {i} label should not be empty or whitespace"
    
    def test_tab_labels_are_correct(self, icon_tab_choose_champion):
        """Verify each tab has the expected label"""
        labels = icon_tab_choose_champion.get_tab_labels()
        expected_labels = ["ASSASSINS", "FIGHTERS", "MAGES", "MARKSMEN", "SUPPORTS", "TANKS"]

        for i, label in enumerate(labels):
    
            assert label == expected_labels[i], \
                f"Icon Tab (Choose Champion) carousel tab {i}'s label should be '{expected_labels[i]}', got '{label}'"

    def test_tabs_have_images_displayed(self, icon_tab_choose_champion):
        """Verify each tab has an image displayed"""
        slides = icon_tab_choose_champion.get_all_slides()
    
        for i, slide in enumerate(slides):
            # Each slide contains an img element
            try:
                img = slide.find_element("tag name", "img")
                assert img is not None, f"Icon Tab (Choose Champion) carousel tab {i} should have an image"
                assert img.is_displayed(), f"Icon Tab (Choose Champion) carousel tab {i} image should be visible"
            except:
                pytest.fail(f"Tab {i} does not have an image element")


    # Tab interaction & media tests

    def test_media_section_has_media_element(self, icon_tab_choose_champion):
        """Verify media section has media element"""
        assert icon_tab_choose_champion.has_media_element(), \
            "Icon Tab (Choose Champion) media section should have media element"
    
    def test_initial_media_title(self, icon_tab_choose_champion):
        """Verify initial media title is displayed"""
        title_text = icon_tab_choose_champion.get_media_title_text()
        expected_title = "AKALI"

        assert title_text == expected_title, \
            f"Icon Tab (Choose Champion) initial media title should be '{expected_title}', got '{title_text}'"

    def test_initial_media_subtitle(self, icon_tab_choose_champion):
        """Verify initial media title is displayed"""
        subtitle_text = icon_tab_choose_champion.get_media_subtitle_text()
        expected_subtitle = "The Rogue Assassin"

        assert subtitle_text == expected_subtitle, \
            f"Icon Tab (Choose Champion) initial media subtitle should be '{expected_subtitle}', got '{subtitle_text}'"

    def test_clicking_tab_changes_media_title_and_subtitle(self, icon_tab_choose_champion):
        """Verify title & subtitle change"""
        index = 2
        previous_title = icon_tab_choose_champion.get_media_title_text()
        previous_subtitle = icon_tab_choose_champion.get_media_subtitle_text()
        icon_tab_choose_champion.click_tab_by_index(index)

        assert icon_tab_choose_champion.verify_media_changed(previous_title, previous_subtitle), \
            "Icon Tab (Choose Champion) media title and subtitle should change after clicking different tab"


