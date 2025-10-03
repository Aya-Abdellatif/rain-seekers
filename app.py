from flask import Flask, render_template, request
from weather_predictor import WeatherPredictor
from data_handler import DataHandler
import datetime


app = Flask(__name__)

cities = {
    "Cairo": (30.0444, 31.2357),
    "Tokyo": (35.6762, 139.6503),
    "Rio": (-22.9068, -43.1729),
    "Sydney": (-33.8688, 151.2093),
    "WashingtonDC": (38.9072, -77.0369),
}

weather_predictor = WeatherPredictor("model/model.keras", "scaler/scaler.pkl")
data_handler = DataHandler("data/data.feather", cities, weather_predictor)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/insights", methods=["GET", "POST"])
def insights():
    if request.method == "GET":
        return render_template("insights-form.html")
    elif request.method == "POST":
        plot = request.form.get("plot")
        city = request.form.get("city")
        start_date = datetime.datetime.strptime(request.form.get("start_date"), "%Y-%m-%d")
        if request.form.get("end_date"):
            end_date = datetime.datetime.strptime(request.form.get("end_date"), "%Y-%m-%d")
        else:
            end_date = start_date

        data = data_handler.get_range(start_date, end_date, city).to_dict(orient="records")
        print(data)
        return render_template("result.html", data=data, plot=plot)