# 💄 Beauty-Tech Fake Review & Ingredient Analyzer

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Release](https://img.shields.io/badge/Release-v1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An AI-powered web application designed to analyze e-commerce product reviews for authenticity, detect potential spam/fraudulent content, and automatically extract key active cosmetic ingredients with their skincare benefits.
---

## ✨ Key Features

- **🛡️ Fake Review Detection**: Identifies aggressive promotional patterns, keyword stuffing, and suspicious repetitive characters.
- **🧪 Active Ingredient Parser**: Detects popular cosmetic active ingredients (e.g., *Niacinamide*, *Salicylic Acid*, *Retinol*) and highlights their skincare benefits.
- **📊 Interactive Streamlit UI**: Offers a clean user experience with single-text analysis and bulk CSV data views.
- **⚡ Fast & Lightweight**: Zero complex external API dependencies—runs efficiently offline or locally.

---

## 🛠️ Project Structure

```text
Beauty-Tech-Fake-Review-Analyzer/
├── app.py              # Main Streamlit web application
├── analyzer.py         # AI analysis logic & ingredient detection DB
├── requirements.txt    # Project dependencies
├── data/               # Sample review datasets (CSV)
├── examples/           # Sample API/JSON input formats
└── screenshots/        # Application screenshots and demo assets
