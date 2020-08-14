# Importing a whole module

import helpful
my_list = ["Small", "Medium",  "Large", "Python"] 

my_a_list = helpful.has_a(my_list)      # Only grab the elements with "a"
assert my_a_list == ["Small", "Large"]  # Which should be Small and Large

my_even_list = helpful.is_even(my_list)      # Only grab the elements of even length
assert my_even_list == ["Medium", "Python"]  # Which should be Medium and Python


# Importing a single function

from helpful import has_a

my_list = ["Small", "Medium",  "Large", "Python"]
my_a_list = has_a(my_list)
assert my_a_list == ["Small", "Large"]


# Importing as a certain name

import helpful as hlp

my_list = ["Small", "Medium",  "Large", "Python"]
my_a_list = hlp.has_a(my_list)
assert my_a_list == ["Small", "Large"]