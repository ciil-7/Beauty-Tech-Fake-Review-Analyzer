import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# 1. تجهيز بيانات تدريب ذكية (Training Dataset) لنموذج الـ Machine Learning
training_data = [
    # مراجعات حقيقية (Authentic)
    ("I've been using this serum with Niacinamide for two weeks and my skin feels hydrated.", "authentic"),
    ("After 10 days of applying this cream, my pores look slightly better, good product.", "authentic"),
    ("Noticed some mild improvements in my skin texture after a month of daily use.", "authentic"),
    ("Good packaging and gentle on my sensitive skin, used it for 3 weeks.", "authentic"),
    ("The bottle lasted a month, nice hydration though a bit pricey.", "authentic"),
    
    # مراجعات مزيفة / مبالغ فيها (Fake / Hype)
    ("MIRACLE product!! Changed my life overnight, 100% cure for everything, buy it NOW!", "fake"),
    ("Absolute magic! Best ever cream in the whole universe, perfection in a bottle!", "fake"),
    ("Best product ever created! Instant results on day one, total perfection!", "fake"),
    ("Unbelievable miracle cream, cured all my skin problems instantly! AMAZING!", "fake")
]

texts = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

# 2. بناء وتدريب نموذج تعلم الآلة (ML Pipeline: TF-IDF + Logistic Regression)
ml_model = make_pipeline(TfidfVectorizer(), LogisticRegression())
ml_model.fit(texts, labels)

def analyze_review(text):
    """
    تحليل نص المراجعة باستخدام نموذج تعلم الآلة (Machine Learning Classifier)
    مبني عبر scikit-learn لتصنيف النص بدقة.
    """
    if not text or not text.strip():
        return {
            "is_authentic": True,
            "confidence": 80,
            "reason": "Please provide a valid review text for analysis."
        }
    
    # التنبؤ بواسطة نموذج الـ ML
    prediction = ml_model.predict([text])[0]
    probabilities = ml_model.predict_proba([text])[0]
    
    # حساب نسبة الثقة بناءً على مخرجات النموذج الاحتمالية
    max_prob = max(probabilities) * 100
    confidence = round(max_prob, 1)
    
    if prediction == "fake":
        return {
            "is_authentic": False,
            "confidence": confidence,
            "reason": "Machine Learning model detected high promotional hype patterns characteristic of unauthentic reviews."
        }
    else:
        return {
            "is_authentic": True,
            "confidence": confidence,
            "reason": "Machine Learning model verified natural language patterns and authentic review tone."
        }

def analyze_ingredients(text):
    """
    استخراج المكونات التجميلية النشطة وفوائدها من نص المراجعة
    """
    text_lower = text.lower()
    ingredients_db = {
        "niacinamide": "Brightens skin, minimizes pore appearance, and regulates oil production.",
        "salicylic acid": "Exfoliates inside pores, targets acne, and reduces blackheads.",
        "hyaluronic acid": "Deeply hydrates and plumps the skin by retaining moisture.",
        "retinol": "Boosts cell turnover, reduces fine lines, and improves skin texture.",
        "vitamin c": "Powerful antioxidant that brightens skin tone and fades dark spots.",
        "ceramides": "Restores and strengthens the natural skin barrier."
    }
    
    detected = {}
    for ingredient, benefit in ingredients_db.items():
        if ingredient in text_lower:
            detected[ingredient.title()] = benefit
            
    return detected
