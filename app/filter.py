import base64
import os
import re
from io import BytesIO
from PIL import Image, ImageFilter, ImagePalette

UPLOAD_FOLDER = os.path.basename('uploads')

# add image filters
def filter_image(filename, filter):
    # strip off prefix from JavaScript File Reader
    image_str = re.sub('^data:image/.+;base64,', '', filename)
    # save decoded Base64 string to bytes object, to simulate file I/O
    in_buffer = BytesIO(base64.b64decode(image_str))
    # Use bytes object to create PIL Image object
    im = Image.open(in_buffer)
    if filter == 'b':
        out = im.filter(ImageFilter.GaussianBlur())
    elif filter == 'g':
        out = im.convert('L')
    elif filter == 's':
        if im.mode != "L":
            im = im.convert("L")
        # Uses make_linear_ramp to create sepia tone palette
        im.putpalette(ImagePalette.sepia("#e5d8ac"))
        out = im
    
    # out.save(UPLOAD_FOLDER + "\\" + outfile + ".png")
    out_buffer = BytesIO()
    out.save(out_buffer, format="PNG")
    image_str = out_buffer.getvalue()                     
    out_str = str(b"data:image/png;base64," + base64.b64encode(image_str))
    reg = re.sub("^b(?P<quote>['\"])(.*?)(?P=quote)", r'\2', out_str)
    return reg
