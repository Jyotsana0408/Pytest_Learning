"""
Combined CLI Command

    pytest --cov=your_module_name --cov-report=term-missing --html=report.html --self-contained-html

Here’s what each part does:

    Option	                    Purpose
    --cov=your_module_name	    Measure coverage for the specified module
    --cov-report=term-missing	Show missing lines in terminal output
    --html=report.html	        Generate an HTML report
    --self-contained-html	    Include CSS and assets in the report file

"""

def get_extension(filename):
    return filename.split('.')[-1]

def is_text_file(filename):
    return get_extension(filename) == "txt"

def is_image_file(filename):
    return get_extension(filename) in ["png", "jpg", "jpeg"]

def is_video_file(filename):
    return get_extension(filename) in ["mp4", "mov"]
