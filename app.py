import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi"
}

source = st.selectbox("Source Language", languages.keys())
target = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation completed")
        st.text_area("Translated Text", translated)