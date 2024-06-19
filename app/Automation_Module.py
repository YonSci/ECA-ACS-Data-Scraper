import streamlit as st

def Automation_Module():
    st.header("🤖 Scheduled Tasks and Automation")

    st.markdown("""
    <div style="text-align: justify; color: #333;">
    <p>The Automation Module is designed to streamline the data extraction process by allowing users to schedule and automate web scraping tasks. This feature is particularly useful for users who need to regularly collect data from the same source at specific intervals. This module is used to set up and manage automated scraping tasks, ensuring that you always have the latest data without manual intervention.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Key Features")
    features = [
        ("Scheduled Web Scraping", "Schedule web scraping tasks to run at specific times or intervals, ensuring you always have the latest data without manual intervention (daily, weekly, monthly)."),
        ("Automated Data Extraction", "Automate the data extraction process, saving you time and effort by eliminating the need for manual data collection."),
        ("Customizable Settings", "Customize the scheduling and automation settings to meet your specific requirements, allowing you to tailor the process to your needs."),
        ("Error Handling and Notifications", "Receive notifications and alerts in case of errors or issues during the web scraping process, ensuring you are always informed."),
        ("Toggle to enable or disable automation", "Enable or disable the automation feature for individual tasks, giving you full control over the data extraction process.")
    ]

    for feature, description in features:
        with st.expander(feature):
            st.markdown(description)



if __name__ == "__main__":
    Automation_Module()
  