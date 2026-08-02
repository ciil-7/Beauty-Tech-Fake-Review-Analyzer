import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. توليد قاعدة بيانات تدريب واسعة داخل الكود
base_authentic = [
    "I've been using this serum with Niacinamide for two weeks and my skin feels hydrated.",
    "After 10 days of applying this cream, my pores look slightly better, good product.",
    "Noticed some mild improvements in my skin texture after a month of daily use.",
    "Good packaging and gentle on my sensitive skin, used it for 3 weeks.",
    "The bottle lasted a month, nice hydration though a bit pricey.",
    "Decent moisturizer, didn't break me out, but results take time.",
    "Applied it every night for a month. Texture is nice, standard results.",
    "It took around three weeks to see any noticeable difference in my dry skin."
]

base_fake = [
    "MIRACLE product!! Changed my life overnight, 100% cure for everything, buy it NOW!",
    "Absolute magic! Best ever cream in the whole universe, perfection in a bottle!",
    "Best product ever created! Instant results on day one, total perfection!",
    "Unbelievable miracle cream, cured all my skin problems instantly! AMAZING!",
    "Get rid of wrinkles in 2 seconds! Best miracle formula ever made, buy 10 now!",
    "Total perfection, glowing skin in one single application, absolute magic!",
    "Buy this right now or regret it forever! Life-changing miraculous potion!",
    "Unreal results within minutes! The greatest beauty secret ever discovered!"
]

texts = (base_authentic * 50) + (base_fake * 50)
labels = (["authentic"] * len(base_authentic) * 50) + (["fake"] * len(base_fake) * 50)

# 2. تقسيم البيانات لتدريب واختبار النموذج
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 3. تدريب نموذج تعلم الآلة
ml_model = make_pipeline(
    TfidfVectorizer(max_features=1000, ngram_range=(1, 2)), 
    LogisticRegression(C=1.0, max_iter=500)
)
ml_model.fit(X_train, y_train)

# 4. حساب مقاييس الأداء
y_pred = ml_model.predict(X_test)
model_accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, output_dict=True)

def get_model_evaluation_metrics():
    return {
        "accuracy": round(model_accuracy * 100, 2),
        "confusion_matrix": conf_matrix.tolist(),
        "classification_report": class_report
    }

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
            "reason": f"Machine Learning model detected high promotional hype patterns with {confidence}% confidence based on trained classification pipeline."
        }
    else:
        return {
            "is_authentic": True,
            "confidence": confidence,
            "reason": f"Machine Learning model verified authentic linguistic patterns with {confidence}% confidence."
        }

def analyze_ingredients(text):
    """
    استخراج المكونات النشطة ديناميكياً من ملف ingredients.csv الخارجي
    """
    text_lower = text.lower()
    detected = {}
    
    # مسار ملف الـ CSV الخارجي
    csv_path = "ingredients.csv"
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            ing_name = str(row['ingredient']).strip()
            ing_benefit = str(row['benefit']).strip()
            
            if ing_name.lower() in text_lower:
                detected[ing_name] = ing_benefit
    else:
        # احتياطياً في حال لم يُوجد الملف
        fallback_db = {
            "Niacinamide": "Brightens skin, minimizes pore appearance, and regulates oil production.",
            "Hyaluronic Acid": "Deeply hydrates and plumps the skin by retaining moisture."
        }
        for ing, ben in fallback_db.items():
            if ing.lower() in text_lower:
                detected[ing] = ben
                
    return detected
