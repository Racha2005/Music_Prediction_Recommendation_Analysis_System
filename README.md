# 🎵 Music Prediction & Recommendation System 🎵

<p align="center">
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032248.png" width="750">
</p>

---

### ▶ Run the Streamlit Dashboard
```bash
streamlit run music_app/app_streamlit/streamlit_dashboard_dark.py
```

<p align="center">
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032340.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032309.png" width="750">
</p>

---

### ▶ Run Desktop Demo
```bash
python -m music_app.app_desktop.desktop_app
```

# or
```bash
python music_app/app_desktop/desktop_app.py
```

<p align="center">
  <img src="images/desktop app/Screenshot 2025-11-22 034012.png" width="750">
</p>

---

### ▶ Train ML Models
```bash
python -m music_app.ml.train_popularity
python -m music_app.ml.train_mood
```

<p align="center">
  <img src="images/data cleaning/Screenshot 2025-11-26 002621.png" width="750"><br>
  <img src="images/data cleaning/Screenshot 2025-11-26 002435.png" width="750">
</p>

---

## 🎧 MUSIC PREDICTION AND RECOMMENDATION SYSTEM

A complete end-to-end **Music Intelligence System** featuring:

- 🌐 Streamlit Analytics Dashboard
- 💻 Tkinter Desktop App
- 🤖 Popularity & Mood ML Models
- 🎧 Audio Feature Extraction
- 🖼️ Image Hashing
- 📝 Lyrics Sentiment Analysis
- 🔍 UMAP + KMeans Clustering
- 🎼 Content-Based Recommendation Engine
- 🌙 Dark Neon Theme

Transforms data → insights → predictions → recommendations.

---

## ⭐ OVERVIEW

Helps users:

- Analyze music trends
- Predict popularity
- Understand mood & energy
- Explore genre distributions
- Use BI-style dashboards
- Get smart recommendations
- Analyze audio, images, lyrics
- Use both web & desktop apps

---

## 📁 FOLDER STRUCTURE

```
music_prediction_recommendation_analysis_project/
│
├── setup.py
├── pyproject.toml
├── requirements.txt
│
├── data/
│   ├── music_dataset_500.csv
│   ├── audio_features.csv
│   ├── image_hashes.csv
│   ├── lyrics_analysis.csv
│   ├── clusters.csv
│   ├── covers/
│   └── audio/
│
└── music_app/
    ├── config.py
    ├── cli.py
    │
    ├── models/
    │   ├── popularity_rf.joblib
    │   └── mood_rf.joblib
    │
    ├── ml/
    │   ├── train_popularity.py
    │   ├── train_mood.py
    │   └── recommender.py
    │
    ├── extras/
    │   ├── audio_features.py
    │   ├── image_hashing.py
    │   ├── lyrics_analysis.py
    │   ├── clustering.py
    │   ├── recommenders.py
    │   ├── organize_music.py
    │   └── voice_commands.py
    │
    ├── app_streamlit/
    │   └── streamlit_dashboard_dark.py
    │
    ├── app_desktop/
    │   └── desktop_app.py
    │
    └── app_flask/
        ├── app.py
        └── templates/
            └── index.html
```

---

## 🚀 RUN COMMANDS

### Activate Virtual Environment
```bash
.\venv\Scripts\Activate.ps1
```

### Run Streamlit Dashboard
```bash
streamlit run music_app/app_streamlit/streamlit_dashboard_dark.py
```

### Run Desktop App
```bash
python music_app/app_desktop/desktop_app.py
```

### Train Models
```bash
python -m music_app.ml.train_popularity
python -m music_app.ml.train_mood
```

---

## 📊 FEATURES

### Streamlit Dashboard

<p align="center">
  <img src="images/streamlit dashboard/Screenshot 2025-11-26 004111.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-26 014127.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032731.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032644.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032606.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032548.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032532.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032454.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032446.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 032606.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 003957.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 004006.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 004018.png" width="750"><br>
  <img src="images/streamlit dashboard/Screenshot 2025-11-22 004025.png" width="750">
</p>

- KPI cards
- Genre stats (bar + donut)
- Popularity vs tempo
- Mood pie chart
- Energy histogram
- Filters
- Recommendation table
- Image hashing viewer
- Audio feature table
- Sentiment table
- Clustering graphs

---

### Desktop App

<p align="center">
  <img src="images/desktop app/Screenshot 2025-11-26 014413.png" width="750"><br>
  <img src="images/desktop app/Screenshot 2025-11-26 014547.png" width="750"><br>
  <img src="images/desktop app/Screenshot 2025-11-26 014643.png" width="750"><br>
  <img src="images/desktop app/Screenshot 2025-11-26 015038.png" width="750">
</p>

- Top tracks view
- Genre charts
- Recommendations popup
- Import audio option

---

## 📦 TECHNOLOGIES

Python, Streamlit, Tkinter  
pandas, numpy, scikit-learn, joblib  
librosa, nltk, pillow, imagehash  
UMAP, KMeans  

---

## 📄 MIT LICENSE

This project is released under the MIT License and can be used, modified, or redistributed with proper credit.

---
