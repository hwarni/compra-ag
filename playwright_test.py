from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chrome.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        page.screenshot(path="example.png")
        browser.close()

if __name__ == "__main__":
    run()
    