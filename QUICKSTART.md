# Quick Start Guide

## ✅ What's Been Completed

Your **Retail Sales Analytics Dashboard** project is ready!

### Files in Repository:
- ✅ README.md - Professional documentation
- ✅ requirements.txt - Python dependencies  
- ✅ dashboard_app.py - Interactive Streamlit dashboard
- ✅ .gitignore - Python ignore rules

### 🔴 IMPORTANT: You Need to Add:
- ❌ data.xlsx - Your retail sales dataset

## 🚀 Next Steps

### 1. Upload Your Dataset
```bash
# Option A: Via GitHub Web
- Click "Add file" → "Upload files"
- Drag and drop your data.xlsx file
- Commit with message: "Add retail sales dataset"

# Option B: Via Git Command Line
git clone https://github.com/amith-1296/retail-sales-analytics-dashboard.git
cd retail-sales-analytics-dashboard
cp /path/to/your/data.xlsx .
git add data.xlsx
git commit -m "Add retail sales dataset"
git push origin main
```

### 2. Test Dashboard Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard_app.py
```

### 3. Deploy to Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - Repo: amith-1296/retail-sales-analytics-dashboard
   - Branch: main
   - File: dashboard_app.py
5. Click "Deploy!"
6. Get your live URL

### 4. Update README with Dashboard Link
Once deployed, edit README.md and replace:
```markdown
**👉 [Access Interactive Dashboard Here](#)**
```
With your actual Streamlit URL:
```markdown
**👉 [Access Interactive Dashboard Here](https://your-app.streamlit.app)**
```

## 📊 Dashboard Features

Your dashboard includes:
- ✅ 5 KPI cards (Revenue, Profit, AOV, Orders, Units)
- ✅ Interactive filters (Category, City, Customer Type)
- ✅ Sales & profit trend charts
- ✅ Top 10 products analysis
- ✅ City performance breakdown
- ✅ Category distribution pie chart
- ✅ Customer segment analysis

## 🛠️ Troubleshooting

### Dashboard won't load?
- Make sure data.xlsx is in the same folder as dashboard_app.py
- Check file name is exactly "data.xlsx" (case-sensitive)

### Streamlit deployment failed?
- Verify requirements.txt is in repository
- Make sure data.xlsx is uploaded
- Check Streamlit Cloud logs for errors

### Need to update dashboard?
- Edit dashboard_app.py directly on GitHub
- Or clone locally, make changes, and push

## 🎯 For Your Resume/LinkedIn

**Project Description:**
"Built an interactive retail sales analytics dashboard using Python, Streamlit, and Plotly. Analyzed 5,000+ transactions, created dynamic KPIs, and deployed live dashboard for stakeholder access. Demonstrated end-to-end data analysis, visualization, and dashboard development skills."

**Technologies:** Python | Streamlit | Plotly | Pandas | Data Visualization | Business Intelligence

## 📞 Need Help?

Contact: Amith D
- GitHub: @amith-1296
- Repository: https://github.com/amith-1296/retail-sales-analytics-dashboard
