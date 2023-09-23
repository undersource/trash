from PIL import Image
import sys
import re

img = sys.argv[1]
cimg = sys.argv[2]
extension = re.findall(r'\.(\w+)', cimg)[0]

Image.open(img).convert('RGB').save(cimg, extension)
