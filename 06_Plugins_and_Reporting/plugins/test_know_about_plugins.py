"""
What Are Pytest Plugins?
Pytest plugins are modular extensions that hook into Pytest’s internal lifecycle. They can:

    Add new CLI options
    Modify test collection or execution
    Enhance reporting
    Provide custom fixtures
    Integrate with external tools (like coverage, HTML reports, CI systems)

Pytest uses a hook-based architecture powered by the pluggy library.
Plugins register functions to respond to specific events like test setup, teardown, or result reporting.

How Pytest Loads Plugins -->
Pytest discovers plugins in several ways:
    Method	                            Description
    Built-in	                        Comes with Pytest (e.g. assertion rewriting, test discovery)
    conftest.py	                        Local plugins scoped to a directory
    pytest_plugins variable	            Declares plugins to load in conftest.py or test modules
    -p plugin_name CLI option	        Explicitly loads a plugin
    entry_points in pyproject.toml	    Used for distributable plugins via PyPI

You can inspect active plugins with:
    pytest --trace-config

To disable a plugin:
    pytest -p no:plugin_name

Popular Plugins You Should Try
    Plugin	            Purpose	Install Command
    pytest-cov	        Code coverage reporting	pip install pytest-cov
    pytest-html	        Generates HTML reports	pip install pytest-html
    pytest-xdist	    Parallel test execution	pip install pytest-xdist
    pytest-mock	        Simplified mocking with mocker fixture	pip install pytest-mock
    pytest-clarity	    Improves assertion error readability	pip install pytest-clarity
    pytest-bdd	        Behavior-driven testing with Gherkin	pip install pytest-bdd
    pytest-randomly	    Randomizes test order to catch dependencies	pip install pytest-randomly


Useful Hooks You Can Implement
    Hook Name	                Purpose
    pytest_addoption	        Add custom CLI options
    pytest_configure	        Modify Pytest config before tests run
    pytest_runtest_setup	    Run logic before each test
    pytest_runtest_call	        Wrap test execution
    pytest_terminal_summary	    Customize final output

"""

