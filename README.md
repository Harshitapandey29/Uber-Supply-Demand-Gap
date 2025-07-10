# 🚖 Uber Supply-Demand Gap Analysis

This repository presents an end-to-end data analysis project focused on identifying and visualizing the mismatch between customer ride requests and driver availability using real-world Uber data.

---

## 📌 Objective

Analyze ride request patterns and operational failures (like cancellations and driver shortages) to uncover insights that can improve Uber's service efficiency.

---

## 📁 Project Structure

Uber-Supply-Demand-Gap/
├── Cleaned_Uber_Supply_Demand.xlsx                     # Cleaned dataset with dashboards and pivot tables 
├── README.md                                           # This file  
├── UBER SUPPLY DEMAND GAP.ipynb                        # Python-based EDA and visualizations  
├── UBER SUPPLY DEMAND GAP.pdf                          # Final Presentation and report  
├── Uber Request Data.csv                               # Raw dataset 
├── ber_Sql_Insights.sql                                # Analytical queries for database-level insights
├── app.py                                              # Streamlit dashboard app  
├── requirements.txt                                    # Dependencies for the Streamlit app  
 

---

## 🚀 Pipeline Steps

### 📦 Data Preparation  
- Cleaned raw Uber ride request data  
- Derived columns: `request_hour`, `request_date`, etc.    

### 📊 Exploratory Analysis  
- Conducted in `UBER SUPPLY DEMAND GAP.ipynb` using Pandas, NumPy,  Seaborn, and Matplotlib  
- Visualizations: heatmaps, pie charts, bar plots, etc.

### 📈 Dashboard Deployment  
- Interactive dashboard built with **Streamlit**  
- Hosted for free using **Streamlit Cloud + GitHub**  

---

## 🔍 Insights

- **Rush Hour Gaps**: Largest supply-demand mismatches occur during 5–9 AM and 5–9 PM  
- **Pickup Trends**: Airports experience more driver shortages; cities see higher cancellations  
- **Trip Failures**: “No Cars Available” dominates failed trips in peak time blocks  

---

## 📈 Charts and Visualizations

- **Hourly Heatmap** – Request by hours and pickup point  
- **clean line chart** – demand variation across each hour of the day  
- **Bar Chart** – Gap by Time Slots and Pickup points  
- **Stacked Column Charts** – Cancellations and No Cars Available by Hour  

---

## 🧠 Recommendations

- Increase driver availability in peak slots (morning and evening)  
- Deploy additional drivers to airport during flight hours  
- Improve customer notifications to reduce cancellation impact  

---

## 📦 Dependencies

- Python 3.11  
- Streamlit  
- Pandas  
- Seaborn  
- Matplotlib  

## 🔗 Live Resources
🌐 Live Dashboard : https://uber-supply-demand-gap.streamlit.app/
