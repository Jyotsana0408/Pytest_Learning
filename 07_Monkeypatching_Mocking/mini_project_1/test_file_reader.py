"""
Goal of the Test

You're testing a function called read_file() without actually reading a real file.
Instead, you're pretending to read a file using a fake version of open().

Step-by-step explanation

1. Import the real function you're testing
        from file_reader import read_file
        – You want to test read_file() that normally opens a file.

2. Start the test function and create a fake open()
        def test_read_file(monkeypatch):
        – Pytest gives you monkeypatch to help replace parts of your code.

3. Write a fake open() function
        def mock_open(*args, **kwargs):
        – This acts like open(), but doesn’t read any real file.

4. Simulate the file object
        class MockFile:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return "Fixed mock content"
        – This mimics how a file behaves when used with with open(...) in Python.
        – Instead of reading a file, it just returns "Fixed mock content".

5. Tell Pytest to use your fake open()
        monkeypatch.setattr("builtins.open", mock_open)
        – You’re saying: “Hey Python, whenever open() is called, use mock_open() instead.”

6. Run your function and check the result
        result = read_file("dummy.txt")
        assert result == "Fixed mock content"
        – You call read_file(), which uses the fake open() and returns the fake content.
        – Then you check if the result is exactly "Fixed mock content".
"""


from file_reader import read_file

def test_read_file(monkeypatch):
    def mock_open(*args, **kwargs):
        class MockFile:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return "Fixed mock content"
        return MockFile()

    monkeypatch.setattr("builtins.open", mock_open)

    result = read_file("dummy.txt")
    print(result)
    assert result == "Fixed mock content"
