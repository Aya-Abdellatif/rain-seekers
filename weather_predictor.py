import datetime
import tensorflow as tf
import joblib
import numpy as np

class WeatherPredictor:
    def __init__(self, model_path: str, scaler_path: str):
        self.model = tf.keras.models.load_model(model_path)
        self.scaler = joblib.load(scaler_path)

    def _make_features(lat: float, lon: float, dt: datetime.datetime):
        """Convert raw lat, lon, datetime into model-ready features."""

        day_of_year = dt.timetuple().tm_yday
        month = dt.month


        day_sin = np.sin(2 * np.pi * day_of_year / 365)
        day_cos = np.cos(2 * np.pi * day_of_year / 365)

        month_sin = np.sin(2 * np.pi * month / 12)
        month_cos = np.cos(2 * np.pi * month / 12)

        # Location features
        lat_sin = np.sin(np.radians(lat))
        lat_cos = np.cos(np.radians(lat))
        lon_sin = np.sin(np.radians(lon))
        lon_cos = np.cos(np.radians(lon))

        # Arrange in the same order as training
        return np.array([[
            day_sin, day_cos,
            month_sin, month_cos,
            lat_sin, lat_cos,
            lon_sin, lon_cos
        ]])
    
    def predict(self, dt: datetime.datetime, location: tuple[str, str]) -> dict[str, datetime.datetime | float]:
        """Return predicted weather for given lat, lon, datetime."""
        lat, lon = location
        features = self._make_features(lat, lon, dt)
        prediction = self.scaler.inverse_transform(self.model.predict(features, verbose=0))[0]

        return {
            "time": dt,
            "lat": lat,
            "lon": lon,
            "T2M": float(prediction[0]),    # Temperature at 2m
            "QV2M": float(prediction[1]),  # Specific humidity
            "U10M": float(prediction[2]),    # Eastward wind
            "V10M": float(prediction[3]),    # Northward wind
            "PS": float(prediction[4])        # Surface pressure
        }