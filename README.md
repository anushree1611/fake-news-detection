📰 Fake News Detection Website

A Machine Learning–based web application that predicts whether a given news article is FAKE or REAL using Natural Language Processing (NLP) techniques.
The project integrates a trained ML model with a Flask web interface to provide real-time predictions.

🚀 Features

Detects Fake vs Real News from text input

Uses TF-IDF Vectorization for text representation

Logistic Regression classifier with ~98% accuracy

Interactive Flask web application

Clean and simple user interface

End-to-end ML pipeline (data → model → web app)

🧠 Machine Learning Approach

Text Preprocessing:
News articles are cleaned and transformed into numerical vectors using TF-IDF.

Model Used:
Logistic Regression (efficient and well-suited for text classification).

Dataset:
Combined dataset of real and fake news articles with proper labeling.

Accuracy:
Achieved approximately 98% accuracy on test data.

🛠️ Tech Stack

Programming Language: Python

Web Framework: Flask

Machine Learning: Scikit-learn

Data Processing: Pandas, NumPy

Frontend: HTML, CSS

Model Persistence: Pickle

📂 Project Structure
Fake News Detection/
│
├── app.py                 # Flask application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── model/
│   ├── model.pkl          # Trained ML model
│   ├── vectorizer.pkl     # TF-IDF vectorizer
│   ├── model.py           # Model training script
│   └── merge_dataset.py   # Dataset preparation
│
├── templates/
│   └── index.html         # Web page
│
└── static/
    └── images/            # Background images (optional)

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/fake-news-detection.git
cd fake-news-detection

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model (optional)
python model/model.py

4️⃣ Run the Flask app
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000
