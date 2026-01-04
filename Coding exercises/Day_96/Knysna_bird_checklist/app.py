# Import needed modules
from flask import Flask, render_template, request
from python_functions import get_date_range, fetch_bird_data

# Define global variables
PENTAD = "3400_2300"
NUM_YEARS_NEEDED = 1

# Define flask app - single page with checklist
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    start_dt, end_dt = get_date_range(NUM_YEARS_NEEDED)
    species_df = fetch_bird_data(PENTAD, start_dt, end_dt)
    species_list = species_df.to_dict("records")
    stats = None
    seen_species_names = []

    if request.method == "POST":
        if "reset" in request.form:
            seen_species_names = []
            seen_species = []
            total_birds = len(species_list)
            seen_count = 0
            stats = {
                "total_birds": total_birds,
                "seen_count": seen_count,
                "percentage": 0
            }
        else:
            seen_species_names = request.form.getlist("Species")
            seen_species = [species for species in species_list if species['Species'] in seen_species_names]
            total_birds = len(species_list)
            seen_count = len(seen_species)

            stats = {
                "total_birds": total_birds,
                "seen_count": seen_count,
                "percentage": round((seen_count/total_birds)*100, 2)
            }

    return render_template("index.html", species_list=species_list, stats=stats,
                           seen_species_names=seen_species_names)


if __name__ == "__main__":
    app.run(debug=True)
