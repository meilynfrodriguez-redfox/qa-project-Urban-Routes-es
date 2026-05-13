# Urban Routes Automation Project

## Description
This project contains automated UI tests for the Urban Routes application using Selenium WebDriver, Pytest, and Python.

The project validates different user scenarios independently, including:
- Setting the route
- Selecting the Comfort tariff
- Adding a phone number
- Confirming the verification code
- Adding a payment card
- Sending a message to the driver
- Ordering a blanket and tissues
- Adding two ice creams
- Confirming the driver search modal

The project follows the Page Object Model (POM) design pattern to improve code organization and maintainability.

## Technologies and Techniques Used
- Python
- Selenium WebDriver
- PyCharm
- Pytest
- Page Object Model (POM)
- Automated UI Testing

## How to Run the Tests

1. Open the project in PyCharm.

2. Install the required packages:

```bash
pip install selenium
pip install pytest
```

3. Run the tests using PyCharm or pytest.

## Project Structure
- `data.py` → test data
- `helpers.py` → helper functions
- `pages.py` → page methods and locators
- `main.py` → automated tests
- `README.md` → project documentation