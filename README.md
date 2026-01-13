# League of Legends Homepage Test Automation
![Tests](https://github.com/PaulE202/leagueoflegends-automation/workflows/Automated%20Tests/badge.svg)

A comprehensive Selenium-based test automation framework for the League of Legends homepage, demonstrating Page Object Model architecture, component-based design, and professional QA automation practices.

## Project Overview

This framework provides automated UI testing for [leagueoflegends.com](https://www.leagueoflegends.com/en-us/), focusing on comprehensive coverage of homepage components (blades) including carousels, video players, interactive tabs, and call-to-action elements. Built as a portfolio project to demonstrate automation engineering skills for QA roles.

**Key Metrics:**
- **100+ automated tests** covering entire homepage
- **6 blade components** with dedicated test suites
- **Session-scoped fixtures** for efficient test execution
- **Automated screenshot capture** on test failures

## Technology Stack

- **Python 3.8+** - Core language
- **Selenium WebDriver** - Browser automation
- **pytest** - Test framework and runner
- **pytest-html** - HTML test reporting with screenshots
- **Firefox/geckodriver** - Primary browser (webdriver-manager for automatic driver setup)

## Architecture

### Page Object Model with Component-Based Design

```
├── pages/
│   ├── base_page.py          # Base page class (load timing, waits, banner dismissal)
│   └── home_page.py           # Homepage class (blade retrieval methods)
├── components/
│   ├── base_blade.py          # Base blade class (common blade functionality)
│   ├── game_simple_masthead_blade.py
│   ├── article_card_carousel_blade.py
│   ├── icon_tab_blade.py
│   ├── media_promo_blade.py
│   └── centered_promotion_blade.py
└── tests/
    ├── conftest.py            # Fixtures and configuration
    ├── test_homepage_game_simple_masthead.py
    ├── test_homepage_article_card_carousel.py
    ├── test_homepage_icon_tab_choose_champion.py
    ├── test_homepage_icon_tab_multiple_ways_to_play.py
    ├── test_homepage_media_promo.py
    └── test_homepage_centered_promotion.py
```

**Design Philosophy:**
- **Separation of concerns** - Page objects handle structure, components handle blade-specific logic
- **Reusability** - Blade components can be used across multiple pages
- **Maintainability** - Changes to blade implementation don't affect test code
- **DRY principle** - Common functionality elevated to base classes

## Key Design Decisions

### 1. Unstripped Text Validation
**Decision:** Getter methods return unstripped text to catch UI quality issues.

```python
def get_title(self):
    """Get main title"""
    try:
        element = self.find_element_in_blade((By.CSS_SELECTOR, "[data-testid='title']"))
        return element.text if element.text.strip() else None  # Check stripped, return unstripped
    except NoSuchElementException:
        return None
```

**Rationale:** Extra whitespace in titles/CTAs indicates poor content quality. Tests should catch `"  TITLE  "` vs `"TITLE"` to identify sloppy HTML/content rather than just semantic correctness. The method checks if text exists (using .strip()), but returns the unstripped version to preserve whitespace for validation.

**Trade-off:** Less robust tests, but catches issues users would see.

### 2. Sampling vs Exhaustive Testing
**Approach:** Test 2-3 representative items from carousels/tabs rather than all items.

**Rationale:**
- Items use same implementation pattern
- Reduces maintenance when content changes
- Focused validation over exhaustive checking
- Sufficient to catch implementation bugs

**Example:**
```python
def test_clicking_tab_changes_media_title_and_subtitle(self, icon_tab_choose_champion):
    """Verify title and subtitle change when clicking different tab"""
    tab_index = 2
    previous_title = icon_tab_choose_champion.get_media_title_text()
    previous_subtitle = icon_tab_choose_champion.get_media_subtitle_text()

    icon_tab_choose_champion.click_tab_by_index(tab_index)

    current_title = icon_tab_choose_champion.get_media_title_text()
    current_subtitle = icon_tab_choose_champion.get_media_subtitle_text()

    assert current_title != previous_title, "Media title should change"
    assert current_subtitle != previous_subtitle, "Media subtitle should change"
```

### 3. Multi-Dimensional Validation
**Principle:** Check multiple aspects of correctness, not just one.

**For Interactive Elements:**
- Visibility (users must see to interact)
- Text content validation
- Link href validation
- Target attribute validation

**For Media Elements:**
- Visibility check
- Source validation (src exists and non-empty)
- Attribute validation (autoplay, muted, loop)

**Example:**
```python
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
```

### 4. Session-Scoped Fixtures
**Strategy:**
- **Session-scoped browser** - One browser instance for entire test run
- **Session-scoped homepage** - Single page load shared by all tests
- Tests are read-only (no state changes)

**Benefits:**
- Dramatically faster test execution (20+ seconds → 3-5 seconds)
- Reduced browser overhead
- Suitable for read-only testing

**Trade-off:** Tests must not modify page state (appropriate for this project's scope).

## Features

### Test Coverage
- ✅ **Masthead blade** - Logo, description, background video, CTAs
- ✅ **Article carousel** - Title, background, multiple slides, CTAs, navigation controls
- ✅ **Icon tabs (2 variants)** - Title, description, background, CTAs, tab switching, media changes, content validation
- ✅ **Media promo** - Title, supertitle, description, background, CTAs, content validation
- ✅ **Centered promotion** - Video validation, CTAs

### Test Reporting & Debugging

**HTML Test Reports:**
```bash
pytest --html=reports/report.html --self-contained-html
```

**Automatic Screenshot Capture on Failure:**
- Screenshots saved to `screenshots/` directory
- Automatically scrolls to relevant blade before capture
- Screenshots embedded in HTML reports
- Filenames include test name and timestamp

**Screenshot naming convention:**
```
screenshots/test_[file]_[class]_[test_name]_YYYYMMDD_HHMMSS.png
```

### Validation Strategy

**Text Content:**
- Exact text matching for critical elements (titles, CTAs)
- Presence validation for descriptions
- Unstripped text to catch whitespace issues

**Links:**
- href validation (not empty, proper format)
- target attribute validation (new tab vs same tab)
- No actual clicking of external links (third-party sites)

**Media Elements:**
- Visibility validation
- Source attribute validation (exists and non-empty)
- Multiple source strategies (primary + fallback selectors)

## Installation

### Prerequisites
- Python 3.8 or higher
- Firefox browser (Chrome/Edge supported via command-line option)
- Git

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/leagueoflegends-automation.git
cd leagueoflegends-automation
```

2. **Create virtual environment:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

**Note:** geckodriver installs automatically via webdriver-manager on first run.

## Usage

### Run All Tests
```bash
pytest tests/
```

### Run Specific Blade Tests
```bash
# Masthead tests
pytest tests/test_homepage_game_simple_masthead.py

# Article carousel tests
pytest tests/test_homepage_article_card_carousel.py

# Icon tab tests
pytest tests/test_homepage_icon_tab_choose_champion.py
pytest tests/test_homepage_icon_tab_multiple_ways_to_play.py

# Media promo tests
pytest tests/test_homepage_media_promo.py

# Centered promotion tests
pytest tests/test_homepage_centered_promotion.py
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Command-Line Options
```bash
# Run in headless mode
pytest --headless

# Use different browser
pytest --browser=edge

# Verbose output
pytest -v

# Run specific test
pytest tests/test_homepage_game_simple_masthead.py::TestGameSimpleMasthead::test_h1_title_text
```

## Test Examples

### Simple Validation Test
```python
def test_h1_title_text(self, masthead):
    """Verify title has expected text"""
    h1_text = masthead.get_h1_title()
    expected_text = "LEAGUE OF LEGENDS — A 5V5 MOBA WHERE TEAMS BATTLE TO DESTROY THE ENEMY NEXUS"
        
    assert h1_text == expected_text, f"Title should be '{expected_text}', got '{h1_text}'"
```

### Multi-Dimensional Validation Test
```python
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
```

### Interactive Element Test
```python
def test_clicking_tab_changes_media_title_and_subtitle(self, icon_tab_choose_champion):
    """Verify title and subtitle change when clicking different tab"""
    tab_index = 2

    previous_title = icon_tab_choose_champion.get_media_title_text()
    previous_subtitle = icon_tab_choose_champion.get_media_subtitle_text()
    
    icon_tab_choose_champion.click_tab_by_index(tab_index)
    
    current_title = icon_tab_choose_champion.get_media_title_text()
    current_subtitle = icon_tab_choose_champion.get_media_subtitle_text()
    
    assert current_title != previous_title, "Media title should change"
    assert current_subtitle != previous_subtitle, "Media subtitle should change"
```

## Project Scope & Limitations

### Deliberate Scope Decisions

**Homepage Only:**
- Focused scope on homepage for ROI (representative complexity, major patterns)
- Framework extensible to other pages when needed
- Page Object Model supports easy addition of new pages

**Read-Only Testing:**
- No form submissions, account creation, or state-changing operations
- Validates visual elements, links, content
- Appropriate scope for testing third-party production site

**Multi-Browser Support:**
- Firefox and Edge browsers supported via `--browser` flag
- Example: `pytest --browser=edge`
- Headless mode available: `pytest --headless`
- Framework architecture supports additional browsers via Selenium abstraction

**Manual Execution:**
- Tests run on-demand rather than on schedule
- User controls when to check
- Appropriate for portfolio/development use

### Known Limitations

- Content-dependent tests may need updates when site content changes
- Third-party site testing (no control over site changes)
- CSS selectors may break with site redesigns
- No performance testing or load testing
- No API testing (UI layer only)

## Development Practices

### Code Quality
- **Consistent naming** - Verb-first docstrings, clear method names
- **DRY principle** - Shared functionality in base classes
- **Clear error messages** - Context-rich assertion messages
- **Proper waits** - Explicit waits for element states, time.sleep() only for scroll animations

### Test Independence
- Tests don't depend on execution order
- Session-scoped fixtures ensure consistent state
- Tests are read-only (no state modification)

### Maintainability
- Component-based architecture isolates changes
- Clear separation: locators → blade methods → tests
- Descriptive test names match method being called

## Future Enhancements

Potential additions for continued development:

- ✅ CI/CD integration (GitHub Actions)
- [ ] Additional page coverage (Champions, News, Esports)
- [ ] Cross-browser testing (Chrome, Safari)
- [ ] Responsive testing (desktop, tablet, mobile viewports)
- [ ] Visual regression testing (Percy, Applitools)
- [ ] Performance metrics collection
- [ ] Parallel test execution (pytest-xdist)
- [ ] Allure reporting integration

## Project Context

**Author:** Paul Egyed  
**Technologies:** Selenium, pytest, Page Object Model, Python, GitHub Actions

This project demonstrates:
- ✅ Framework architecture and design
- ✅ Page Object Model implementation
- ✅ pytest fixture strategies
- ✅ Selenium best practices
- ✅ Test organization and maintainability
- ✅ Professional QA automation skills
- ✅ CI/CD integration (GitHub Actions)


## Contributing

This is a portfolio project and is not actively seeking contributions. However, feel free to fork and adapt for your own learning purposes.

## License

This project is for educational and portfolio purposes. League of Legends and related trademarks are property of Riot Games.

---

**Contact:** GitHub [PaulE202]