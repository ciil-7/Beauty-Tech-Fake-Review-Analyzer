import re

# قاعدة بيانات مصغرة لمكونات التجميل الشهيرة ووظائفها
INGREDIENTS_DB = {
    "retinol": "Anti-aging / Wrinkles",
    "niacinamide": "Brightening / Pore control",
    "hyaluronic acid": "Hydration / Moisture",
    "salicylic acid": "Acne treatment / Exfoliation",
    "vitamin c": "Glow / Antioxidant"
}

# كلمات وتراكيب مشبوهة تكثر في المراجعات المزيفة
SPAM_KEYWORDS = [
    "100% magic", 
    "miracle", 
    "buy now", 
    "click here", 
    "best product everrrr", 
    "guaranteed"
]

def analyze_review(review_text):
    print(f"\n--- Analyzing Review ---")
    print(f"Text: \"{review_text}\"")
    
    # 1. كشف المراجعات المزيفة (Fake/Spam Detection)
    spam_score = 0
    text_lower = review_text.lower()
    
    for word in SPAM_KEYWORDS:
        if word in text_lower:
            spam_score += 1

    # التقييم يعتبر مشكوك فيه لو احتوى على كلمات ترويجية متطرفة أو كان قصيرًا جدًا ومبالغًا فيه
    is_fake = spam_score > 0 or len(review_text.split()) < 3
    status = "⚠️ Suspicious / Fake Review" if is_fake else "✅ Authentic Review"
    
    # 2. استخراج المكونات الكيميائية وتحليلها (Ingredient Extraction)
    found_ingredients = []
    for ingredient, benefit in INGREDIENTS_DB.items():
        if ingredient in text_lower:
            found_ingredients.append(f"{ingredient.title()} ({benefit})")

    # طباعة النتائج في الشاشة
    print(f"Status: {status}")
    if found_ingredients:
        print("Detected Active Ingredients:", ", ".join(found_ingredients))
    else:
        print("Detected Active Ingredients: None found in database.")
    
    return not is_fake

# تشغيل تجريبي للكود (Demo execution)
if __name__ == "__main__":
    sample_review_1 = "This serum with Niacinamide and Hyaluronic Acid is good for hydration."
    sample_review_2 = "100% magic best product everrrr buy now!!"
    
    analyze_review(sample_review_1)
    analyze_review(sample_review_2)
