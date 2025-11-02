# Sauce Demo Test Automation

Automated test suite for Sauce Demo e-commerce site using Python, Selenium, and Pytest with Page Object Model design pattern.

## Project Structure
```
saucedemo_pom/
├── pages/             # Page Object Model classes
├── tests/             # Test files
│   ├── test_checkout_details_verification.py
│   ├── test_order_confirmation.py
│   └── test_order_cancel.py
├── reports/           # Test execution reports
├── conftest.py       # Pytest fixtures and configurations
└── test_suite.py     # Test suite runner
```

## Prerequisites

- Python 3.8 or higher
- Chrome browser
- ChromeDriver matching your Chrome version

## Setup

1. Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```powershell
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run specific test file:
```powershell
pytest tests/test_checkout_details_verification.py
```

### Run with markers:
```powershell
pytest -m smoke  # Run smoke tests only
```

## Test Configuration

### Environment Variables

- `SKIP_CANCEL`: Skip order cancellation test
  ```powershell
  $env:SKIP_CANCEL=1; pytest tests/
  ```

### Test Fixtures

- `setup_driver`: Initializes WebDriver, performs login (function-scoped)
- `retry_on_failure`: Implements retry logic for flaky tests
- `test_products`: Provides test data for product selections

### Test Markers

- `@pytest.mark.dependency`: Manage test dependencies
- `@pytest.mark.order`: Control test execution order
- `@pytest.mark.flaky`: Handle flaky tests with retries
- `@pytest.mark.skipif`: Conditional test skipping
- `@pytest.mark.smoke`: Mark smoke tests

## Test Structure

1. Checkout Details Verification
   - Validates product addition and checkout process
   - Order: 1
   - Dependencies: None

2. Order Confirmation
   - Verifies successful order placement
   - Order: 2
   - Dependencies: Requires checkout verification

3. Order Cancellation
   - Tests order cancellation flow
   - Order: 3
   - Can be skipped via environment variable

## Page Objects

- `AddToCart`: Product addition functionality
- `GetCartItems`: Cart items retrieval
- `GoToCart`: Cart navigation
- `Checkout`: Checkout process
- `Login/Logout`: Authentication handling

## Reports

HTML reports are generated in the `reports` directory after test execution. Open `reports/report.html` in a browser to view results.

## Best Practices

1. Always use the provided fixtures for browser handling
2. Implement proper waits for element interactions
3. Use appropriate markers for test categorization
4. Follow Page Object Model pattern for maintainability

## Troubleshooting

1. ChromeDriver version mismatch:
   - Update ChromeDriver to match your Chrome browser version

2. Element not found errors:
   - Check if proper waits are implemented
   - Verify element locators are correct

3. Test dependencies failing:
   - Ensure tests are running in correct order
   - Check if dependent tests are passing

## Contributing

1. Follow existing code structure
2. Add appropriate markers and dependencies
3. Update README for new features
4. Include test reports in pull requests

Enjoy the project. 