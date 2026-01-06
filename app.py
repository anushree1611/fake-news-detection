from flask import Flask, render_template, request
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

model = pickle.load(open(os.path.join(BASE_DIR, "model", "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "model", "vectorizer.pkl"), "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        news = request.form["news"]
        data = vectorizer.transform([news])
        result = model.predict(data)[0]
        prediction = "REAL NEWS" if result == "REAL" else "FAKE NEWS"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
