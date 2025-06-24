import streamlit as st
import pandas as pd
import json
import os
from app.data_loader import load_data

st.set_page_config(page_title="CleanTrain AI", layout="wide")
st.title("🧹 CleanTrain AI")
st.subheader("LLM eğitim verileri için akıllı temizlik ve JSONL çıktısı")

# Yüklenen veri
uploaded_file = st.file_uploader("📁 Veri dosyanızı yükleyin (.txt, .csv, .jsonl)", type=["txt", "csv", "jsonl"])

if uploaded_file:
    # Dosyayı geçici olarak kaydet
    temp_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        raw_data = load_data(temp_path)

        st.success(f"✅ {len(raw_data)} satır yüklendi.")
        st.dataframe(raw_data[:100] if isinstance(raw_data, list) else pd.DataFrame(raw_data).head(100))

        st.markdown("### 🔄 Bir sonraki adım: Veri temizleme")
        st.button("🚀 Temizlemeye Başla (yakında aktif)")

    except Exception as e:
        st.error(f"Hata oluştu: {str(e)}")

else:
    st.info("Lütfen bir .txt, .csv veya .jsonl dosyası yükleyin.")

