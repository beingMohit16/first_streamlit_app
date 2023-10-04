import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Test = Title ')

streamlit.header('Test = Header')
streamlit.text('Test = Text')
streamlit.text('Test2 = Text1')
streamlit.text('Test3 = Text2')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')
selected_fruits = streamlit.multiselect("Pick Some Fruits: ", list(fruit_list.index),['Apple','Banana'])
fruits_to_show = fruit_list.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

#for display fruitsvice api response

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit you like information about? ','Kiwi')
  streamlit.write('The User entered ', fruit_choice)
  if not fruit_choice:
    streamset.error("Please select a fruit to get information : ")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# Convert JSON file format into dataframe
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display in a dataframe
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

# don't run anything past here while we troubleshoot
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("The Fruit List Contains: ")
streamlit.dataframe(my_data_row)

streamlit.write("Thanks for inserting into: ")

#This will not work correctly, but just go with it now
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
