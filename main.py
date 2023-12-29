import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the laptop dataset
@st.cache
def load_laptop_data():
    df = pd.read_csv('data/laptops.csv') # Load the dataset
    return df

# Configure Streamlit app
st.set_page_config(
    page_title="Laptops Data set",
    page_icon="💻",
    layout="wide",
)

# Load data
st.title("Laptops Data set")
with st.spinner("Loading data..."):
    laptops_df = load_laptop_data()

# Display the dataset and column information
st.header("Laptops Dataset")
st.info("Raw data in DataFrame")
st.dataframe(laptops_df, use_container_width=True)
st.success("Column information in the dataset")
cols = laptops_df.columns.tolist()
st.subheader(f'Total columns: {len(cols)} ⏩ {",".join(cols)}')

# Basic Data Visualization
st.header("Basic Data Visualization")

# Graph 1: Bar chart for Type of Laptops count
fig1 = px.bar(laptops_df['TypeOfLaptop'].value_counts(), x=laptops_df['TypeOfLaptop'].value_counts().index, y=laptops_df['TypeOfLaptop'].value_counts().values, labels={'x':'Laptop Type', 'y':'Count'})
fig1.update_layout(title='Laptop Types Distribution')
st.plotly_chart(fig1, use_container_width=True)

# Graph 2: Histogram for Laptop Screen Size (Inches)
fig2 = px.histogram(laptops_df, x='Inches', title='Histogram of Laptop Screen Sizes')
st.plotly_chart(fig2, use_container_width=True)

# Graph 3: Box plot for Laptop Prices
fig3 = px.box(laptops_df, y='Price', title='Box Plot of Laptop Prices')
st.plotly_chart(fig3, use_container_width=True)

# Graph 4: Scatter plot for RAM vs Price
fig4 = px.scatter(laptops_df, x='Ram', y='Price', title='Scatter Plot: RAM vs Price')
st.plotly_chart(fig4, use_container_width=True)

# Graph 5: Pie chart for Operating Systems distribution
fig5 = px.pie(laptops_df['OpSys'].value_counts(), values=laptops_df['OpSys'].value_counts().values, names=laptops_df['OpSys'].value_counts().index, title='Operating System Distribution')
st.plotly_chart(fig5, use_container_width=True)

# Graph 6: Line chart for Weight of Laptops
fig6 = px.line(laptops_df, x=laptops_df.index, y='Weight', title='Laptop Weights Over Index')
st.plotly_chart(fig6, use_container_width=True)

# Graph 7: Violin plot for Laptop Screen Resolution
fig7 = px.violin(laptops_df, y='ScreenResolution', title='Violin Plot of Laptop Screen Resolution')
st.plotly_chart(fig7, use_container_width=True)

# Graph 8: Bar chart for CPU count
fig8 = px.bar(laptops_df['Cpu'].value_counts(), x=laptops_df['Cpu'].value_counts().index, y=laptops_df['Cpu'].value_counts().values, labels={'x':'CPU Type', 'y':'Count'})
fig8.update_layout(title='CPU Types Distribution')
st.plotly_chart(fig8, use_container_width=True)

# Graph 9: Histogram for Laptop Memory
fig9 = px.histogram(laptops_df, x='Memory', title='Histogram of Laptop Memory')
st.plotly_chart(fig9, use_container_width=True)

# Graph 10: Bar chart for GPU count
fig10 = px.bar(laptops_df['Gpu'].value_counts(), x=laptops_df['Gpu'].value_counts().index, y=laptops_df['Gpu'].value_counts().values, labels={'x':'GPU Type', 'y':'Count'})
fig10.update_layout(title='GPU Types Distribution')
st.plotly_chart(fig10, use_container_width=True)






# about section
st.title("About this app")
st.write(
    """
    This app is for data visualization of the laptops dataset. 
    The dataset is from Kaggle and can be found [here](https://www.kaggle.com/ionaskel/laptop-prices).
    """
    **data visualization** is the presentation of data in a pictorial or graphical format.
    It enables decision makers to see analytics presented visually, so they can grasp difficult concepts or identify new patterns.
    With interactive visualization, you can take the concept a step further by using technology to drill down into charts and graphs for more detail, interactively changing what data you see and how it’s processed.
    """
    created by [MOHAMMAD FAZAL](
    github:
    linkedin:
    mail:
    """
)
)
