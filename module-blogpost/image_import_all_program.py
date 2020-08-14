from image.filters import *   # import all from filters according to its __init__.py

assert sepia                  # The sepia filter can be used
assert dog                    # and so can the dog filter

try:
	assert black_and_white
except NameError:
	print("black_and_white isn't imported!")   # but not a b&w one