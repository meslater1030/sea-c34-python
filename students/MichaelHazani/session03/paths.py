import pathlib


def pathvar():
    """can a pathlib path be a variable?"""
    thispath = pathlib.Path('./')
    print(thispath.absolute())

# pathvar()
# result: sure can!
# output: /Users/mhazani/Documents/Coding/Python/Codefellows/sea-c34-python/
# students/MichaelHazani/session03
