import streamlit
import pandas
import requests
from urllib.error import URLError
streamlit.title('🥑bulid your own fruit soomthie🥣')

streamlit.header('🥣 Breakfast menu')
streamlit.text('🥗omega 3 & blueberry oatemai')
streamlit.text('🐔omelt & offoil')
streamlit.text('🥑hard-boiled')

#import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:",list( my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)   
streamlit.stop()
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("the furit load list contains")
streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("the furit load list contains")
streamlit.text(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choice)

my_cur.execute("insert into fruit_load_list values('from streamlit')")

streamlit.header("Fruityvice Fruit Advice!") 
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice: streamlit.error("Please select a fruit to get information.")
  
  else:
      back_from_function = get_fruityvice_data(fruit_choice) 
      streamlit.dataframe(back_from_fuction)
except URLError as e:
  steramlit.error()
