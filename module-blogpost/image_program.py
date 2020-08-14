# Importing a submodule with the package prefix
import image.filters.sepia

my_img = "Hello World"
sepia_img = image.filters.sepia.apply_filter(my_img)

# Importing a submodule directly

from image.filters import sepia

my_img = "Hello GitHub"
sepia_img = image.filters.sepia.apply_filter(my_img)

# Importing a function from a module directly

from image.filters.sepia import apply_filter
my_img = "Hello jordantwells"
sepia_img = apply_filter(my_img)