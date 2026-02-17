import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("STREAMLIT")
st.write("Hello World!!")

#interactive table
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#normal static table
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


#interactive table
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)


#using styler to add more interctive to df

dataframe = pd.DataFrame(
    np.random.rand(10,20),
    columns=('col %d' %i  for i in range(20))
)

st.write(dataframe.style.highlight_max(axis=0))


st.line_chart(dataframe)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#widgetssss

#slider
x = st.slider('Slider')

st.write(x, 'Squared is', x*x)

#checkbox:
if st.checkbox("show input box"):
    #input
    if 'name' not in st.session_state:
        st.session_state.name = ''
    st.text_input("You name :", key = 'name')

    st.write(st.session_state.name)
    


#select box 
df = pd.DataFrame({
    'first_col' : [ '',1,2,3,4],
    'second_col' : ['' ,10,20,30,40]
})

option = st.selectbox(
    "what is your favourite number?",
    df['first_col']
)

st.write("Your choosen Fav number is ", option)


# layout 

st.sidebar.title("Hello")

add_slider = st.sidebar.slider('Your Age : ',  0.0, 100.0, (25.0, 75.0))

st.sidebar.write("My age is between : ",add_slider)


# st.echo and st.spinner are not currently supported inside the sidebar or layout options. 
# Rest assured, though, we're currently working on adding support for those too!


left_col , right_col = st.columns(2)

left_col.button('Press Me')

with right_col:
    chosen = st.radio('fav color',('black','white','blue','pink'))
    st.write(f"My fav color is {chosen}")


# progress
st.write('Starting long process....')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration  {i+1}')
    bar.progress(i+1)
    time.sleep(0.5)

'...now we are done'




# # Define the pages
# main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
# page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
# page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# # Set up navigation
# pg = st.navigation([main_page, page_2, page_3])

# # Run the selected page
# pg.run()