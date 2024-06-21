import streamlit as st
from PIL import Image
import json
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import os


def Data_Extraction_Page():

    keywords = None

    
    st.title("Data Extraction Module 📊")


    st.markdown("---")


    st.markdown(""" 
                <div style="text-align: justify"> <p> Welcome to the Data Extraction Module!  This module is a comprehensive tool designed to facilitate the process of scraping publicly available  data from various African National Statistical Offices (NSOs) websites. This user-friendly module guides you through a step-by-step process, allowing you to: </p>


    🌐 **Select your data source**   
    🔍 **Customize scraping parameters**   
    💾 **Choose your desired output format**               
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("## Step 1: Choose Your Data Source 🌐")
    st.markdown("""
                <div style="text-align: justify"> <p> Select the National Statistical Office (NSO) website that holds the keys to the data you seek. You can choose from a list of African countries and the application gives the link of the website that opens in a new tab. </p>
    """, unsafe_allow_html=True)

    
    # Step 1: Mapping of African countries to their NSO websites
    # Load NSO websites from JSON file
    with open('nso_websites.json', 'r') as f:
        nso_websites = json.load(f)



    # Step 2: User selects a country
    country_options = [None] + list(nso_websites.keys())
    country = st.selectbox("Select an African NSOs website", country_options, index=0)

    # Step 3: Display the NSO website and provide a link

    if country is None:
        st.warning("Please select a country")
    else:
        website = nso_websites[country]
        st.info(f"URL for {country} : {website}")

 
    st.markdown("---")

    st.markdown("## Step 2: Select Dataset and Category🔍")
    st.markdown("""
                <div style="text-align: justify"> <p> 
                The user can select a dataset and one or more keywords related to the available dataset within the chosen NSO website. Based on these selections, the application displays URLs that correspond to the selected dataset and keyword combinations.
                </p>
    """, unsafe_allow_html=True)

    
    # Step 1: Define the available datasets
    datasets = [None,
                "Annual Statistical Abstract",
                "Demographics",
                "Environment",
                "Macro Economic",
                "National Standard Indicators",
                "Production",
                "Standards, Methods and Classifications"
                ]


    dataset = st.selectbox("Select Dataset", datasets, index=0)
    # Check if a dataset has been selected and display appropriate message
    if dataset is None:
        st.warning("Please select a dataset")
    else:
        st.info(f"Selected Dataset: {dataset}")
  
    # Step 2: Map each dataset to its keywords
    keywords_dict = {
        "Annual Statistical Abstract": ["Annual Statistical Abstract"],
        "Demographics": ["Population & Censuses", "Education", "Labour Market & Earnings", 
                    "Household Surveys", "Public Health", "Crime",
                      "Income, expenditure, poverty", "Governance", "Service Delivery",
                      "Gender"],
        "Environment": ["Land", "Climate", "Administrative Units", "Water Supply"],
        "Macro Economic": ["National Accounts", "External Trade", "Government Finance", 
                    "Banking and Currency", "Insurance", "Prices", "Key Economic Indicators"],

        "National Standard Indicators": ["Income", "Human Assets", "Economic Vulnerability"],
        "Production": ["Agriculture", "Energy", "Building and Construction", 
                    "Migration & Tourism", "Communication", "Transport", 
                    "Business & Industry", "Mining", "Uganda National Panel Surveys"],
        "Standards, Methods and Classifications": ["Standards, Methods and Classifications"]
        }
    
    if dataset:
        keywords = st.multiselect("Select Keywords", keywords_dict[dataset])


    # Step 4: Define a mapping from dataset and keyword to URLs
    url_map = {
        ('Annual Statistical Abstract', 'Annual Statistical Abstract'): 'https://www.ubos.org/explore-statistics/74/',
        ('Demographics', 'Population & Censuses'): 'https://www.ubos.org/explore-statistics/20/',
        ('Demographics', 'Education'): 'https://www.ubos.org/explore-statistics/21/',
        ('Demographics', 'Labour Market & Earnings'): 'https://www.ubos.org/explore-statistics/22/',
        ('Demographics', 'Household Surveys'): 'https://www.ubos.org/explore-statistics/23/',
        ('Demographics', 'Public Health'): 'https://www.ubos.org/explore-statistics/25/',
        ('Demographics', 'Crime'): 'https://www.ubos.org/explore-statistics/26/',
        ('Demographics', 'Income, expenditure, poverty'): 'https://www.ubos.org/explore-statistics/33/',
        ('Demographics', 'Governance'): 'https://www.ubos.org/explore-statistics/34/',
        ('Demographics', 'Service Delivery'): 'https://www.ubos.org/explore-statistics/36/',
        ('Demographics', 'Gender'): 'https://www.ubos.org/explore-statistics/67/',
        ('Environment', 'Land'): 'https://www.ubos.org/explore-statistics/14/',
        ('Environment', 'Climate'): 'https://www.ubos.org/explore-statistics/16/',
        ('Environment', 'Administrative Units'): 'https://www.ubos.org/explore-statistics/17/',
        ('Environment', 'Water Supply'): 'https://www.ubos.org/explore-statistics/18/',
        ('Macro Economic', 'National Accounts'): 'https://www.ubos.org/explore-statistics/9/',
        ('Macro Economic', 'External Trade'): 'https://www.ubos.org/explore-statistics/10/',
        ('Macro Economic', 'Government Finance'): 'https://www.ubos.org/explore-statistics/11/',
        ('Macro Economic', 'Banking and Currency'): 'https://www.ubos.org/explore-statistics/12/',
        ('Macro Economic', 'Insurance'): 'https://www.ubos.org/explore-statistics/13/',
        ('Macro Economic', 'Prices'): 'https://www.ubos.org/explore-statistics/30/',
        ('Macro Economic', 'Key Economic Indicators'): 'https://www.ubos.org/explore-statistics/64/',
        ('National Standard Indicators', 'Income'): 'https://www.ubos.org/explore-statistics/70/',
        ('National Standard Indicators', 'Human Assets'): 'https://www.ubos.org/explore-statistics/71/',
        ('National Standard Indicators', 'Economic Vulnerability'): 'https://www.ubos.org/explore-statistics/72/',
        ('Production', 'Agriculture'): 'https://www.ubos.org/explore-statistics/2/',
        ('Production', 'Energy'): 'https://www.ubos.org/explore-statistics/4/',
        ('Production', 'Building and Construction'): 'https://www.ubos.org/explore-statistics/5/',
        ('Production', 'Migration & Tourism'): 'https://www.ubos.org/explore-statistics/7/',
        ('Production', 'Communication'): 'https://www.ubos.org/explore-statistics/28/',
        ('Production', 'Transport'): 'https://www.ubos.org/explore-statistics/29/',
        ('Production', 'Business & Industry'): 'https://www.ubos.org/explore-statistics/32/',
        ('Production', 'Mining'): 'https://www.ubos.org/explore-statistics/65/',
        ('Production', 'Uganda National Panel Surveys'): 'https://www.ubos.org/explore-statistics/69/',
        ('Standards, Methods and Classifications', 'Standards, Methods and Classifications'): 'https://www.ubos.org/explore-statistics/39/'


    }

    keyword = None
    url = None

    # Step 5: Display the URL(s) based on selected dataset and keyword(s)
    if keywords:
        for keyword in keywords:
            url = url_map.get((dataset, keyword))
            if url:
                st.info(f"URL for {dataset} and {keyword}: {url}")

    else:
        # Prompt the user to select keywords if none are selected
        st.warning("Please select at least one keyword.")


    st.markdown("---")    
    st.markdown("## Step 3: Select the time range :calendar: ")
    
    # st.write("Please select the date range for the data you would like to download")
    col1, col2 = st.columns(2)  
  
    start_date = datetime(1985, 1, 1)
    end_date = datetime.now()

    col1, col2 = st.columns(2)  
    with col1:
        start_date = st.date_input("Start date:", min_value=start_date, max_value=end_date)
    with col2:
        end_date = st.date_input("End date:", min_value=start_date, max_value=end_date)


    st.info("You selected: " + str(start_date) + " to " + str(end_date))

    
    start_year = start_date.year
    end_year = end_date.year

    # st.info(f"Selected Time Range: {start_year} to {end_year}") 

    st.markdown("---")
    
    st.markdown("## Step 4: Choose the Data Format Type 💾")
    output_format = st.selectbox("Select Output Format", ["CSV", "Excel",  "PDF", "JSON"])
    if output_format == "CSV":
        data_format = '.csv'
    elif output_format == "Excel":
        data_format = '.xlsx'
    elif output_format == "PDF":
        data_format = '.pdf'
    elif output_format == "JSON":
        data_format = '.json'



    # Step 6: Analyze the URL and provide the user with the available data information
     
    if url is not None and keywords is not None and dataset is not None:

        # provided URL
        provided_url = website

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # st.write(soup)

        # Specific path you're interested in
        interested_path = "/statistics/"

        # interested_start_year = 2021
        # interested_end_year = 2024

        # user_specified_extensions = ['.xlsx']  # Example: User specifies only PDF files

        # Year range you're interested in
        interested_start_year = start_year
        interested_end_year = end_year
        # # st.write(start_year) 
        # # st.write(end_year)

        user_specified_extensions = data_format
        #st.write(data_format)


        # Function to convert relative URLs to absolute URLs
        def make_absolute(url, base_url=provided_url):
            return urljoin(base_url, url)

        # Parse the provided URL to extract the base URL
        parsed_url = urlparse(provided_url)
        # st.write(parsed_url)

        scheme = parsed_url.scheme
        # st.write(scheme)

        netloc = parsed_url.netloc
        # st.write(netloc)

        base_url = f"{scheme}://{netloc}"
        # st.write(base_url)


        def is_url_of_interest(href):
            if not href:
                return False
            absolute_href = make_absolute(href)
            if not absolute_href.startswith(base_url):
                return False
            path = urlparse(absolute_href).path
            if interested_path not in path:
                return False
            if not any(re.search(str(year), absolute_href) for year in range(interested_start_year, interested_end_year + 1)):
                return False
            if not any(absolute_href.endswith(ext) for ext in user_specified_extensions):
                return False
            return True

        # Use the function to filter URLs
        files = soup.find_all('a', href=is_url_of_interest)

        # Debugging print commented out
        # st.write(files)


        if files == None:
            st.warning("Data is not available for the selected periodn and file format.")
        else:

            # # Assuming 'files' is your list of BeautifulSoup Tag objects
            titles = [re.sub(r'[\d\._]+', '', file.text.strip()) for file in files]
            data_format = [file['href'].split('.')[-1] for file in files]

            time = []
            for file in files:
                text = file.text.strip()
                numbers = re.findall(r'\d+', text)
                if numbers:
                    time.append(numbers[-1])


            # # Create a dataframe with the columns
            df_scrap = pd.DataFrame({'Title': titles, 'Format': data_format, 'Time': time})

            # # Print the dataframe
            # st.write(df_scrap)


            # Example step to add 'Absolute_URL' to df_scrap (adjust according to your actual URL construction logic)
            absolute_urls = [file['href'] for file in files]  # Assuming 'href' contains the full URL
            df_scrap['Absolute_URL'] = absolute_urls

            # Now, create 'Clickable_Title' with the correct reference to 'Absolute_URL'
            df_scrap['Downloadable Title'] = df_scrap.apply(lambda row: f"<a href='{row['Absolute_URL']}' target='_blank'>{row['Title']}</a>", axis=1)

            df_scrap.drop(columns=['Absolute_URL'], inplace=True)


            # Print the dataframe
            st.write(df_scrap.to_html(escape=False), unsafe_allow_html=True)
    else:
        # Handle the case where one or more variables are None
        st.warning("Please ensure a dataset is selected and keywords are provided.")



if __name__ == "__main__":
    Data_Extraction_Page()
