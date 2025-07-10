import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up page
st.set_page_config(page_title="Uber Supply-Demand Gap", layout="wide")
st.title("🚖 Uber Supply-Demand Gap Analysis")

# Load data
df = pd.read_excel("Cleaned_Uber_Supply_Demand.xlsx")

# Show summary
st.subheader("🔍 Summary Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Requests", df.shape[0])
col2.metric("Completed", df[df['Status'] == 'Trip Completed'].shape[0])
col3.metric("Cancelled", df[df['Status'] == 'Cancelled'].shape[0])
col4.metric("No Cars Available", df[df['Status'] == 'No Cars Available'].shape[0])

# Time plot
if 'Request hour' in df.columns:
    st.subheader("🕒 Ride Requests by Hour")
    hourly = df.groupby('Request hour')['Status'].count()
    st.line_chart(hourly)

# Heatmap
if {'Request hour', 'Request day'}.issubset(df.columns):
    st.subheader("📅 Heatmap: Requests by Day & Hour")
    heatmap_data = pd.crosstab(df['Request day'], df['Request hour'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt="d", ax=ax)
    st.pyplot(fig)

# Pickup points
st.subheader("📍 Pickup Point Distribution")
pickup_counts = df['Pickup point'].value_counts()
st.bar_chart(pickup_counts)

# Failure analysis
st.subheader("❌ Trip Failures")
failures = df[df['Status'] != 'Trip Completed']['Status'].value_counts()
fig2, ax2 = plt.subplots()
failures.plot(kind='bar', color='salmon', ax=ax2)
ax2.set_ylabel("Count")
st.pyplot(fig2)

# Recommendations
st.subheader("💡 Recommendations")
st.markdown("""
- Increase drivers during **rush hours (5–9 AM, 5–9 PM)**
- Allocate more drivers to **Airport**
- Improve app UX to reduce cancellations
""")
