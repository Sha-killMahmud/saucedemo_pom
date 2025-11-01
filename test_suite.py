import os
import pytest

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

pytest.main([

    "tests/test_order_confirmation.py",
    "tests/test_order_cancel.py",
    "tests/test_checkout_details_verification.py",
    #"-m", "smoke",
    "--html=reports/report.html",
    "--self-contained-html"
])