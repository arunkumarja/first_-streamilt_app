import streamlit
streamlit.title('My parents new health diner')

streamlit.header('🥣 Breakfast menu')
streamlit.text('🥗omega 3 & blueberry oatemai')
streamlit.text('🐔omelt & offoil')
streamlit.text('🥑hard-boiled')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:",list( my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
