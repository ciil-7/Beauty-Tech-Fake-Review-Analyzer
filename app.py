import streamlit as st
import pandas as pd
from analyzer import analyze_review, analyze_ingredients

# إعدادات الصفحة
st.set_page_config(
    page_title="Beauty-Tech Review Analyzer",
    page_icon="💄",
    layout="wide"
)

# القائمة الجانبية (Sidebar)
st.sidebar.image("https://img.icons8.com/color/96/sparkling.png", width=60)
st.sidebar.title("Beauty-Tech AI")
st.sidebar.write("Advanced Fraud Detection & Cosmetic Ingredient Parser.")
st.sidebar.divider()
st.sidebar.info("💡 **Tip:** Real reviews usually include specific product experience details rather than extreme hype.")

# العنوان الرئيسي
st.title("💄 Beauty-Tech Fake Review & Ingredient Analyzer")
st.caption("AI-Powered Platform for E-Commerce Authenticity & Cosmetic Ingredient Insights")

st.divider()

# تقسيم الشاشة إلى تبويبات (Tabs)
tab1, tab2 = st.tabs(["🔍 Analyze Single Review", "📊 Batch CSV Analysis"])

# --- التبويب الأول: تحليل مراجعة واحدة ---
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_input = st.text_area(
            "Enter Product Review Text:", 
            placeholder="e.g., I've been using this serum with Niacinamide and Salicylic Acid for two weeks, my skin feels hydrated!",
            height=150
        )
        analyze_btn = st.button("🚀 Run AI Analysis", type="primary", use_container_width=True)
        
    if analyze_btn:
        if user_input.strip():
            results = analyze_review(user_input)
            ingredients = analyze_ingredients(user_input)
            
            with col2:
                st.subheader("📊 Result Breakdown")
                if results["is_authentic"]:
                    st.success("✅ **Authentic Review**")
                else:
                    st.error("⚠️ **Suspicious / Fake Review**")
                
                # عرض مؤشرات
                st.metric(label="AI Confidence Score", value=f"{results['confidence']}%")
                st.caption(f"**Details:** {results['reason']}")
            
            st.divider()
            
            # عرض المكونات المستخرجة
            st.subheader("🧪 Detected Active Ingredients")
            if ingredients:
                for ing, benefit in ingredients.items():
                    st.info(f"✨ **{ing}**: {benefit}")
            else:
                st.write("No specific active ingredients detected from the database list.")
        else:
            st.warning("Please input review text before clicking analyze.")

# --- التبويب الثاني: تحليل ملف كامل ---
with tab2:
    st.subheader("📁 Bulk Dataset Analysis")
    st.write("Preview sample batch dataset or upload your custom Excel/CSV.")
    
    try:
        df = pd.read_csv("data/reviews.csv")
        st.dataframe(df, use_container_width=True)
    except Exception:
        st.info("No sample data found in `data/reviews.csv`.")
