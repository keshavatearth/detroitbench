"""Build the same navigation, typography and theme controls into every page."""
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "site"
THEME_INIT = """<script data-site-theme-init>try{document.documentElement.dataset.theme=localStorage.getItem('db-theme')==='dark'?'dark':'light';}catch(error){document.documentElement.dataset.theme='light';}</script>"""


def render_shell(page: str, *, section: str, skip_target: str) -> str:
    """Inline shared assets so downloaded diagrams remain self-contained."""
    replacements = {
        "<!--SITE_ICON-->": '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'%3E%3Ccircle cx=\'50\' cy=\'50\' r=\'35\' fill=\'none\' stroke=\'%23176caa\' stroke-width=\'14\'/%3E%3C/svg%3E">',
        "<!--SITE_THEME_INIT-->": THEME_INIT,
        "<!--SITE_STYLES-->": f'<style data-site-shared>\n{(SITE / "shared.css").read_text()}\n</style>',
        "<!--SITE_HEADER-->": (SITE / "shared.header.html").read_text(),
        "<!--SITE_SCRIPT-->": f'<script data-site-shared>\n{(SITE / "shared.js").read_text()}\n</script>',
        "<!--SITE_SKIP-->": f'<a class="site-skip" href="#{skip_target}">Skip to content</a>',
        "__SITE_SECTION__": section,
    }
    for marker, value in replacements.items():
        if page.count(marker) != 1:
            raise ValueError(f"Expected exactly one shared site marker: {marker}")
        page = page.replace(marker, value)
    # Full-screen flowcharts end with their own toolbar, so the footer is opt-in.
    footer_marker = "<!--SITE_FOOTER-->"
    if page.count(footer_marker) > 1:
        raise ValueError(f"Expected at most one shared site marker: {footer_marker}")
    return page.replace(footer_marker, (SITE / "shared.footer.html").read_text())
