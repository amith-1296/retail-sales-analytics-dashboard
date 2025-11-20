import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide", page_icon="📊")

st.title("📊 Retail Sales Analytics Dashboard")
st.markdown("**Interactive Executive Dashboard for Business Intelligence**")
st.markdown("---")

@st.cache_data
def load_data():
    def clean_money(val):
        if pd.isnull(val): 
            return None
        return float(str(val).replace('$', '').replace(',', ''))
    
    df = pd.read_csv('data.csv')
    
    money_cols = ['Cost Price', 'Retail Price', 'Profit Margin', 'Sub Total', 
                  'Discount $', 'Order Total', 'Shipping Cost', 'Total']
    for col in money_cols:
        df[col] = df[col].apply(clean_money)
    
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Year-Month'] = df['Order Date'].dt.to_period('M').astype(str)
    
    return df

df = load_data()

st.sidebar.header("🔍 Filters")

categories = ['All'] + list(df['Product Category'].unique())
selected_category = st.sidebar.selectbox("Product Category", categories)

cities = ['All'] + list(df['City'].unique())
selected_city = st.sidebar.selectbox("City", cities)

customer_types = ['All'] + list(df['Customer Type'].unique())
selected_customer = st.sidebar.selectbox("Customer Type", customer_types)

filtered_df = df.copy()
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['Product Category'] == selected_category]
if selected_city != 'All':
    filtered_df = filtered_df[filtered_df['City'] == selected_city]
if selected_customer != 'All':
    filtered_df = filtered_df[filtered_df['Customer Type'] == selected_customer]

st.header("📈 Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Revenue", f"₹{filtered_df['Order Total'].sum():,.0f}")
with col2:
    st.metric("Total Profit", f"₹{filtered_df['Profit Margin'].sum():,.0f}")
with col3:
    st.metric("Avg Order Value", f"₹{filtered_df['Order Total'].mean():,.0f}")
with col4:
    st.metric("Total Orders", f"{filtered_df['Order No'].nunique():,}")
with col5:
    st.metric("Units Sold", f"{filtered_df['Order Quantity'].sum():,}")

st.markdown("---")

st.header("📉 Sales & Profit Trends")
trends = filtered_df.groupby('Year-Month').agg({'Order Total':'sum', 'Profit Margin':'sum'}).reset_index()

fig_trends = go.Figure()
fig_trends.add_trace(go.Scatter(x=trends['Year-Month'], y=trends['Order Total'], name='Total Sales', mode='lines+markers'))
fig_trends.add_trace(go.Scatter(x=trends['Year-Month'], y=trends['Profit Margin'], name='Total Profit', mode='lines+markers'))
fig_trends.update_layout(height=400, xaxis_title="Month", yaxis_title="Amount (₹)")
st.plotly_chart(fig_trends, use_container_width=True)

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🏆 Top 10 Products")
    top_products = filtered_df.groupby('Product Name')['Order Total'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_products, y='Product Name', x='Order Total', orientation='h', color='Order Total')
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("🌆 Top Cities")
    top_cities = filtered_df.groupby('City')['Order Total'].sum().sort_values(ascending=False).head(10).reset_index()
    fig2 = px.bar(top_cities, x='City', y='Order Total', color='Order Total')
    fig2.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

with col_right:
    st.subheader("📦 Category Distribution")
    category_sales = filtered_df.groupby('Product Category')['Order Total'].sum().reset_index()
    fig3 = px.pie(category_sales, values='Order Total', names='Product Category')
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("👥 Customer Segments")
    segment_sales = filtered_df.groupby('Customer Type')['Order Total'].sum().reset_index()
    fig4 = px.bar(segment_sales, x='Customer Type', y='Order Total', color='Order Total')
    fig4.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.markdown("**Created by Amith D** | [GitHub](https://github.com/amith-1296)")
