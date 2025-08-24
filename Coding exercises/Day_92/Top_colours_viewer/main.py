# Import needed modules
import numpy as np
import os
from PIL import Image
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5


# Define macro variables
NUM_COLOURS = 10


# Open image function
def open_img(img_path):
    img_file = Image.open(img_path)
    img_file = img_file.convert("RGB")
    return img_file


# Count most frequent colour groups function
def top_colours(img_file):
    # Count number of times a colour appears - we want similar colours grouped together to get meaningful results
    palette_img = img_file.quantize(colors=NUM_COLOURS)
    palette = palette_img.getpalette()
    frequent_colours = np.array(palette).reshape(-1, 3)
    return frequent_colours


# Convert RGB to hex function
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


# Initialize app
app = Flask(__name__)
bootstrap = Bootstrap5(app)


# Define home page
@app.route("/", methods=["GET", "POST"])
def display_home():
    img = None
    uploaded_filename = None

    # Clear previous uploads
    for f in os.listdir("static\\uploads"):
        os.remove(os.path.join("static\\uploads", f))

    # If a file is uploaded
    if request.method == "POST":
        if "file" in request.files and request.files["file"].filename != "":
            file = request.files["file"]
            uploaded_filename = file.filename
            save_path = os.path.join("static\\uploads", uploaded_filename)
            file.save(save_path)
            img = Image.open(save_path).convert("RGB")

    # If starting and using default image
    if img is None:
        img = open_img("static/images/flower.jpg")

    main_colours = top_colours(img)

    colours = []
    for rgb in main_colours:
        rgb_tuple = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        colours.append({
            "rgb": rgb_tuple,
            "hex": rgb_to_hex(rgb)
        })

    return render_template("index.html", colours=colours, uploaded_filename=uploaded_filename)


# Run website
if __name__ == '__main__':
    app.run(debug=True)
