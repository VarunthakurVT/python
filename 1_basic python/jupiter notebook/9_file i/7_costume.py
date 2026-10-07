import sys
from PIL import Image

if len(sys.argv) != 3:
    raise SystemExit("Usage: python 7_costume.py input_image output_image")

with Image.open(sys.argv[1]) as image:
    image.save(sys.argv[2])