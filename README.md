# 🧪 Pytest Tutorial Series

Welcome to the Pytest Learning Series!
This repository documents a hands-on journey through core Pytest concepts, automation techniques, and testing strategies using Python—perfect for QA engineers, developers, or curious coders.

---

## 🎯 Project Purpose / Challenge Solved

Writing clean, reliable tests can be challenging for beginners—especially beyond basic `assert` statements.
This series bridges the gap between theory and practical automation using Pytest. From simple test functions to full CI/CD integration, each module builds skills that empower real-world software testing.

The goal is to:

- Reinforce core testing principles using Pytest
- Build confidence designing scalable test suites
- Explore plugins, reporting tools, and best practices
- Prepare for professional QA roles and CI/CD workflows

---

## 📚 What's Inside


- **Installation & Setup** – Creating virtual environments, installing Pytest
- **Test Writing Basics** – Writing test functions with `assert`
- **Parametrization** – Simplify repetitive test logic using decorators
- **Fixtures** – Reuse test setup with `@pytest.fixture`
- **Monkeypatching** – Mock functions, variables, and external behavior
- **Test Organization** – Folder structures, naming conventions, class-based tests
- **CLI Usage** – Running tests with `-s`, `-v`, `-k`, and custom markers
- **Plugins** – Coverage reports, HTML reports, mocking, parallel testing
- **CI/CD Integration** – Running Pytest in GitHub Actions and Jenkins pipelines

---

## 🔌 Automation / Real-World Utility

Real-world benefits from this series:

- Grouping tests by type (unit, regression, smoke)
- Tagging and filtering tests with markers
- Auto-generating HTML and coverage reports
- Mocking real-world edge cases for testing reliability
- Seamless integration with GitHub Actions for automated testing

---

## ✅ Learning Goals

- Understand Pytest fundamentals and its Pythonic syntax
- Write readable, maintainable tests for any scale of project
- Explore real-world testing strategies for automation
- Build confidence integrating Pytest with Git & CI pipelines

---

## 🛠️ Tools Used

- Python 3.13+
- Pytest (8.x)
- PyCharm
- Git & GitHub
- Optional Plugins: `pytest-html`, `pytest-cov`, `pytest-mock`, `pytest-xdist`

---

## 🤝 Contributions

This is a personal learning project—but collaboration is always welcome! Fork it, suggest improvements, add your own test scenarios, or open issues to make learning better for everyone 😊

---

## 📅 Updates

This repo will grow regularly with new test modules, plugins, and CI/CD examples. Stay tuned for markers, fixtures, mocking examples, and coverage analytics!

---

## 🚀 How to Run

Clone this repo to your machine:

```bash
git clone https://github.com/your-username/Pytest_Learning.git
cd Pytest_Learning

Create and activate a virtual environment:
python -m venv .venv
.\.venv\Scripts\activate
pip install pytest

Run any test file:
pytest -s test_first_function.py

Happy testing! 🔍🧪
