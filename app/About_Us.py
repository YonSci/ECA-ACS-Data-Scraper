import streamlit as st

def About_Us():

    st.header("About Us")
    st.markdown("""
    <div style="text-align: justify; color: #333;">
    <p><strong style="color: #007BFF;">ECA-ACS-Data-Scraper</strong> is designed to streamline the data extraction process from the National Statistical Offices websites that are publicly available. The application is tailored to meet the specific needs of users who require access to public data for research, analysis, and decision-making purposes. This page could provide information about the developers or organization behind the ACS-Data-Scraper. It could include:</p>
    </div>
    """, unsafe_allow_html=True)


    features = [
        ("Mission and goals of the project", "The mission and goals of the ACS-Data-Scraper project, including the purpose of the application and the target audience."),
        ("Contact information for feedback or suggestions", " Contact information for users to provide feedback, suggestions, or report issues with the application."),
       
    ]

    for feature, description in features:
        with st.expander(feature):
            st.markdown(description)







    



if __name__ == "__main__":
    About_Us()