
import streamlit 
streamlit.title('Hello')
streamlit.header('First streamlit APP !')



import pandas

my_fruit_list = pandas.read_csv("fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)
