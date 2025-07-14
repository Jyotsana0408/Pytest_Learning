
"""
In pytest, monkeypatching is a powerful technique used to temporarily modify or override parts of your code during
testing without changing the actual source code.

It’s especially handy when you want to isolate your tests from external dependencies like
APIs, databases, or environment variables.

What You Can Monkeypatch :
    Functions or methods:   Replace a function with a mock version.
    Attributes:             Override object properties.
    Environment variables:  Simulate different system configurations.
    Dictionary values:      Modify config settings or global states.
    System paths:           Adjust sys.path for module imports.

Cleanup Is Automatic :
    All changes made with monkeypatch are automatically reverted after the test finishes, keeping your test environment clean.

Core Methods of monkeypatch :
    Method	                        Purpose	                            Example
    setattr(obj, name, value)	    Replace an attribute or method	    monkeypatch.setattr(Path, "home", mock_home)
    delattr(obj, name)	            Delete an attribute                	monkeypatch.delattr(os, "getcwd")
    setitem(mapping, key, value)	Modify a dictionary	                monkeypatch.setitem(config, "timeout", 10)
    delitem(mapping, key)	        Remove a dictionary key	            monkeypatch.delitem(config, "timeout")
    setenv(name, value)	            Set an environment variable	        monkeypatch.setenv("USER", "test_user")
    delenv(name)	                Delete an environment variable	    monkeypatch.delenv("USER")
    syspath_prepend(path)	        Add a path to sys.path	            monkeypatch.syspath_prepend("/custom/path")
    chdir(path)	                    Change working directory	        monkeypatch.chdir("/tmp")

Imp questions and answers :
    1. What Is Monkeypatching in Python?
            Monkeypatching is when you temporarily change or replace part of a program during runtime
            usually to test something without affecting the original code.

    2. How to Use Monkeypatch in Pytest ?
            Use the monkeypatch fixture to replace functions, variables, or config.

            Replace a Function
            monkeypatch.setattr("module.function", lambda: "fake response")

            Replace an Environment Variable
            monkeypatch.setenv("USER", "TestUser")
            Monkeypatch automatically restores everything after the test finishes.

    3. Can you give an example?
            Yes! Swap a function using setattr, or fake an env var with setenv.

    4.What's the difference between monkeypatching and mocking?
            Monkeypatch replaces parts of code. Mocking creates fake versions with tracking.

    5. Monkeypatch vs Mocking ?
            Feature	    Monkeypatch	                Mocking
            Use Case	Replace something quickly	Create test doubles
            Tracking	No	                        Yes — mocks track calls, args, etc.
            Tool	    Pytest	                    unittest.mock or pytest-mock


"""
import monkey_patching

"""
What’s Happening Here -->
    greet() normally returns a real message.
    In the test, we replace greet() with fake_greet() using monkeypatch.setattr.
    The test checks that the monkeypatched version is used.
    After the test, pytest automatically restores the original greet() function.
"""
def test_greet(monkeypatch):
    # Define a fake version of greet
    def fake_greet():
        return "Hello from the fake function!"

    # Replace the real greet with the fake one
    monkeypatch.setattr(monkey_patching, "greet", fake_greet)

    # Now calling greet() will use the fake version
    assert monkey_patching.greet() == "Hello from the fake function!"

