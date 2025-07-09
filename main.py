"""
Pytest Learning Series - Overview

Pytest is a powerful and flexible testing framework for Python
that makes writing and running tests both simple and scalable

What Pytest Is --->
A tool for writing test cases in Python using plain assert statements.
Supports everything from basic unit tests to complex functional testing.
Automatically discovers test files and functions based on naming conventions.
Offers detailed failure reports, making debugging easier.

Real-World Use Cases --->
Testing APIs, databases, and UI workflows
Automating regression and smoke tests
Integrating with CI/CD pipelines like GitHub Actions or Jenkins
Generating HTML or JUnit reports for test results

This series covers:
 Setting up Pytest in a virtual environment
 Writing your first test functions using `assert`
 Parametrized testing for multiple input scenarios
 Using print statements inside tests with `-s` flag
 Organizing test files and naming conventions
 Understanding Pytest CLI commands (-v, -k, --maxfail, etc.)
 Ignoring unnecessary files with .gitignore
 Monkeypatching for mocking functions and environment variables
 Using plugins for coverage, mocking, parallel testing, and HTML reports
 Generating test reports (HTML, JUnit, JSON) for CI/CD pipelines
 Structuring tests with classes, markers, and fixtures
 Integrating Pytest with CI/CD tools like GitHub Actions, Jenkins, and GitLab

"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Learners')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
