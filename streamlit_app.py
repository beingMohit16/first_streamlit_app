import streamlit
import pandas
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
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# convert json file format into dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# display in a dataframe
streamlit.dataframe(fruityvice_normalized)






