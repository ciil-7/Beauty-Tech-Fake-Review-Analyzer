# Beauty-Tech Fake Review Analyzer

A robust Streamlit web application designed to evaluate the authenticity of cosmetic product reviews and extract active skincare ingredients using a supervised Machine Learning pipeline.

## 🚀 Features
* **Review Authenticity Detection:** Analyzes review text to detect unauthentic, overly promotional, or fake hype patterns.
* **Probabilistic Confidence Scoring:** Computes statistical confidence metrics (`predict_proba`) for transparent reliability evaluation.
* **Active Ingredient Extraction:** Automatically identifies active cosmetic ingredients (such as Niacinamide, Hyaluronic Acid, Retinol, etc.) mentioned in the review and lists their clinical skin benefits.
* **Interactive UI:** Built with Streamlit for a fast, responsive, and user-friendly experience.

---

## 📊 Model Architecture & Methodology
The application evaluates review authenticity using a supervised **Machine Learning pipeline** rather than complex generative AI models:
* **Feature Extraction:** Utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** with unigrams and bigrams (`ngram_range=(1, 2)`) to capture individual words and contextual phrase patterns (such as marketing hype vs. regular speech).
* **Classification Algorithm:** Powered by a **Logistic Regression** classifier trained on a balanced corpus of authentic and unauthentic review samples.
* **Confidence Estimation:** Generates probabilistic confidence scores to provide transparent and quantifiable reliability metrics for each analysis.

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
