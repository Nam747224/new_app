import streamlit as st
import pandas as pd
data = pd.read_csv("travel.csv")

st.title("Nhật ký chuyến đi")
st.write("Danh sách các chuyến đi của tôi")

st.subheader("Tất cả các chuyến đi")
st.dataframe(data)
st.subheader("Thống kê")
st.write("Tổng số chuyến đi:",len(data))
st.write("Các địa điểm đã đi")
diadiem_list = data["diadiem"].unique()
st.write(diadiem_list)

st.subheader("Tìm kiếm chuyến đi")
diadiem=st.selectbox(
    "Chọn địa điểm",
    diadiem_list
)
result = data[data["diadiem"]==diadiem]
st.write("Các chuyến đi đến: ", diadiem)
st.dataframe(result)
st.write(
    "Số chuyến đi",
    len(result)
)