import streamlit as st
import pandas as pd
from analyzer import analyze_review

# إعدادات الصفحة
st.set_page_config(page_title="Beauty-Tech Review Analyzer", page_icon="💄", layout="centered")

# العنوان والرأس
st.title("💄 Beauty-Tech Fake Review & Ingredient Analyzer")
st.write("An AI-driven system to detect fraudulent reviews and analyze active cosmetic ingredients.")

st.divider()

# مدخل النص من المستخدم
user_input = st.text_area("Enter Product Review Text:", placeholder="e.g., This serum with Niacinamide helped hydrate my skin!")

if st.button("🔍 Analyze Review", type="primary"):
    if user_input.strip():
        # استدعاء دالة التحليل
        is_authentic = analyze_review(user_input)
        
        st.subheader("📊 Analysis Results:")
        if is_authentic:
            st.success("✅ Authentic Review - The review appears legitimate.")
        else:
            st.error("⚠️ Suspicious / Fake Review - High probability of promotional or bot-generated content.")
    else:
        st.warning("Please enter a review text first.")

st.divider()

# عرض عينة البيانات من المجلد
st.subheader("📁 Dataset Sample (`data/reviews.csv`)")
try:
    df = pd.read_csv("data/reviews.csv")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.info("Upload `data/reviews.csv` to view dataset samples here.")
