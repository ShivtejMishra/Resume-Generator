import streamlit as st
from resume_generator import generate_pdf
from ai_enhancement import enhance_summary

st.title("AI-Powered Resume Builder")
st.write("Fill in your details and generate a professional resume.")

# User Input Fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
address = st.text_input("Address")
website = st.text_input("Website")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Experience")
education = st.text_area("Education")

if st.button("Enhance and Generate Resume"):
    # AI Enhancement for summary (optional)
    enhanced_summary = enhance_summary(summary)
    st.write("Enhanced Professional Summary:")
    st.write(enhanced_summary)

    # Generate PDF
    generate_pdf(name, email, phone, address, website, summary, skills, experience, education)
    with open("resume_output.pdf", "rb") as pdf_file:
        st.download_button("Download Resume", data=pdf_file, file_name="resume.pdf", mime="application/pdf")
