import re

# قاعدة بيانات المكونات التجميلية وفوائدها
INGREDIENTS_DB = {
    "niacinamide": "Soothes redness and improves skin texture",
    "hyaluronic acid": "Deeply hydrates and plumps the skin",
    "salicylic acid": "Unclogs pores and controls acne",
    "retinol": "Promotes cell turnover and reduces wrinkles",
    "vitamin c": "Brightens complexion and fades dark spots",
    "glycolic acid": "Gently exfoliates dead skin cells",
    "ceramides": "Restores and strengthens the natural skin barrier"
}

# الكلمات المفتاحية الترويجية المشبوهة
SPAM_KEYWORDS = [
    "magic", "100%", "miracle", "guaranteed", "buy now", 
    "click here", "best product everrrr", "instant results", "shocking"
]

def analyze_ingredients(text):
    """استخراج المكونات الفعالة الموجودة في النص مع شرح فوائدها"""
    text_lower = text.lower()
    found_ingredients = {}
    for ingredient, benefit in INGREDIENTS_DB.items():
        if ingredient in text_lower:
            found_ingredients[ingredient.title()] = benefit
    return found_ingredients

def analyze_review(text):
    """تحليل موثوقية المراجعة وكشف الاحتيال"""
    if not text or len(text.strip()) < 10:
        return {
            "is_authentic": False,
            "confidence": 0,
            "reason": "Text is too short to accurately analyze."
        }
    
    text_lower = text.lower()
    spam_score = 0
    
    # حساب النقاط بناءً على الكلمات الترويجية
    for kw in SPAM_KEYWORDS:
        if kw in text_lower:
            spam_score += 2
            
    # كشف الأحرف المكررة بكثرة (مثل: everrrr!)
    if re.search(r'(.)\1{3,}', text_lower):
        spam_score += 2
        
    # كشف المبالغة في علامات التعجب
    if text.count('!') > 3:
        spam_score += 1

    is_authentic = spam_score < 2
    confidence = max(60, 100 - (spam_score * 20))
    
    reason = "Normal feedback pattern detected." if is_authentic else "High frequency of promotional keywords or exaggeration."
    
    return {
        "is_authentic": is_authentic,
        "confidence": confidence,
        "spam_score": spam_score,
        "reason": reason
    }
