# Imports in Python allow access to external modules or packages to reuse code.
# Python searches for modules in sys.path, including built-ins, current dir, and site-packages.

import math              # Imports the entire module
import math as m         # Alias for the module
from math import sqrt    # Imports specific function
from math import *       # Imports everything (not recommended)