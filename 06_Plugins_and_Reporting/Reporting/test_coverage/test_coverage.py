"""
pytest-cov is a powerful plugin that integrates code coverage analysis into your Pytest workflow.
It helps you measure how much of your code is actually being tested

What Is pytest-cov?

    It’s a Pytest plugin that wraps around the coverage.py tool.
    Tracks which lines of code were executed during tests.
    Highlights untested code, helping you improve coverage.
    Generates reports in terminal, HTML, XML, or annotated source formats.

Installation
    pip install pytest-cov

Measure single module:
        pytest --cov=module1

Generate HTML Report

    pytest --cov=module_name --cov-report=html
        This creates a folder htmlcov/ with a detailed visual report.
        Open htmlcov/index.html in your browser to explore coverage line-by-line.

    Other Report Formats
        Format	        Command	                Output File
        Terminal	    --cov-report=term	    Console summary
        HTML	        --cov-report=html	    htmlcov/index.html
        XML (for CI)	--cov-report=xml	    coverage.xml
        Annotated Src	--cov-report=annotate	.py,cover files

    You can combine reports:
        pytest --cov=math_ops --cov-report=term --cov-report=html

    Advanced Options
        Measure multiple modules:
        pytest --cov=module1 --cov=module2

        Fail if coverage is too low:
        pytest --cov=math_ops --cov-fail-under=80
"""