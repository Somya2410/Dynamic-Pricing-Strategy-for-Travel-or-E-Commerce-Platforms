
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("dynamic_pricing_data.csv")

st.title("🚀 Dynamic Pricing Strategy Dashboard")
st.markdown("Analyze real-time pricing decisions based on demand, time, season, and user segments.")

# Filters
season = st.selectbox("Select Season", ["All"] + df["season"].unique().tolist())
time = st.selectbox("Select Time of Day", ["All"] + df["time_of_day"].unique().tolist())
segment = st.selectbox("Select User Segment", ["All"] + df["user_segment"].unique().tolist())

# Apply filters
filtered_df = df.copy()
if season != "All":
    filtered_df = filtered_df[filtered_df["season"] == season]
if time != "All":
    filtered_df = filtered_df[filtered_df["time_of_day"] == time]
if segment != "All":
    filtered_df = filtered_df[filtered_df["user_segment"] == segment]

# Metrics
st.metric("Average Base Price", f"₹{filtered_df['base_price'].mean():.2f}")
st.metric("Average Dynamic Price", f"₹{filtered_df['dynamic_price'].mean():.2f}")

# Line Chart
st.subheader("📈 Price Trend Over Time")
st.line_chart(filtered_df.set_index("timestamp")[["base_price", "dynamic_price"]])

# Price Distribution
st.subheader("📊 Price Distribution")
st.bar_chart(filtered_df[["base_price", "dynamic_price"]].sample(20).reset_index(drop=True))

# Raw Data
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
