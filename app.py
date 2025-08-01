import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Sales Dashboard')
st.header('Interactive Sales Dashboard 📊')

# Read and parse the data
df = pd.read_csv('Online Sales Data.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Ensures proper datetime parsing

st.write(df)

# Sidebar filters
st.sidebar.header('Filter data 🔍')
region_filter = st.sidebar.multiselect('Select regions', options=df['Region'].unique(), default=df['Region'].unique())
product_filter = st.sidebar.multiselect('Select product', options=df['Product Category'].unique(), default=df['Product Category'].unique())

# Apply filters
filtered_df = df[(df['Region'].isin(region_filter)) & (df['Product Category'].isin(product_filter))]

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    total_sales = filtered_df["Total Revenue"].sum()
    st.metric('Total Revenue', f'${total_sales:.2f}')
with col2:
    avg_sales = filtered_df["Total Revenue"].mean()
    st.metric('Average Revenue', f'${avg_sales:.2f}')
with col3:
    total_product = df["Product Name"].nunique()
    st.metric("Total Products", f'{total_product}')

# Tabs
tab1, tab2, tab3 = st.tabs(["Sales by Product 📊", "Sales by Region 📶", "📉 Temporal Trends"])

# Tab 1: Product-based charts
with tab1:
    st.subheader('Sales by Product')
    fig1 = px.bar(filtered_df, x='Product Category', y='Total Revenue', color='Product Category')
    st.plotly_chart(fig1)

    st.subheader("Unit Price Distribution (Histogram)")
    fig6 = px.histogram(filtered_df, x='Unit Price', nbins=5, color='Product Category', title="Distribution of Unit Price")
    st.plotly_chart(fig6)

# Tab 2: Region-based charts
with tab2:
    st.subheader('Sales by Region')
    fig2 = px.pie(filtered_df, names='Region', values='Total Revenue', title='Sales by Region')
    st.plotly_chart(fig2)

    st.subheader('Revenue vs Unit Price (Scatter Plot)')
    fig3 = px.scatter(filtered_df, x='Unit Price', y="Total Revenue", color='Product Category',
                      size='Unit Price', hover_data=['Region'],
                      title="Total Revenue vs Unit Price")
    st.plotly_chart(fig3)

    st.subheader("Revenue Distribution by Product Category (Box Plot)")
    fig4 = px.box(filtered_df, x='Product Category', y='Total Revenue', color='Product Category',
                  title='Revenue Distribution by Product Category')
    st.plotly_chart(fig4)

# Tab 3: Time-based trends
with tab3:
    st.subheader("Total Revenue Over Time (Line Chart)")
    fig5 = px.line(filtered_df, x='Date', y='Total Revenue', title="Revenue Trends Over Time")
    st.plotly_chart(fig5)

    st.subheader("Revenue Area Chart Over Time")
    fig7 = px.area(filtered_df, x='Date', y='Total Revenue', title='Revenue Area Chart Over Time')
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("3D Line Plot: Date vs Unit Price vs Revenue")
    fig8 = px.line_3d(filtered_df, x='Date', y='Unit Price', z='Total Revenue', title="3D Revenue Trends Over Time")
    st.plotly_chart(fig8)
