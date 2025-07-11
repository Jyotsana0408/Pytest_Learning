"""
Why Reporting Matters :

    Visibility: Helps you and your team understand what passed, failed, or was skipped.
    Debugging: Offers detailed tracebacks and logs for failed tests.
    Documentation: Creates a historical record of test runs.
    Stakeholder Communication: Shareable reports for non-technical teammates or managers.

Built-in Reporting Options
Pytest gives you several CLI flags to control output:

    Option	                Purpose
    -v, -vv	                Increase verbosity (more detailed output)
    `--tb=short	   long`	Control traceback format
    --maxfail=1	            Stop after N failures
    --junitxml=report.xml	Generate XML report (CI-friendly)

Built-in Reporting

    Pytest provides basic terminal output and supports:

    JUnit XML: --junitxml=report.xml
    Custom hooks: pytest_terminal_summary, record_property

HTML Reports with pytest-html

    pytest --html=report.html --self-contained-html

    Generates a standalone HTML file
    Includes pass/fail status, logs, and metadata
    Great for sharing with non-technical stakeholders

Allure Reports

    Allure provides rich, interactive dashboards:
        pip install allure-pytest
        pytest --alluredir=allure-results
        allure serve allure-results

    Shows test steps, attachments, timelines, severity levels
    Integrates with CI/CD tools like GitHub Actions and Jenkins
    Supports metadata like @allure.title, @allure.description, @allure.severity

JUnit XML for CI Integration

    pytest --junitxml=report.xml

    Compatible with Jenkins, GitLab CI, Azure DevOps
    Can be customized with record_xml_property and record_testsuite_property

Coverage Reports with pytest-cov

    pytest --cov=my_module --cov-report=html

    Generates HTML or XML coverage reports
    Shows which lines were missed
    Can be configured via .coveragerc

Best Practices for Reporting
    Use pytest-html for quick sharing
    Use pytest-cov to track test completeness
    Use allure-pytest for rich CI dashboards
    Automate report generation in CI pipelines
    Customize verbosity with -v, -vv, --tb=short|long|no
"""