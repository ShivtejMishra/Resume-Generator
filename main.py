import streamlit as st
from resume_generator import generate_pdf
from ai_enhancement import enhance_summary

st.set_page_config(page_title="AI-Powered Resume Builder", layout="wide")
st.title("AI-Powered Resume Builder")
st.write("Fill in your details and generate a professional resume.")

# User Input Fields
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")
    website = st.text_input("Website")
with col2:
    summary = st.text_area("Professional Summary")
    skills = st.text_area("Skills (comma-separated)")
    experience = st.text_area("Experience")

# Education Details
st.subheader("Education")

# High School
with st.expander("High School (1-10th)"):
    high_school_name = st.text_input("High School Name")
    col1, col2 = st.columns([2, 1])
    with col1:
        high_school_percentage = st.text_input("10th Grade Percentage")

# Junior College
with st.expander("Junior College (11-12th)"):
    junior_college_name = st.text_input("Junior College Name")
    col1, col2 = st.columns([2, 1])
    with col1:
        junior_college_percentage = st.text_input("12th Grade Percentage")

# Bachelor's Degree
with st.expander("Bachelor's Degree"):
    bachelor_college_name = st.text_input("Bachelor's College Name")
    bachelor_branch = st.text_input("Bachelor's Branch Name")
    col1, col2 = st.columns(2)
    with col1:
        bachelor_start_date = st.date_input("Start Date", key="b_start_date")
    with col2:
        bachelor_passout_date = st.date_input("Pass Out Date", key="b_passout_date")

# Master's Degree
with st.expander("Master's Degree"):
    master_college_name = st.text_input("Master's College Name")
    master_branch = st.text_input("Master's Branch Name")
    col1, col2 = st.columns(2)
    with col1:
        master_start_date = st.date_input("Start Date", key="m_start_date")
    with col2:
        master_passout_date = st.date_input("Pass Out Date", key="m_passout_date")

# PhD
with st.expander("PhD"):
    phd_college_name = st.text_input("PhD College Name")
    col1, col2 = st.columns(2)
    with col1:
        phd_start_date = st.date_input("Start Date", key="phd_start_date")
    with col2:
        phd_passout_date = st.date_input("Pass Out Date", key="phd_passout_date")

if st.button("Enhance and Generate Resume"):
    # AI Enhancement for summary (optional)
    enhanced_summary = enhance_summary(summary)
    st.write("Enhanced Professional Summary:")
    st.write(enhanced_summary)

    # Prepare education details for PDF
    education_details = f"High School: {high_school_name} | 10th Percentage: {high_school_percentage}%\n"
    education_details += f"Junior College: {junior_college_name} | 12th Percentage: {junior_college_percentage}%\n"
    education_details += f"Bachelor's: {bachelor_college_name}, {bachelor_branch} | {bachelor_start_date} - {bachelor_passout_date}\n"
    education_details += f"Master's: {master_college_name}, {master_branch} | {master_start_date} - {master_passout_date}\n"
    education_details += f"PhD: {phd_college_name} | {phd_start_date} - {phd_passout_date}\n"

    # Generate PDF
    generate_pdf(name, email, phone, address, website, summary, skills, experience, education_details)
    with open("resume_output.pdf", "rb") as pdf_file:
        st.download_button("Download Resume", data=pdf_file, file_name="resume.pdf", mime="application/pdf")
