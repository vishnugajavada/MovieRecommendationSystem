# MovieRecommendationSystem
# 🎬 Movie Recommendation System

> A content-based movie recommendation engine powered by NLP and the TMDB API, with an interactive Streamlit web interface.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-4B8BBE?style=flat)
![TMDB](https://img.shields.io/badge/API-TMDB-01B4E4?style=flat&logo=themoviedatabase&logoColor=white)


---

## 📖 Overview

This project recommends movies based on **content similarity** — analyzing movie metadata like genres, cast, director, and plot overview to suggest films that closely match the one you select. It uses **TF-IDF vectorization** and **cosine similarity** to find the best matches, and fetches live posters and metadata from the **TMDB API**.

---

## ✨ Features

- 🔍 **Smart Content-Based Recommendations** — finds similar movies using NLP-driven metadata analysis
- 🖼️ **Live Movie Posters** — fetches real-time posters and details via the TMDB API
- 🎛️ **Interactive UI** — clean Streamlit web app with dropdown selection and grid display
- ⚡ **Cached Similarity Matrix** — precomputed results for fast, lag-free recommendations
- 🧹 **Robust Preprocessing Pipeline** — handles missing values, normalizes text, and builds a rich feature "soup"

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **NLP:** Scikit-learn (TF-IDF, Cosine Similarity)
- **Frontend:** Streamlit
- **Data Source:** TMDB API
- **Data Handling:** Pandas, NumPy
- **Storage:** CSV (cached dataset)

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── app.py                  # Streamlit web application
├── recommender.py          # Core recommendation logic
├── preprocess.py           # Data cleaning and feature engineering
├── fetch_data.py           # TMDB API data collection
│
├── data/
│   ├── movies.csv          # Processed movie dataset
│   └── similarity.pkl      # Cached cosine similarity matrix
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

**1. Data Collection**
Movie metadata (title, overview, genres, keywords, cast, crew, and posters) is fetched from the TMDB API and stored locally in a CSV file for efficient reuse.

**2. Preprocessing**
A preprocessing pipeline cleans the raw data — fills missing values, normalizes text to lowercase, removes special characters, and combines `overview + genres + cast + director` into a single `soup` feature field.

**3. Vectorization (TF-IDF)**
The soup text is converted into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency), which assigns higher weight to rare but meaningful words while downweighting common ones.

**4. Similarity Calculation**
Cosine Similarity is computed across all movie vectors. When a user selects a movie, its vector is compared against all others and the top-N closest matches are returned as recommendations.

**5. Streamlit Interface**
The frontend provides a searchable dropdown for movie selection, a "Recommend" button to trigger results, and a responsive grid showing recommended movie posters and titles.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A free [TMDB API key](https://www.themoviedb.org/settings/api)

### Installation

```bash
# Clone the repository
git clone https://github.com/vishnugajavada/movie-recommendation-system.git
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory and add your TMDB API key:

```env
TMDB_API_KEY=your_api_key_here
```

### Run the App

```bash
# (Optional) Fetch fresh data from TMDB
python fetch_data.py

# Launch the Streamlit app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
requests
python-dotenv
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 📸 Demo

> 💡 Example: Searching for **Iron Man** will recommend movies like *Avengers*, *Thor*, and *Captain America* based on shared cast, genre, and thematic keywords.

*Screenshots coming soon.*

---

## 🔧 Configuration Options

You can tweak the following parameters in `recommender.py`:

- **`TOP_N`** *(default: 10)* — Number of recommendations to return
- **`WEIGHT_GENRE`** *(default: 2x)* — Genre keywords are weighted higher
- **`WEIGHT_DIRECTOR`** *(default: 2x)* — Director name is weighted higher
- **`MAX_FEATURES`** *(default: 5000)* — Max TF-IDF vocabulary size

---

## 🧠 Key Concepts

**TF-IDF (Term Frequency–Inverse Document Frequency)**
A numerical statistic that reflects how important a word is to a document in a collection. Rare but meaningful terms (like *superhero* or *dystopian*) score higher than common words (like *the* or *and*).

**Cosine Similarity**
Measures the angle between two vectors in multi-dimensional space. A score of `1.0` means identical; `0.0` means no similarity. Movies sharing similar themes, genres, and cast score higher.

**Content-Based Filtering**
Unlike collaborative filtering (which uses user ratings), this approach recommends based purely on the properties of the content itself — ideal for new users with no watch history.

---

## 🚧 Known Limitations

- Recommendations are based solely on metadata — user preferences and watch history are not considered
- Dataset is limited to popular movies for performance; niche films may have fewer recommendations
- TMDB API rate limits may slow down initial data fetching for large datasets

---

## 🔮 Future Improvements

- [ ] Add collaborative filtering using user ratings
- [ ] Integrate a hybrid recommendation model (content + collaborative)
- [ ] Deploy on Streamlit Cloud or Hugging Face Spaces
- [ ] Add movie trailer previews via YouTube API
- [ ] Support multi-language movie recommendations

---

## 👤 Author

**Gajavada Vishnu**
M.Tech Integrated Software Engineering — VIT Vellore (2021–2026)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Vishnu%20Gajavada-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/vishnugajavada)
[![GitHub](https://img.shields.io/badge/GitHub-vishnugajavada-181717?style=flat&logo=github)](https://github.com/vishnugajavada)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> ⭐ If you found this project helpful, consider giving it a star!
