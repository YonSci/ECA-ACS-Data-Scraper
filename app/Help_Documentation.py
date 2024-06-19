import streamlit as st

def Help_Documentation():
    st.header("Help Documentation")

    st.markdown("""
    <div style="text-align: justify; color: #333;">
    <p>The Help Documentation provides detailed information on how to use the ACS Web Scraping Application. Whether you're a first-time user or an experienced data analyst, this guide will help you navigate the application's features and functionalities with ease.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Table of Contents")
    st.markdown("""
    1. [User Guides and Tutorials](#user-guides-and-tutorials)
    2. [FAQs](#faqs)
    3. [External Resources](#external-resources)
    """)




if __name__ == "__main__":
    Help_Documentation()