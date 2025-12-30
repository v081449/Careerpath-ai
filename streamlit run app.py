import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🤖",
    layout="centered"
)

# ---------------- LINKS ----------------
WEBSITE_LINK = "https://sites.google.com/view/career-adda/home"
YOUTUBE_LINK = "https://youtube.com/@careerbyvaibhav"
INSTAGRAM_LINK = "https://www.instagram.com/careeraddaai"
FACEBOOK_LINK = "https://www.facebook.com/share/17kQ1rBd9d/"

# ---------------- HEADER ----------------
st.title("🤖 CareerPath AI")
st.subheader("AI Based Career Guidance System")
st.write("Select your interest, skill and education to get career guidance.")

st.markdown("---")

# ---------------- INPUTS ----------------
interest = st.selectbox(
    "🎯 Select Your Interest",
    ["Technology", "Design", "Business", "Medical", "Arts"]
)

skill = st.selectbox(
    "🧠 Select Your Skill",
    ["Coding", "Creativity", "Communication", "Biology", "Writing"]
)

education = st.selectbox(
    "🎓 Education Level",
    ["12th Pass", "Graduate", "Post Graduate"]
)

st.markdown("---")

# ---------------- BUTTON ----------------
if st.button("🚀 Get Career Suggestion"):
    if interest == "Technology" and skill == "Coding":
        career = "Software Developer / AI Engineer"
        required = "Python, AI, Machine Learning"

    elif interest == "Design":
        career = "UI / UX Designer"
        required = "Figma, Design Principles"

    elif interest == "Business":
        career = "Marketing / Management"
        required = "Communication, Strategy"

    elif interest == "Medical":
        career = "Nursing / Lab Technician"
        required = "Biology, Practical Training"

    else:
        career = "Content Writer / Journalist"
        required = "Writing, Research"

    # -------- RESULT (BIG & BEAUTIFUL) --------
    st.success("✅ Career Suggestion Ready")

    st.markdown(f"""
## 🎯 Career Suggestion
**{career}**

## 🧠 Required Skills
{required}

## 🎓 Education Level
{education}
""")

    # -------- WEBSITE BUTTON --------
    st.markdown("### 🌐 Visit Our Website")
    st.markdown(f"[👉 Click here to open Career Website]({WEBSITE_LINK})")

# ---------------- SIDEBAR (BEST PLACE FOR LINKS) ----------------
st.sidebar.title("🌐 Connect With Us")

st.sidebar.markdown(f"""
🌍 **Website**  
[Career Adda]({WEBSITE_LINK})

▶️ **YouTube**  
[Career by Vaibhav]({YOUTUBE_LINK})

📸 **Instagram**  
[careeraddaai]({INSTAGRAM_LINK})

📘 **Facebook**  
[Career Adda]({FACEBOOK_LINK})
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2025 CareerPath AI | Built with Python & Streamlit")
