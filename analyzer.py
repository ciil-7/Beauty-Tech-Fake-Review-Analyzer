import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# توسيع بيانات التدريب لتمثل نماذج حقيقية وموسعة للمراجعات
training_data = [
    # مراجعات حقيقية (Authentic)
    ("I've been using this serum with Niacinamide for two weeks and my skin feels hydrated.", "authentic"),
    ("After 10 days of applying this cream, my pores look slightly better, good product.", "authentic"),
    ("Noticed some mild improvements in my skin texture after a month of daily use.", "authentic"),
    ("Good packaging and gentle on my sensitive skin, used it for 3 weeks.", "authentic"),
    ("The bottle lasted a month, nice hydration though a bit pricey.", "authentic"),
    ("Decent moisturizer, didn't break me out, but results take time.", "authentic"),
    ("Applied it every night for a month. Texture is nice, standard results.", "authentic"),
    ("It took around three weeks to see any noticeable difference in my dry skin.", "authentic"),
    
    # مراجعات مزيفة / مبالغ فيها (Fake / Hype)
    ("MIRACLE product!! Changed my life overnight, 100% cure for everything, buy it NOW!", "fake"),
    ("Absolute magic! Best ever cream in the whole universe, perfection in a bottle!", "fake"),
    ("Best product ever created! Instant results on day one, total perfection!", "fake"),
    ("Unbelievable miracle cream, cured all my skin problems instantly! AMAZING!", "fake"),
    ("Get rid of wrinkles in 2 seconds! Best miracle formula ever made, buy 10 now!", "fake"),
    ("Total perfection, glowing skin in one single application, absolute magic!", "fake")
]

texts = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

# بناء نموذج تعلم الآلة مع تحسين الكشف عبر n-grams
ml_model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2)), 
    LogisticRegression()
)
ml_model.fit(texts, labels)

def analyze_review(text):
    if not text or not text.strip():
        return {
            "is_authentic": True,
            "confidence": 80,
            "reason": "Please provide a valid review text for analysis."
        }
    
    prediction = ml_model.predict([text])[0]
    probabilities = ml_model.predict_proba([text])[0]
    confidence = round(max(probabilities) * 100, 1)
    
    if prediction == "fake":
        return {
            "is_authentic": False,
            "confidence": confidence,
            "reason": f"Machine Learning model detected high promotional hype patterns with {confidence}% confidence based on trained dataset."
        }
    else:
        return {
            "is_authentic": True,
            "confidence": confidence,
            "reason": f"Machine Learning model verified authentic linguistic patterns with {confidence}% confidence."
        }

def analyze_ingredients(text):
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
