# 📊 Retail Sales Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An **interactive executive dashboard** for retail sales analytics built with Python, Streamlit, and Plotly. This project demonstrates end-to-end data analysis skills including data cleaning, exploratory data analysis (EDA), KPI tracking, and interactive visualization.

## 🎯 Project Overview

This project analyzes retail sales transaction data to uncover business insights and trends. The dashboard enables stakeholders to:
- Track key performance indicators (KPIs) in real-time
- Identify top-performing products, cities, and customer segments  
- Analyze sales trends and seasonality patterns
- Examine operational metrics like shipping modes and order priorities
- Filter data dynamically for customized analysis

## 🚀 Live Dashboard

**👉 [Access Interactive Dashboard Here](https://retail-sales-analytics-dashboard-tjp3djeprdlfqnkemm2jew.streamlit.app/)**
## 🛠️ Tech Stack

- **Python 3.8+** - Core programming language
- **Streamlit** - Interactive web application framework
- **Plotly** - Interactive visualizations  
- **Pandas** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Statistical visualizations

## 📊 Key Features

### Interactive Filters
- Date range selector
- Product category filter
- City/location filter  
- Customer type filter
- Shipping mode filter

### KPI Cards
- Total Revenue
- Total Profit
- Average Order Value
- Total Orders
- Units Sold

### Visualizations
- 📈 Monthly sales and profit trends (line charts)
- 🏆 Top 10 products by sales (bar charts)
- 🌆 Top cities performance analysis
- 📦 Product category distribution (pie charts)
- 👥 Customer segment analysis
- 🚚 Shipping mode breakdown  
- ⚡ Order priority distribution
- 💰 Discount usage analysis (boxplots)
- 🔍 Profit outlier tables

## 📁 Project Structure

```
retail-sales-analytics-dashboard/
├── notebooks/
│   └── retail_sales_analysis.ipynb    # Jupyter notebook with full EDA
├── dashboard/  
│   └── dashboard_app.py                # Streamlit dashboard application
├── data/
│   └── data.xlsx                       # Raw sales transaction data
├── requirements.txt                    # Python dependencies
└── README.md                          # Project documentation
```

## 🔧 Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/amith-1296/retail-sales-analytics-dashboard.git
cd retail-sales-analytics-dashboard
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Run the Dashboard Locally
```bash
cd dashboard
streamlit run dashboard_app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Run the Jupyter Notebook
```bash
jupyter notebook notebooks/retail_sales_analysis.ipynb
```

## 📈 Analysis Highlights

### Key Insights Discovered:
- **Sydney** is the top-performing city with ₹2.67M in sales
- **Corporate customers** drive the highest revenue (₹1.35M)
- **Office Supplies** category dominates with 78% of total sales  
- **Cando PC940 Copier** is the best-selling product (₹703K)
- Average discount rate is **5%** across all orders
- **Regular Air shipping** is preferred for 85% of orders

### Business Recommendations:
1. Focus marketing efforts on Sydney and Melbourne markets
2. Develop loyalty programs for corporate customer segment
3. Optimize inventory for top 10 products to prevent stockouts
4. Review pricing strategy for low-margin products  
5. Investigate high-value order patterns for upselling opportunities

## 📚 Dataset

The dataset contains **5,000+ retail transactions** with the following features:
- Order details (Order No, Date, Priority)
- Customer information (Name, Type, Location)
- Product details (Name, Category, Container)  
- Financial metrics (Cost, Retail Price, Profit, Discounts)
- Shipping information (Mode, Ship Date, Costs)

## 🎓 Skills Demonstrated

- **Data Cleaning & Preprocessing**: Handling currency formats, date parsing, missing values
- **Exploratory Data Analysis (EDA)**: Statistical analysis, trend identification  
- **Data Visualization**: Creating interactive and static charts
- **Dashboard Development**: Building user-friendly interfaces with Streamlit
- **Business Intelligence**: Translating data into actionable insights
- **Python Programming**: Pandas, Plotly, Matplotlib, Seaborn
- **Version Control**: Git and GitHub

## 📞 Contact

**Amith D**
- GitHub: [@amith-1296](https://github.com/amith-1296)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile)  
- Portfolio: [View my work](https://amith-1296.github.io/Amith.github.io/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

This project was created as part of my data analytics portfolio to demonstrate end-to-end business intelligence capabilities.

---

⭐ **If you found this project helpful, please consider giving it a star!**
