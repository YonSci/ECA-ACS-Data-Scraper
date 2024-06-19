import streamlit as st

page_icon = "image/eca_logo.png"

st.set_page_config(
    page_title="Main Page",
    page_icon=page_icon,
    layout="centered" 
)


from app.Landing_Page import Landing_Page
from app.Data_Extraction_Page import Data_Extraction_Page
from app.Automation_Module import Automation_Module
from app.Help_Documentation import Help_Documentation
from app.About_Us import About_Us




def main():
    st.sidebar.title("Navigation Bar")
    
    pages = {
        "Landing Page": Landing_Page,
        "Data Extraction Module": Data_Extraction_Page,
        "Automation Module": Automation_Module,
        "Help Documentation": Help_Documentation,
        "About Us": About_Us

    
    }
    
    choice = st.sidebar.selectbox("Go to", list(pages.keys()))

    selected_page = pages[choice]()
    
if __name__ == "__main__":
    main()

    
 