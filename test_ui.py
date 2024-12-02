from playwright.sync_api import sync_playwright # type: ignore

def test_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:5000")  # Update with your app's URL

        # Test Compute Mean
        page.fill("textarea#value_box", "9\n6\n8\n5\n7")
        page.click("button#mean")
        assert page.locator("textarea#result_box").input_value() == "7"

        browser.close()
