import streamlit as st
import pandas as pd

data = pd.read_csv("gold.csv")
data["date"]=pd.to_datetime(data["date"])
st.title("ỨNG DỤNG THEO DÕI GIÁ VÀNG")
years = sorted(data["years"].unique())

select_years = st.multiselect(
    "chọn các năm muốn xem",
    options=years,
    default=years
)
filtered_data = data[data["years"].isin(select_years)]

st.write("Dữ liệu giá vàng")
st.dataframe(filtered_data)

st.subheader("1. Biểu đồ đường")
st.line_chart(filtered_data, x="date", y="price")

st.subheader("2. Biểu đồ cột")
st.bar_chart(filtered_data, x="date", y="price")

st.subheader("3. Biểu đồ vùng")
st.area_chart(filtered_data, x="date", y="price")

