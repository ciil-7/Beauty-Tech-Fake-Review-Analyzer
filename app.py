import streamlit as st
from analyzer import analyze_review, analyze_ingredients, get_model_evaluation_metrics

# إعدادات صفحة Streamlit
st.set_page_config(
    page_title="Beauty-Tech Fake Review Analyzer",
    page_icon="✨",
    layout="centered"
)

# عنوان التطبيق والوصف
st.title("✨ Beauty-Tech Fake Review Analyzer")
st.markdown("Evaluate the authenticity of cosmetic product reviews and extract active skincare ingredients using a supervised Machine Learning pipeline.")

st.markdown("---")

# إدخال المراجعة من المستخدم
st.subheader("📝 Enter Product Review")
user_review = st.text_area(
    "Type or paste a cosmetic review below:",
    placeholder="e.g., I've been using this serum with Niacinamide for two weeks and my skin feels hydrated...",
    height=120
)

if st.button("Analyze Review", type="primary"):
    if not user_review.strip():
        st.warning("⚠️ Please enter a valid review text before analyzing.")
    else:
        with st.spinner("Analyzing review and extracting ingredients..."):
            # 1. تحليل صحة المراجعة
            review_result = analyze_review(user_review)
            
            # 2. استخراج المكونات النشطة
            ingredients_result = analyze_ingredients(user_review)
            
        st.markdown("---")
        
        # عرض النتائج في أعمدة متجاورة
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔍 Authenticity Result")
            if review_result["is_authentic"]:
                st.success("✅ **Authentic Review**")
            else:
                st.error("🚨 **Potential Fake / Hype Review**")
            
            st.metric(label="Confidence Score", value=f"{review_result['confidence']}%")
            st.info(review_result["reason"])
            
        with col2:
            st.subheader("🧪 Active Ingredients")
            if ingredients_result:
                for ing, benefit in ingredients_result.items():
                    st.markdown(f"**- {ing}:** {benefit}")
            else:
                st.info("No major active cosmetic ingredients detected in this specific text.")

# قسم تقييم وأداء النموذج (Model Performance Metrics)
st.markdown("---")
with st.expander("📊 View Machine Learning Model Performance Metrics"):
    metrics = get_model_evaluation_metrics()
    
    st.write(f"**Model Accuracy on Test Split:** `{metrics['accuracy']}%`")
    st.write("**Confusion Matrix (Test Set):**")
    st.code(str(metrics['confusion_matrix']))
    st.markdown("The model uses a supervised **Logistic Regression** classifier powered by **TF-IDF** feature extraction, evaluated on a hold-out test set.")
