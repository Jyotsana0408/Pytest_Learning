"""
In Python testing, fixtures are reusable setups that prepare the environment before running tests.
They’re especially powerful in frameworks like Pytest, where they help keep your test code clean, modular,
and DRY (Don’t Repeat Yourself).

What Are Fixtures?
    Fixtures are functions that:
    Run before (and optionally after) a test.
    Provide data, resources, or configurations needed for the test.
    Are marked with @pytest.fixture in Pytest.

Reusability & Scope
    You can control how often a fixture runs using scope:
        function (default): runs before each test
        class: runs once per test class
        module: runs once per module
        session: runs once per test session
        eg: @pytest.fixture(scope="module")

Advanced Use Cases
    Parametrized fixtures for testing multiple inputs
    Yield-based fixtures for teardown logic
    Fixtures defined in conftest.py for sharing across files

If you want to see which fixtures are being used and how they’re set up, use:
command : pytest --setup-show

What --setup-show Does
    Displays detailed info about fixture setup and teardown.
    Shows the order in which fixtures are invoked.
    Helps debug fixture dependencies and scopes.
"""

# Basic Example
import pytest

@pytest.fixture
def input_value():
    return 10

def test_addition(input_value):
    assert input_value + 5 == 15 # Here, input_value is a fixture that supplies data to the test.

"""
Fixture Chaining --> Fixtures can depend on other fixtures:
"""

@pytest.fixture
def base():
    return "Hello"

@pytest.fixture
def greeting(base):
    return base + ", World!"

def test_greeting(greeting):
    assert greeting == "Hello, World!"

"""
Autouse Fixtures

    You can make a fixture run automatically for all tests.
    it run automatically without being explicitly requested.
"""

@pytest.fixture(autouse=True)
def setup_env():
    print("Setting up environment")

"""
Parametrized Fixtures

    Parametrization allows you to run the same test with different inputs. You can apply this to fixtures too!
    Using params in Fixtures
"""

@pytest.fixture(params=[2, 4, 6])
def number(request):
    return request.param

def test_is_even(number):
    assert number % 2 == 0 # This will run the test three times with number set to 1, 2, and 3 respectively

"""
Indirect Parametrization

    clever way to pass parameters to fixtures instead of directly to test functions
    Normally, @pytest.mark.parametrize sends values straight to the test function.
    But with indirect=True, Pytest routes those values through a fixture first.

In below example , Here’s what happens:

    "Apple" and "Banana" are passed to the fruit fixture via request.param.
    The fixture transforms them into "Fruit: Apple" and "Fruit: Banana".
    The test receives the transformed value.
"""

@pytest.fixture
def fruit(request):
    return f"Fruit: {request.param}"

@pytest.mark.parametrize("fruit", ["Apple", "Banana"], indirect=True)
def test_fruit_name(fruit):
    assert "Fruit" in fruit


"""
Partial Indirect Parametrization : You can apply indirect to specific arguments only:
"""

@pytest.fixture
def multiplier(request):
    return request.param * 10

@pytest.mark.parametrize("multiplier", [1, 2, 3], indirect=["multiplier"])
def test_scaled_value(multiplier):
    assert multiplier in [10, 20, 30]

"""
What Is Teardown Logic?
    In testing, setup prepares the environment (ex- opening a DB connection), 
    and teardown cleans it up (ex- closing the connection). 
    Pytest lets you handle both in a single fixture using yield.

How yield Works in Fixtures

    When Pytest encounters a fixture with yield, it:
    Executes the code before yield → this is your setup.
    Pauses and runs the test.
    After the test finishes, resumes and runs the code after yield → this is your teardown.

Why Use yield for Teardown?

    Automatic cleanup: No need for separate teardown functions
    Isolation: Ensures each test runs in a clean environment
    Resilience: Teardown runs even if the test fails or throws an exception

yield vs addfinalizer

    You can also use request.addfinalizer() for teardown, but yield is:
    More readable
    Easier to maintain
    Recommended for most use cases

Real-World Use Case

    Let’s say you’re testing a file handler utility:
    
    This ensures:
        File is created before the test
        File is closed and deleted after the test
        
    @pytest.fixture
    def temp_file():
        # f = open("temp.txt", "w")  
        yield f
        f.close()
        os.remove("temp.txt")   
          
"""

@pytest.fixture
def sample_data():
    print("Setup: Creating sample data")
    data = [1, 2, 3]
    yield data
    print("Teardown: Cleaning up sample data")
    data.clear()


def test_sum(sample_data):
    """
    What Happens Here
        Before the test: sample_data fixture runs and prints setup message.
        During the test: test_sum uses the data [1, 2, 3].
        After the test: Pytest resumes the fixture and runs the teardown code (data.clear()).
    """
    print("Running test")
    assert sum(sample_data) == 6

@pytest.fixture()
def set_up():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close Browser")

def test_add_item_to_cart(set_up):
    print("Add items Successfully")

def test_remove_item_to_cart(set_up):
    print("Remove items Successfully")
