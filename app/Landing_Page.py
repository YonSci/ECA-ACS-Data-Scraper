import streamlit as st
from PIL import Image

def Landing_Page():
    display1 = Image.open('image/eca_logo.png')


    col1, col2 = st.columns((3, 7))
    with col1:
        st.image(display1, width=190)
    with col2:
        st.markdown("<h2 style='text-align: left; color: blue; font-family: Arial, sans-serif;'>ACS-Data-Scraper</h2>", unsafe_allow_html=True)

    st.header("Welcome to ACS Web Scraping Application") 

    
    st.markdown("""
    <div style="text-align: justify; color: #333;">
    <p><strong style="color: #007BFF;">ECA-ACS-Data-Scraper</strong> is designed to streamline the data extraction process from the National Statistical Offices websites that are publicly available. The application is tailored to meet the specific needs of users who require access to public data for research, analysis, and decision-making purposes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Key Features")
    features = [
        ("Intuitive and Interactive User Interface", "Navigate with ease using our user-friendly interface. Whether you're a seasoned data analyst or a novice, our application simplifies the data extraction process, making it accessible for everyone."),
        ("Clear and Organized Data Presentation", "The application ensures that the extracted data is presented in a clear, organized manner, enabling you to quickly make sense of the information and derive valuable insights."),
        ("Robust Error Handling", "The application is equipped with advanced error handling mechanisms, ensuring a smooth and reliable data collection process."),
        ("Save and Export Options", "Save or export the scraped data in your preferred format, allowing you to seamlessly integrate it into your workflows and analyses."),
        ("Scheduled and Automated Web Scraping", "The application allows you to schedule and automate the web scraping process, ensuring you always have the latest data without manual intervention.")
    ]

    for feature, description in features:
        with st.expander(feature):
            st.markdown(description)

    st.markdown("---")
    st.markdown('<p style="text-align: center; color: gray;">Copyright @2024 ECA-ACS-Data-Scraper</p>', unsafe_allow_html=True)
    st.markdown("---")

if __name__ == "__main__":
    Landing_Page()