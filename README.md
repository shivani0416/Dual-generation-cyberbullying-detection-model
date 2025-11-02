# 🧠 Cyberbullying Detection – Dual Gen-Z & Millennial Mode

### 👩‍💻 Developed by: *Shivani Kawade*

---

## 🌍 Overview

This project is an **AI-powered Cyberbullying Detection System** designed to identify **offensive or non-offensive** comments across two distinct language styles — **Gen-Z** and **Millennial**.
It uses **machine learning models** stacked through **meta-learning** and **sentence embeddings** to detect offensive, sarcastic, and subtle bullying patterns online.

---

## 🚀 Key Features

* 🧩 Dual-mode classification: Gen-Z & Millennial
* 🤖 Stacked ensemble of SVM, Random Forest & XGBoost
* 💬 SentenceTransformer embeddings (`all-MiniLM-L6-v2`)
* 🔄 Handles slang, emojis & sarcasm effectively
* 🌐 Interactive Flask web interface
* 📊 Dynamic testing log for real-time evaluation

---

## 🧱 Tech Stack

| Category            | Tools / Libraries                         |
| ------------------- | ----------------------------------------- |
| **Frontend**        | HTML, Tailwind CSS, JavaScript            |
| **Backend**         | Flask (Python)                            |
| **ML Models**       | SVM, Random Forest, XGBoost, Meta-Model   |
| **NLP Embeddings**  | SentenceTransformer                       |
| **Preprocessing**   | Regex, Emoji Mapping, Slang Normalization |
| **Version Control** | Git & GitHub                              |

---

## ⚙️ Project Workflow

1. **Data Collection & Cleaning:** Preprocessed Gen-Z and Millennial text samples.
2. **Feature Extraction:** Converted text into embeddings using `SentenceTransformer`.
3. **Model Training:**

   * Trained base models (SVM, RF, XGBoost).
   * Stacked their predictions using a meta-classifier for higher accuracy.
4. **Flask Integration:** Unified backend for dual mode prediction.
5. **Frontend Design:** Built a clean, responsive UI with real-time prediction and logging.

---

## 🧩 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/<your-username>/cyberbullying-detection.git

# Navigate to project directory
cd cyberbullying-detection

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** 🌐

---

## 🎯 Results

* Achieved high confidence classification for both modes.
* Effectively handles sarcasm and emoji-heavy text.
* Clear visual interface for real-time evaluation and data logging.

---

## 💡 Future Enhancements

* Expand dataset with multilingual text.
* Integrate transformer-based models like BERT or RoBERTa.
* Deploy on cloud for public access.

---

## 🏅 About the Project

This project was developed for **Avishkar Competition**, showcasing innovative use of **NLP and AI** for **online safety and sentiment understanding**.
