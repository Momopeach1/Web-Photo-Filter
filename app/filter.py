import os
from PIL import Image, ImageFilter, ImagePalette

UPLOAD_FOLDER = os.path.basename('uploads')

# Creates color gradient of designated color.
def make_linear_ramp(color):
    ramp = []
    r, g, b = color
    for i in range(255):
        ramp.extend((r*i//255, g*i//255, b*i//255))
    return ramp

# add image filters
def filter_image(filename, filter):
    im = Image.open(UPLOAD_FOLDER + "\\" + filename)
    if filter == 'b':
        out = im.filter(ImageFilter.GaussianBlur())
    elif filter == 'g':
        out = im.convert('L')
    elif filter == 's':
        if im.mode != "L":
            im = im.convert("L")
        # Uses make_linear_ramp to create sepia tone palette
        im.putpalette(ImagePalette.sepia("#e5d8ac"))
        im.save(UPLOAD_FOLDER + "\\a.png")
        out = im
    outfile = filename.split('.')[0] + "_transform"
    out.save(UPLOAD_FOLDER + "\\" + outfile + ".png")
    return outfile + ".png"
