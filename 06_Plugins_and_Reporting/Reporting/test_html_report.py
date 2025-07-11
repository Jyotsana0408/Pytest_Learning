"""
HTML Reports with pytest-html
    Setup
    pip install pytest-html

Generate Report
    pytest --html=report.html --self-contained-html
        1. --html=report.html - creates an HTML report file.
        2. --self-contained-html - ensures it includes all styles and media in one file (no external dependencies).

    Creates a standalone HTML file.
    Includes pass/fail status, logs, and environment info.
    Great for sharing or archiving test results.

"""

# Generate HTML Report
# Use this command:
# pytest test_html_report.py --html=report.html --self-contained-html

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 10 - 4 == 6