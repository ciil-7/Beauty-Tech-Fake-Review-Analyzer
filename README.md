# Beauty-Tech Fake Review Analyzer

A robust Streamlit web application designed to evaluate the authenticity of cosmetic product reviews and extract active skincare ingredients using a supervised Machine Learning pipeline.

## 🚀 Features
* **Review Authenticity Detection:** Analyzes review text to detect unauthentic, overly promotional, or fake hype patterns.
* **Probabilistic Confidence Scoring:** Computes statistical confidence metrics (`predict_proba`) for transparent reliability evaluation.
* **Active Ingredient Extraction:** Automatically identifies active cosmetic ingredients mentioned in the review and lists their clinical skin benefits.
* **Interactive UI:** Built with Streamlit for a fast, responsive, and user-friendly experience.

---

## 📊 Model Architecture & Methodology
The application evaluates review authenticity using a supervised **Machine Learning pipeline** rather than complex generative AI models:
* **Feature Extraction:** Utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** with unigrams and bigrams (`ngram_range=(1, 2)`) to capture individual words and contextual phrase patterns.
* **Classification Algorithm:** Powered by a **Logistic Regression** classifier trained on a balanced corpus of authentic and unauthentic review samples.
* **Confidence Estimation:** Generates probabilistic confidence scores to provide transparent and quantifiable reliability metrics for each analysis.

---

## 📈 Model Evaluation & Performance Metrics
The classification model is rigorously evaluated using a hold-out test set ($20\%$ of the processed dataset):
* **Accuracy:** Evaluated and verified on test splits.
* **Precision & Recall:** Tracked per class (Authentic vs. Fake) to minimize false positives.
* **Confusion Matrix:** Implemented to measure true/false positives and negatives accurately.

---

## 🛠️ Tech Stack
* **Python**
* **Scikit-Learn** (for Vectorization and Logistic Regression Classification)
* **Pandas** (for Data Processing)
* **Streamlit** (for Web Interface Frontend and Deployment)

---

## ⚙️ Installation & Running Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/mayaralshahrani/Beauty-Tech-Fake-Review-Analyzer.git](https://github.com/mayaralshahrani/Beauty-Tech-Fake-Review-Analyzer.git)
   cd Beauty-Tech-Fake-Review-Analyzer
