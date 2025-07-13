import streamlit as st
from coding_data import coding_questions


# --- Background Image with Strong Blur ---
page_bg_blur = """
<style>
/* Background image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    position: relative;
}

/* Blur overlay */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    backdrop-filter: blur(12px);  /* Increased from 6px to 12px */
    background-color: rgba(0,0,0,0.3);  /* Optional: subtle dark overlay */
    z-index: -1;
}

/* Clean header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}

.css-10trblm, .stMarkdown, .stTextInput > div > div > input {
    color: white !important;
    font-weight: 500;
}
</style>
"""

st.markdown(page_bg_blur, unsafe_allow_html=True)
# --- Title & Input ---
st.title("🧠 Coding Practice Chatbot")
st.markdown("Ask me a coding question:")
user_input = st.text_input("")
st.caption(
    "Try typing things like 'prime', 'palindrome', or 'greatest of 3 numbers'")


# --- Download Button Function ---
def generate_download_button(code_str, filename):
    st.download_button(
        label="📥 Download Code",
        data=code_str,
        file_name=filename,
        mime="text/plain"
    )


# --- Chatbot Logic ---
if user_input:
    found = False
    for question, code in coding_questions.items():
        if user_input.lower() in question.lower():
            st.subheader(f"Here's your answer for: {question}")
            st.code(code, language='python')
            filename = f"{question.replace(' ', '_').lower()}.py"
            generate_download_button(code, filename)
            found = True
            break
    if not found:
        st.warning(
            "❌ Sorry, I don't know that yet. Try asking for 'Palindrome' or 'Prime number check'.")
