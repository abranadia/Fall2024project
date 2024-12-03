from playwright.sync_api import sync_playwright
import time

def test_calculator():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=True to run tests without opening a browser
        page = browser.new_page()

        # Navigate to the Flask app (running locally)
        page.goto("http://127.0.0.1:5000")

        # Select an operation (e.g., Compute Mean)
        page.select_option("select#operation", "mean")

        # Input values
        page.fill("textarea#values", "9\n6\n8\n5\n7")

        # Click the Compute button
        page.click("button[type='submit']")

        # Wait for the result to appear
        time.sleep(1)  # Adjust the sleep time if necessary

        # Check that the result is correct (Mean = 35 / 5 = 7)
        result = page.inner_text("#result")
        
        # Adjusted the assertion to check for both integer and float result formats
        assert "Result: 7" in result or "Result: 7.0" in result, f"Expected 'Result: 7' or 'Result: 7.0' but got {result}"

        # Clear the inputs and results
        page.click("button#clear-button")
        
        # Validate that the input and result are cleared
        assert page.input_value("textarea#values") == "", "Values textarea was not cleared"
        assert page.inner_text("#result") == "", "Result was not cleared"

        # Close the browser
        browser.close()

