
import streamlit 
streamlit.title('Hello')
streamlit.header('First streamlit APP !')



import pandas

my_fruit_list = pandas.read_csv("fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
