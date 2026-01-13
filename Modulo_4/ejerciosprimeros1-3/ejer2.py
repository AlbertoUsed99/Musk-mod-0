import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from child import Child

hijo = Child(10, 20, 30)
hijo.display()
