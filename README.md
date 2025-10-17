# 🌧️ RainSeekers

RainSeekers is a web application developed for the **NASA Space Apps Hackathon 2025**.  
It predicts **temperature, pressure, humidity, and wind speed** for a given location and date, then evaluates whether specific activities (like going on a picnic, visiting the beach, or hosting a concert) are suitable for that day.  

Our mission: **Help people plan better, safer, and more enjoyable activities by making NASA’s weather data accessible to everyone.**

---

## 🚀 Features

- **NASA Data Integration** – Uses NASA’s **M2T1NXSLV v5.12.4** dataset (1980–1983, 1991–2011).
- **Deep Learning Predictions** – Forecasts:
  - Temperature (`T2M`)
  - Humidity (`QV2M`)
  - Wind speed (`U10M`, `V10M`)
  - Surface pressure (`PS`)
- **Supported Cities** – Cairo, Washington DC, Rio de Janeiro, Tokyo, Sydney.
- **Activity Scoring System** – Rates how suitable the weather is for different activities.
- **Historical & Future Data** – Explore trends and predict upcoming conditions.
- **Data Visualizations** – Interactive charts for a clear, user-friendly experience.
- **Accessible Web Platform** – No technical background needed.

---
## 🛰️ Data Pipeline & Processing

We designed an optimized pipeline to handle large NASA climate datasets efficiently:

### 1️⃣ Data Collection  
- Downloaded from NASA using [`eatchaccess`](https://pypi.org/project/earthaccess/).  
- Extracted only the 5 supported cities: **Cairo, Washington DC, Rio de Janeiro, Tokyo, Sydney**.  
- Selected daily averages for key variables:  
  - `T2M` (temperature)  
  - `QV2M` (humidity)  
  - `U10M`, `V10M` (wind components)  
  - `PS` (surface pressure)  

⏱️ **Performance:**  
- Sequential processing: **3–5 hours per year** of data.  
- With multithreading: **40–60 minutes per year**.  
- Saved intermediate results to avoid repeating this step.

---

### 2️⃣ Preprocessing  
- Converted raw NetCDF data to **Pandas DataFrames**.  
- Engineered new features to represent **cyclic variables**:  
  - Day: `day_sin`, `day_cos`  
  - Month: `month_sin`, `month_cos`  
  - Latitude: `lat_sin`, `lat_cos`  
  - Longitude: `lon_sin`, `lon_cos`  

---

### 3️⃣ Data Optimization  
- Saved preprocessed data in **Feather format (.feather)** for instant loading.  
- Before: Loading NetCDF files for 25 years = **~40 minutes**.  
- After: Loading Feather files = **< 1 second**.  
- Massive improvement in training & prediction efficiency.  

---

### ⚡ Efficiency Gains (Before vs After)
|Step|Before|After (Optimized)|Improvement|
|----|-----|------|-----|
|Downloading and Processing (1 year)|3-5 hours|40-60 minutes|~4x faster|
|Data Loading (25 yrs)|~40 minutes|< 1 second|~2400× faster|

---

### 🌍 Scalability & Reproducibility
- Scalable: Can be extended to more cities or even global coverage.
- Reproducible: Intermediate and final datasets are saved and versioned, ensuring consistent results without repeating heavy computations.
- Hackathon-Ready: Preprocessed data allows training and predictions in real time during demos.

---

## 🛠️ Tech Stack

- **Backend + Frontend:** Flask (serves both the web interface & API)
- **Machine Learning:** Deep Learning Regression Model
- **Data:** NASA MERRA-2 (`M2T1NXSLV v5.12.4`)
- **Deployment:** *(TBD – local/demo for hackathon use)*

---

## 📈 Model Performance  

We trained a deep learning regression model to predict 5 climate variables. Below are the **Mean Absolute Errors (MAE)** for each target:  

| Variable | Description              | MAE      |
|----------|--------------------------|----------|
| `T2M`    | Temperature (K)          | **1.577** |
| `QV2M`   | Humidity (kg/kg)         | **0.001** |
| `U10M`   | Wind (east-west) (m/s)   | **2.654** |
| `V10M`   | Wind (north-south) (m/s) | **2.855** |
| `PS`     | Surface Pressure (Pa)    | **418.554** |

✅ The errors are within acceptable ranges for climate prediction, making the model reliable for activity planning.  

---

## 📂 Project Structure

```bash
RainSeekers/
│── data/                    # Dataset (for historical data)
│── model/                   # Trained regression model
│── scaler/                  # The scaler used with the data
│── static/                  # Assets (CSS, JS, images)
│── templates/               # HTML templates
│── README.md                # Documentation
│── app.py                   # The flask app
│── data_handler.py          # The component responsible for handling data efficiently
│── weather_predictor.py     # The component responsible for predicting future/unavailable data
│── requirements.txt         # The required python libraries
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Aya-Abdellatif/rain-seekers.git
cd rain-seekers
pip install -r requirements.txt
```

Run the Flask app:

```bash
flask run
```

Open in your browser at:  
👉 `http://localhost:5000`

---

## 📊 How It Works

1. **Input**: User selects a city and a date.  
2. **Prediction**: The deep learning model forecasts weather variables.  
3. **Activity Scoring**: The system assigns a score (e.g., "Good for picnic 🌳", "Bad for outdoor concerts 🎤").  
4. **Visualization**: Charts display historical trends and predicted values.  
5. **Recommendation**: Users receive a simple, actionable suggestion.

---

## 🌍 Impact

RainSeekers makes **NASA’s weather data accessible to everyone**.  
- Helps individuals plan safe outdoor activities.  
- Supports event organizers (e.g., concerts, sports).  
- Provides insights for communities and small farmers.  
- Educates students and enthusiasts about data-driven climate forecasting.  

---

## 🌐 Web App Interface

### Home Page
<img width="1891" height="947" alt="image" src="https://github.com/user-attachments/assets/c1595413-2045-4917-9f07-c0af35e96432" />

### Weather Insights
<img width="1457" height="3782" alt="screencapture-127-0-0-1-5000-insights-2025-10-04-05_49_57 (1)" src="https://github.com/user-attachments/assets/d60816aa-2c1c-4237-a6f2-024ae6a55b8a" />

### About Us
<img width="1894" height="951" alt="image" src="https://github.com/user-attachments/assets/72e77e1e-bab5-4646-88c6-5ca27738d81d" />

### Clothing Recommendation
<img width="1457" height="1508" alt="screencapture-127-0-0-1-5000-extra-2025-10-04-05_50_28" src="https://github.com/user-attachments/assets/3ebe5d49-a98e-4aff-9a69-64430ec3896d" />


---

## 👩‍💻 Team

Developed by **Team RainSeekers** for the **NASA Space Apps Hackathon 2025**:  
<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/99624292?v=4" width="100px;" alt="Pavly Samuel"/>
      <br />
      <a href="https://www.linkedin.com/in/pavlysamuel/">Pavly Samuel</a>
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D03AQEL76ybhUiNuQ/profile-displayphoto-scale_400_400/B4DZiqi1n8HwAg-/0/1755207919013?e=1762387200&v=beta&t=8tZpMAWETpMPZCN8TfCjSABxRALYFGIK6ND-8Zl-xvI" width="100px;" alt="Aya Abdellatif"/>
      <br />
      <a href="https://www.linkedin.com/in/aya-abdllatif/">Aya Abdullatif</a>
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D03AQHzzKu1Bc4rDA/profile-displayphoto-crop_800_800/B4DZivj0IjGgAQ-/0/1755292059795?e=1762387200&v=beta&t=900D7A3-fGIJEan4WMNxurw7FIjZKamcEuvbPO6fgFQ" width="100px;" alt="Aalaa Ayman"/>
      <br />
      <a href="https://www.linkedin.com/in/aalaa-ayman/">Aalaa Ayman</a>
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D03AQEv-tvnkAnaKw/profile-displayphoto-crop_800_800/B4DZkoznvcIgAI-/0/1757326246833?e=1762387200&v=beta&t=rqGrIum6eyf7exxtemIM-HFBY9YTxQJTxFpAXx3hKKo" width="100px;" alt="Ahmed Essam"/>
      <br />
      <a href="https://www.linkedin.com/in/ahmed-essam538/">Ahmed Essam</a>
    </td>
  </tr>
</table>

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.  

---

✨ *“Exploring data, predicting tomorrow.”* – RainSeekers
