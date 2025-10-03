import datetime
import pandas as pd

from weather_predictor import WeatherPredictor


class DataHandler:
    def __init__(self, data_path: str, cities: dict[str, tuple[float, float]], weather_predictor: WeatherPredictor):
        self.cities = cities
        self.df = pd.read_feather(data_path)
        self.df["time"] = pd.to_datetime(self.df["time"])
        self.weather_predictor = weather_predictor

    def get_range(self, start_date: datetime.datetime, end_date: datetime.datetime, city: str):
        city_df = self._select_near_city(city)

        filtered_df = city_df[(city_df["time"] >= start_date) & (city_df["time"] <= end_date)]

        all_days = pd.date_range(start_date, end_date, freq="D")
        missing_days = all_days.difference(filtered_df["time"])

        missing_df = pd.DataFrame([self._handle_missing(day, self.cities[city]) for day in missing_days])
        final = pd.concat([filtered_df, missing_df]).sort_values("time").reset_index(drop=True)

        return final

    
    def _handle_missing(self, day: datetime.datetime, location: tuple[float, float]):
        return self.weather_predictor.predict(day, location)

    def _select_near_city(self, city, tol=0.5):
        lat, lon = self.cities[city]
        return self.df[
            (self.df["lat"].between(lat - tol, lat + tol)) &
            (self.df["lon"].between(lon - tol, lon + tol))
        ]
    