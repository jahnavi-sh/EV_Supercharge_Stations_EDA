#load libraries 
import numpy as np 
import pandas as pd 
import plotly.express as py 

#load data into pandas dataframe 
df = pd.read_csv(r"supercharge_locations.csv", encoding='latin-1')

#view the first fove rows of the dataframe 
df.head()

#The data consists of following columns or features 
#1. ID - A unique identifier assigned to each Supercharge location
#2. Name - The name or title associated with the Supercharge location
#3. Address - The physical address of the Supercharge location, including street name, city, state, and ZIP code
#4. Latitude - The geographical latitude coordinate of the Supercharge location
#5. Longitude - The geographical longitude coordinate of the Supercharge location
#6. Type - The type or category of the Supercharge location, such as "Urban" or "Suburban"
#7. Status - The current operational status of the Supercharge location, whether it is "Active," "Planned," or "Under Construction"
#8. Stalls - The number of charging stalls available at the Supercharge location
#9. Power (kW) - The power rating in kilowatts (kW) provided by the Supercharger
#10. Phone Number - The contact phone number associated with the Supercharge location
#11. Website - The website URL for additional information about the Supercharge location
#12. City - The city where the Supercharge location is situated 
#13. State - The state or region where the Supercharge location is situated 
#14. ZIP - The ZIP code associated with the Supercharge location 
#15. Country - The country where the Supercharge location is situated

#View the total number of rows and columns 
df.shape 

#There are 5876 rows (5875 data points) and 12 columns (12 features)

fig = py.bar(df, x='Country', color='Country',title='Countries with most Supercharge Stations')
fig.show()

#As we see from the graph - USA and Japan have the highest number of locations of Supercharge Stations 

#Check USA data 
usa_df = df[df['Country'] == 'USA']

#view data 
usa_df.head()

df[['Latitude', 'Longitude']] = df['GPS'].str.split(', ', expand=True).astype(float)

# Create the USA map plot
fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name='Supercharger',
                        hover_data=['Street Address', 'City', 'State', 'Zip'],
                        color_discrete_sequence=['blue'], zoom=3, height=600)

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(title_text='Supercharger Locations in the USA')
fig.update_layout(margin={'r': 0, 't': 30, 'l': 0, 'b': 0})

# Display the plot
fig.show()