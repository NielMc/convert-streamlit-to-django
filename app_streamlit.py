import streamlit as st
import numpy as np
import pandas as pd
import time


################ Agenda
# Display text
# display data
# display chart
# optimize performance
# Display widgets
# Display media
# Display progress and status


################################################################################
### Display text ###
################################################################################
# st.text('Field with  text')
# st.markdown('This is **markdown**, *is it?*')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('we will use this st.write() all the time!')
# st.write(['st', 'is <', 3])
# a = ['st', 'is <', 3]
# st.write("## Hello",a)
# st.write("* Hello")
# st.write("---")

# st.title('My title')
# st.header('My header')
# st.subheader('My sub')
# st.code('for i in range(8): foo()')




################################################################################
### Display data ###
################################################################################
df = pd.DataFrame(data={
                    "Col1":np.random.randint(low=-100,high=100,size=25),
                    "Col2":np.random.randint(low=25,high=80,size=25)
                    })


# st.write("* Using st.write()",df)
# st.write("* Using st.dataframe()")
# st.dataframe(df)
# st.write("* Using st.table()")
# st.table(df.iloc[0:10])
# st.write("* Using st.json()")
# st.json({'foo':'bar','fu':'ba'})



################################################################################
### Display charts ###
################################################################################
# st.write("* Line chart")
# st.line_chart(df)

# st.write("* Area chart")
# st.area_chart(df)

# st.write("* Stacked bar chart")
# st.bar_chart(df)

################################################################################
# Plot matplotlib, seaborn or plotly 
import matplotlib.pyplot as plt
import seaborn as sns

# st.write("* Matplotlib")
# fig, ax = plt.subplots()
# ax.hist(np.random.normal(10, 1, size=500,), bins=50)
# st.pyplot(fig)





# penguins = sns.load_dataset("penguins")
# st.write("* Seaborn",penguins)
# for col in penguins.select_dtypes(include="object").columns:
#     st.write(f"### {col}")
#     fig = sns.pairplot(data=penguins, hue=col)
#     st.pyplot(fig)



# st.write("* Plotly")
# penguins = sns.load_dataset("penguins")
# import plotly.express as px
# fig = px.scatter_3d(penguins.dropna(),x='bill_length_mm',y='bill_depth_mm',
#             z='body_mass_g',color='island',width=800,height=700)
# st.plotly_chart(fig)


# streamlit supports bokeh_chart, vega_lite_chart, altair_chart, pydeck_chart


# st.write("* Map")
# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [15, 10] + [53.41, -6.5],
#     columns=['lat', 'lon'])
# st.map(df)






################################################################################
### Optimize performance ###
################################################################################
# @st.cache
# def load_your_data():
#     return sns.load_dataset("penguins")

# df = load_your_data()
# # df =sns.load_dataset("penguins")

# st.write("* df", df)





################################################################################
### Display widgets ###
################################################################################
# st.button('Hit me')
# st.checkbox('Check me out')
# st.radio('Radio', [1,2,3])
# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.color_picker('Pick a color')
# st.write("---")


# list_of_sth = st.multiselect('list of sth', [1,2,3,4,5,6])
# st.write("* list_of_sth",list_of_sth)





penguins = sns.load_dataset("penguins")
hue_option =  st.selectbox(
    label='Select a variable',
    options=penguins.select_dtypes(include="object").columns)

if st.button(label="Pairplot"):
    fig = sns.pairplot(data=penguins, hue=hue_option)
    st.pyplot(fig)




# main_menu = st.sidebar.radio('Main Menu:', ['Option 1','Option 2','Option 3'])



################################################################################
### Display media ###
################################################################################

# col1, col2 = st.beta_columns(2)
# with col1:
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
# with col2:
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=355)

# st.audio(data="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav",)
# st.video(data="https://www.youtube.com/watch?v=g4Vp_P9d6O4&list=RDg4Vp_P9d6O4&start_radio=1")





################################################################################
### Display progress and status ###
################################################################################
import time
# my_bar = st.progress(0)
# for x in np.arange(0,101,10):
#     time.sleep(0.1)
#     my_bar.progress(int(x))


# st.spinner()
# with st.spinner(text='Your request is in progress...'):
#     time.sleep(5)
#     st.success('Done')
#     st.balloons()



# st.error(df)
# st.warning('Warning message')
# st.info('Info message')
# st.success('Success message')

# try:
#     sum= 1/0
# except Exception as e:
#     st.exception(e)

