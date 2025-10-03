# 🌧️ RainSeekers

RainSeekers is a web application developed for the **NASA Space Apps Hackathon**.  
It predicts **temperature, pressure, humidity, and wind speed** for a given location and date, then evaluates whether specific activities (like going on a picnic, visiting the beach, or hosting a concert) are suitable for that day.  

Our mission: **Help people plan better, safer, and more enjoyable activities by making NASA’s weather data accessible to everyone.**

---

## 🚀 Features

- 🔭 **NASA Data Integration** – Uses NASA’s **M2T1NXSLV v5.12.4** dataset (1980–1983, 1991–2010).
- 📊 **Deep Learning Predictions** – Forecasts:
  - 🌡️ Temperature (`T2M`)
  - 💧 Humidity (`QV2M`)
  - 🌬️ Wind speed (`U10M`, `V10M`)
  - 🏞️ Surface pressure (`PS`)
- 🌍 **Supported Cities** – Cairo, Washington DC, Rio de Janeiro, Tokyo, Sydney.
- 🎯 **Activity Scoring System** – Rates how suitable the weather is for different activities.
- 📜 **Historical & Future Data** – Explore trends and predict upcoming conditions.
- 📈 **Data Visualizations** – Interactive charts for a clear, user-friendly experience.
- 🖥️ **Accessible Web Platform** – No technical background needed.

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
- Pavly Samuel  
- Aya Abdullatif  
- Aalaa Ayman  
- Ahmed Essam  

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
