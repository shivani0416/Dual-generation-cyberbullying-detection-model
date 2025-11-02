# ==============================================
# 💻 app.py — Sarcasm-aware Cyberbullying Detector
# ==============================================
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from preprocess import normalize_text  # your normalization function

# ------------------------------
# Flask setup
# ------------------------------
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

print("🚀 Loading models & embedding pipeline...")

# ------------------------------
# Load trained models (Gen-Z & Millennials)
# ------------------------------
svm_genz = joblib.load("models/svm_model_genz.pkl")
rf_genz  = joblib.load("models/rf_model_genz.pkl")
xgb_genz = joblib.load("models/xgb_model_genz.pkl")
meta_genz= joblib.load("models/meta_model_genz.pkl")

svm_mill = joblib.load("models/svm_model_mill.pkl")
rf_mill  = joblib.load("models/rf_model_mill.pkl")
xgb_mill = joblib.load("models/xgb_model_mill.pkl")
meta_mill= joblib.load("models/meta_model_mill.pkl")

# ------------------------------
# Load embedding models
# ------------------------------
embedder = SentenceTransformer('paraphrase-mpnet-base-v2')
sentiment_analyzer = pipeline("sentiment-analysis")

print("✅ All models & embedding layers loaded successfully.")


# ==============================================
# 🔮 Prediction Function
# ==============================================
def predict_text(text, mode='genz'):
    # Step 1 — Normalize input
    clean = normalize_text(text)

    # Step 2 — Get contextual + sentiment-aware embedding
    emb_context = embedder.encode([clean])
    sent = sentiment_analyzer([clean])[0]
    sent_vec = np.array([[1 if sent['label'] == 'POSITIVE' else -1, sent['score']]])
    emb = np.concatenate((emb_context, sent_vec), axis=1)

    # Step 3 — Select correct ensemble model
    if mode.lower().startswith('g'):  # Gen-Z
        p1 = svm_genz.predict_proba(emb)[:, 1]
        p2 = rf_genz.predict_proba(emb)[:, 1]
        p3 = xgb_genz.predict_proba(emb)[:, 1]
        X_meta = np.column_stack((p1, p2, p3))
        pred = meta_genz.predict(X_meta)[0]
        conf = meta_genz.predict_proba(X_meta)[0][pred]
    else:  # Millennials
        p1 = svm_mill.predict_proba(emb)[:, 1]
        p2 = rf_mill.predict_proba(emb)[:, 1]
        p3 = xgb_mill.predict_proba(emb)[:, 1]
        X_meta = np.column_stack((p1, p2, p3))
        pred = meta_mill.predict(X_meta)[0]
        conf = meta_mill.predict_proba(X_meta)[0][pred]

    # Step 4 — Format output
    label = "Cyberbullying / Offensive" if pred == 1 else "Non-offensive"
    return {"label": label, "confidence": round(float(conf) * 100, 2)}


# ==============================================
# 🌐 Flask Routes
# ==============================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    text = data.get("text", "")
    mode = data.get("mode", "genz")
    res = predict_text(text, mode)
    return jsonify(res)


# ==============================================
# 🏁 Run Server
# ==============================================
if __name__ == "__main__":
    print("🌸 Flask server running at http://127.0.0.1:5000/")
    app.run(debug=True)
