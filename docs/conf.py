from datetime import datetime

extensions = ["myst_parser"]
source_suffix = ".md"
master_doc = "index"

project = "First Web Scraper"
year = datetime.now().year
copyright = f"{year} palewire"

exclude_patterns = ["_build"]

html_theme = "palewire"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
    ]
}
html_theme_options = {
    "canonical_url": f"https://palewi.re/docs/first-web-scraper/",
}
html_theme_options = {
    "nosidebar": True,
}

html_static_path = ["_static"]

pygments_style = "sphinx"
