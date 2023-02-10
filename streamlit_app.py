import streamlit
streamlit.title('New Healthy Diner')
streamlit.header('Menu')
streamlit.text('item-1')
streamlit.text('item-2')
streamlit.text('item-3')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import Pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
