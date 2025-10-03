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
|Downlaodinng and Processing (1 year)|3-5 hours|40-60 minutes|4x faster|
|Data Loading (25 yrs)|~40 minutes|< 1 second|~2400× faster|

---

### 🌍 Scalability & Reproducibility
- Scalable: Can be extended to more cities or even global coverage.
- Reproducible: Intermediate and final datasets are saved and versioned, ensuring consistent results without repeating heavy computations.
- Hackathon-Ready: Preprocessed data allows training and predictions in real time during demos.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Machine Learning:** Deep Learning Regression Model
- **Data:** NASA MERRA-2 (`M2T1NXSLV v5.12.4`)
- **Frontend:** *(TBD – will be added after final implementation)*
- **Deployment:** *(TBD – local/demo for hackathon use)*

---

## 📂 Project Structure

```bash
RainSeekers/
│── backend/          # Flask backend & ML model
│── data/             # Sample datasets (MERRA-2)
│── models/           # Trained regression models
│── frontend/         # Web UI (coming soon)
│── static/           # Assets (CSS, JS, images)
│── templates/        # HTML templates
│── README.md         # Documentation
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/RainSeekers.git
cd RainSeekers
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
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
- 🌱 Helps individuals plan safe outdoor activities.  
- 🎶 Supports event organizers (e.g., concerts, sports).  
- 🌾 Provides insights for communities and small farmers.  
- 📚 Educates students and enthusiasts about data-driven climate forecasting.  

---

## 👩‍💻 Team

Developed by **Team RainSeekers** for the **NASA Space Apps Hackathon 2025**:  
<table>
  <tr>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D03AQG54S7ivcdAig/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1728139307128?e=1762387200&v=beta&t=hszyUpReqy_e41alKhPQOKVR_Ggx8HKdTr4eEUvrDC4" width="100px;" alt="Pavly Samuel"/>
      <br />
      <a href="https://www.linkedin.com/in/pavlysamuel/">Pavly Samuel</a>
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D35AQGY3JS4r8NAXw/profile-framedphoto-shrink_800_800/B4DZiqi2mfHYAk-/0/1755207920355?e=1760090400&v=beta&t=l28iiqWL8UChjg-3wNnJfBSku8GLwbSK8aNxjlKydf0" width="100px;" alt="Aya Abdullatif"/>
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

## 📸 Screenshots

(Add screenshots of your web app here)  

| Home Page | Prediction Result | Charts & Visualizations |
|-----------|------------------|-------------------------|
| ![Home](images/home.png) | ![Prediction](images/prediction.png) | ![Charts](images/charts.png) |

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.  

---

✨ *“Exploring data, predicting tomorrow.”* – RainSeekers
