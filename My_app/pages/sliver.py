import streamlit as st
import pandas as pd

data = pd.read_csv("silver.csv")
data["date"]=pd.to_datetime(data["date"])

st.title("ỨNG DỤNG THEO DÕI GIÁ BẠC")

year = sorted(data["year"].unique())

selected_year = st.multiselect(
    "Chọn các năm muốn xem",
    options=year,
    default=year
)

filtered_data = data[data["year"].isin(selected_year)]
filtered_data = filtered_data.sort_values("date")

st.subheader("1. Dữ liệu giá bạc")
st.dataframe(filtered_data)

if not filtered_data.empty:
    st.subheader("2. Biểu đồ đường")
    st.line_chart(filtered_data, x="date", y="price")

    st.subheader("3. Biểu đồ cột")
    st.bar_chart(filtered_data, x="date", y="price")

    st.subheader("4. Biểu đồ  vùng")
    st.area_chart(filtered_data, x="date", y="price")

    st.subheader("5. Thống kê giá bạc")

    st.write("Giá cao nhất:",filtered_data["price"].max())
    st.write("Giá thấp nhất:",filtered_data["price"].min())
    st.write("Giá trung bình:", filtered_data["price"].mean())

    st.subheader("6. Giá bạc trung bình từng năm")

    yearly = filtered_data.groupby("year")["price"].mean()
    st.bar_chart(yearly)

    money=st.number_input(
        "Số tiền tích lũy mỗi năm(VNĐ)",
        min_value=0,
        value=12000000,
        step=1000000
    )
    yearly_plan=(
        filtered_data.groupby("year", as_index=False)["price"]
        .mean()
    )
    yearly_plan["budget"]=money
    yearly_plan["silver_amount"]=(
        yearly_plan["budget"]/yearly_plan["price"]
    )
    st.dataframe(yearly_plan)