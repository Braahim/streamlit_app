import streamlit as st
import pandas
from urllib.error import URLError
import requests

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)


# API calls : 

def get_fruityvice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

    # normalize json response 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()
#streamlit.write('The user entered ', fruit_choice)




import snowflake.connector 

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
if 'my_cnx' not in streamlit.session_state:
  my_cur = st.session_state.my_cnx.cursor()
my_cur.execute("use warehouse pc_rivery_wh")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
st.header("The fruit list contains :")
st.dataframe(my_data_row)





def insert_row_snowflake(new_fruit):
  with st.session_state.my_cnx.cursor() as my_cur:
    #query = """ insert into fruit_load_list values %s """
    my_cur.execute("use warehouse pc_rivery_wh")
    my_cur.execute("insert into fruit_load_list values ( %s );", new_fruit)
    return "thanks for adding " + new_fruit
  
add_my_fruit = st.text_input("What fruit would you like to add ?")
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function)





















