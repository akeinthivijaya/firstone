from library import *
import pandas as pd
import streamlit as st


#Title
st.title('Covid-19 Visulaization Dashboard')
st.caption('Made By Team Python Troopers')

#image
from PIL import Image
image = Image.open('R.jpg')

st.image(image)

#what is covid

st.subheader('What is Covid 19')
st.caption('COVID-19 is a new strain of coronavirus that has not been previously identified in humans. The COVID-19 is the cause of an outbreak of respiratory illness first detected in Wuhan, Hubei province, China. Since December 2019, cases have been identified in a growing number of countries.')

#countries and the picture codes
countries = ['Sri Lanka', 'UK', 'USA', 'Japan', 'China', 'Australia', 'Uganda', 'Qatar', 'India', 'Iceland', 'Malaysia', 'Italy', 'Germany', 'South Korea', 'Russia', 'Spain', 'Mexico', 'Indonesia', 'Turkey', 'Argentina', 'Sweden', 'Thailand', 'Iran', 'Brazil', 'Egypt', 'Israel', 'Singapore', 'Colombia', 'South Africa','Pakistan', 'Bangladesh', 'Chilie', 'Finland', 'Portugal', 'Peru', 'Vietnam', 'New Zealand', 'Greece', 'Austria', 'Philippiens', 'Malawi', 'Madagascar', 'Maldives', 'Denmark', 'Iraq', 'Chad', 'Palau', 'Panama']
country_codes = {'Sri Lanka':'LK', 'UK':'GB', 'USA':'US', 'Japan':'JP', 'China':'CN', 'Australia':'AU', 'Uganda':'UG', 'Qatar':'QA', 'India':'IN', 'Iceland':'IS', 'Malaysia':'MY', 'Italy':'IT', 'Germany':'DE', 'South Korea':'KR', 'Russia':'RU', 'Spain': 'ES', 'Mexico':'MX', 'Indonesia':'ID', 'Turkey':'TR', 'Argentina':'AR', 'Sweden':'SE', 'Thailand':'TH', 'Iran':'IR', 'Brazil':'BR', 'Egypt':'EG', 'Israel':'IL', 'Singapore':'SG', 'Colombia':'CO', 'South Africa':'ZA','Pakistan':'PK', 'Bangladesh':'BD', 'Chilie':'CL', 'Finland':'FI', 'Portugal':'PT', 'Peru':'PE', 'Vietnam':'VN', 'New Zealand':'NZ', 'Greece':'GR', 'Austria':'AT', 'Philippiens':'PH', 'Malawi':'MW', 'Madagascar':'MG', 'Maldives':'MV', 'Denmark': 'DK', 'Iraq':'IQ', 'Chad':'TD', 'Palau' : 'PW', 'Panama' : 'PA'}


#data types
data_types = ['cases','deaths','recoveries']

#select box
country = st.sidebar.selectbox('What is your country',countries)

#slider
days = st.sidebar.slider('days', min_value=1, max_value=90, value=30, step=1)

#multiselect box
data_type = st.sidebar.multiselect('Pick Data Types', data_types)

#total cases
total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))

total_df = pd.concat([total_deaths, total_cases, total_recoveries],axis=1).astype(int)

#daily cases
daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))

daily_df = pd.concat([daily_deaths, daily_cases, daily_recoveries],axis=1).astype(int)

#yesterday cases
yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

#image infront the selected country 
st.image (f"https://www.countryflagicons.com/FLAT/64/{country_codes[country]}.png")

#st.metrics
st.metric('Selected Country', country)
st.metric('Total Cases', yesterday_cases)
st.metric('Total Recoveries', yesterday_recoveries)
st.metric('Total Deaths', yesterday_deaths)

#Daily cases line chart
st.line_chart(daily_df[data_type])
st.bar_chart(daily_df[data_type])

from PIL import Image
image = Image.open('V.jpg')

st.image(image, caption='Take the Vaccine')

#Vaccine information 
st.subheader('•Covid 19 Vaccine')
st.caption('COVID-19 vaccines are safe, effective, and free! After you’ve been fully vaccinated, you can participate in many of the activities that you did prior to the pandemic.')

#covid 19 symptoms
st.subheader('•Covid 19 Symptoms')
st.caption('• Fever')
st.caption('• Cough')
st.caption('• Loosing Taste or Smell')
st.caption('• Stortnes of Breath')
st.caption('• Headache')
st.caption('• Sneezing')
st.caption('• Sore Throat')
st.caption('• Running Nose')
st.caption('• Chest Pain')

#video file
st.subheader('Get Vaccinated & Stay Safe')
video_file = open('covid_video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

import time

my_bar = st.sidebar.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

#mask protection against covid 19

st.header('Mask protection against Covid 19')

st.subheader('Fabric/cloth masks:')
from PIL import Image
image = Image.open('F 2.png')

st.image(image)

st.caption('Fabric or cloth masks trap droplets that are released when the person wearing the mask sneezes, coughs or talks. They reduce the spread of viruses, are easy to purchase or make, and can be washed and worn again. It’s also important for the wearer to avoid touching their masks, and if they do, to sanitize or wash their hands after. Additionally, if a cloth or fabric mask becomes wet or dirty, it’s important to switch to a clean one. These masks should not be shared.')

st.subheader('Surgical masks:')
from PIL import Image
image = Image.open('S.png')

st.image(image)
st.caption('Surgical masks — also called medical masks — are loose-fitting and disposable. They protect the nose and mouth from coming into contact with droplets that could carry germs. They’re made to protect you from sprays or splashes that could enter the nose or mouth. These masks are also able to filter out large particles in the air, and can make sure droplets from the wearer aren’t being spread. These masks are single-use only.')

st.subheader('N95 masks:')
from PIL import Image
image = Image.open('K.png')

st.image(image)
st.caption('N95 masks provide a higher degree of protection than a surgical mask or cloth mask because they can filter out both large and small particles when the wearer breathes. They’re called KN95 masks because they’re designed to block 95% of particles or liquids that may come in contact with your face. However, these masks are not for general public use and should be reserved for healthcare workers and other medical first responders. They’re also incompatible with children or people with facial hair. Healthcare providers are fit tested for these masks, and like surgical masks, they’re intended to be single-use only, though researchers are examining effective ways to clean these masks.')
