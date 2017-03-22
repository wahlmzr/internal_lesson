# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:48:07 2017

@author: wahlmzr
"""

from PIL import Image
import sys
from pyocr import pyocr
from PIL import Image
import sys
from pyocr import pyocr
from pyocr import builders


tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
print("Using '%s'" % (tools[0].get_name()))
tools[0].image_to_string(Image.open('showphone.gif'), lang='fra',builder=TextBuilder())