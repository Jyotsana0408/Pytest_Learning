"""
Goal of the Test
You're testing your function get_data() from api_client.py, which likely makes a request to an API using requests.get().
But instead of actually calling a real API, you're using monkeypatching to fake the network call and give a controlled
response.

Step-by-step Breakdown
1. Create a fake response object
        class MockResponse:
            def json(self): return {"key": "mocked_value"}
        – This is a fake version of the object you'd get from requests.get()
        – It has a .json() method that returns a fixed dictionary.

2. Create a fake requests.get() function
        def mock_get(*args, **kwargs):
            return MockResponse()
        – This fake function replaces requests.get() – When called, it returns the fake response.

3. Tell Pytest to use your fake get()
        monkeypatch.setattr("requests.get", mock_get)
        – This replaces the real requests.get() with mock_get() just during the test.

4. Import the function to test and run it
        from api_client import get_data
        result = get_data()
        – You run get_data(), and instead of making a real API call, it uses your fake one.
        – This means it gets {"key": "mocked_value"} without connecting to the internet.

5. Check that the result is correct
        assert result == {"key": "mocked_value"}
        – This confirms that your get_data() function handled the fake response properly.

Why this is useful
        No actual network needed
        Fast and reliable tests
        You control exactly what requests.get() returns
"""
def test_get_data(monkeypatch):
    class MockResponse:
        def json(self): return {"key": "mocked_value"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    from api_client import get_data
    result = get_data()
    print(result)
    assert result == {"key": "mocked_value"}
