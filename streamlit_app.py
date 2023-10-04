#import Libraries
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

# For repetitive Api call 

def get_fruityvice_data (this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit you like information about? ','Kiwi')
  streamlit.write('The User entered ', fruit_choice)
  if not fruit_choice:
    streamset.error("Please select a fruit to get information : ")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
# display in a dataframe
  streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# Stoping below function to run anything past here while we troubleshoot
#Snowflake related functions



def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
      return my_cur.fetchall()

#Add Button to load fruit name
if streamlit.button('Get Fruit Load List '):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_row = get_fruit_load_list()
   streamlit.dataframe(my_data_row)

#Allow the End User to Add fruit to the list
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
      return "Thanks for adding "+new_fruit

add_my_fruit = streamlit.text_input("What fruit do you like to add? ")

if streamlit.button('Add a Fruit to the list '):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   
streamlit.stop()
streamlit.write("Thanks for inserting into: ")

#This will not work correctly, but just go with it now
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
