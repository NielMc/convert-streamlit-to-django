import streamlit as st
import numpy as np
import pandas as pd
import datetime

# Display text
# display data
# display chart
# optmize performance
# Display widgets


################################################################################
### Display text ###
################################################################################
# st.text('Field with  text')
# st.markdown('This is **markdown**, *is it?*')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('You will use this function all the time!')
# st.write(['st', 'is <', 3])
# st.write("## Hello")
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




# st.write("* Seaborn")
# penguins = sns.load_dataset("penguins")
# for col in penguins.select_dtypes(include="object").columns:
#     st.write(f"### {col}")
#     fig = sns.pairplot(data=penguins, hue=col)
    # st.pyplot(fig)



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
@st.cache
def load_your_data():
    return sns.load_dataset("penguins")

df = load_your_data()
st.write("* df", df)

################################################################################
### Display widgets ###
################################################################################



################################################################################
### Display media ###
################################################################################


# st.image('./header.png')
# st.audio(data)
# st.video(data)

# st.title("Form for the Users")
# st.write("Here, you can answer to some questions in this form.")

# user_id = st.text_input("ID", value="Your ID", max_chars=7)
# info = st.text_area("Share some information about you", "Put information here",
#                     help='You can write about your hobbies or family')
# age = st.number_input("Age", min_value=18, max_value=100, step=1)
# birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1),
#                            max_value=datetime.date(2003, 12, 31))
# smoke = st.checkbox("Do you smoke?")
# genre = st.radio("Which movie genre do you like?",
#                  options=['horror', 'adventure', 'romantic'])
# weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
# physical_form = st.selectbox("Select level of your physical condition",
#                              options=["Bad", "Normal", "Good"])
# colors = st.multiselect('What are your favorite colors',
#                         options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])
# image = st.file_uploader("Upload your photo", type=['jpg', 'png'])

# col1, col2 = st.beta_columns(2)
# with col1:
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
#     st.button("Like cats")
# with col2:
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
#     st.button("Like dogs")

# submit = st.button("Submit")

# if submit:
#     st.write("You submitted the form")

# click = st.sidebar.button('Click me!')
# if click:
#     st.sidebar.write("You clicked the button")
