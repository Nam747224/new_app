import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime

st.set_page_config(
    page_title="Quản lý chi tiêu cá nhân",
    layout="wide"
)

st.title("Quản lý chi tiêu cá nhân")

st.markdown("""
Ứng dụng giúp
            
-Ghi lại khoản thu
-Ghi lại khoản chi
-Thống kê
-Biểu đồ
-Xuất Excel
""")
if "data" not in st.session_state:
    st.session_state.data=pd.DataFrame(columns=[
        "Ngày",
        "Loại",
        "Danh mục",
        "Số tiền(vnd)",
        "Đơn vị tiền",
        "Quy đổi tiền",
        "Ghi chú"
    ])

st.sidebar.header("Thêm giao dịch")

date = st.sidebar.date_input(
    "Ngày",
    datetime.today()
)

transaction_type = st.sidebar.selectbox(
    "Loại",
    ["Thu", "Chi"]
)
category = st.sidebar.selectbox(
    "Danh mục",
    [
        "Ăn uống",
        "Đi lại",
        "Giải trí",
        "Lương",
        "Mua sắm",
        "Tiền điện",
        "Tiền nước",
        "Khác"
    ]
)
amount = st.sidebar.number_input(
    "Số tiền(vnd)",
    min_value=0,
    step=1000
)

unit = st.sidebar.selectbox(
    "Đơn vị tiền",
    [
        "vnd",
        "ndt",
        "$"
    ]
)

note = st.sidebar.text_input(
    "Ghi Chú"
)
def exchange(amount,unit):
    if (unit == "$"):
        exchange = amount*25000
    elif (unit == "ndt"):
        exchange = amount * 8000
    elif (unit=="vnd"):
        exchange = amount * 1
    return exchange

if st.sidebar.button("Lưu"):
    exc = exchange(amount,unit)
    new_row = {
        "Ngày":str(date),
        "Loại":transaction_type,
        "Danh mục":category,
        "Số tiền(vnd)":amount,
        "Đơn vị tiền":unit,
        "Quy đổi tiền": exc,
        "Ghi chú":note
    }

    st.session_state.data=pd.concat(
        [
            st.session_state.data,
            pd.DataFrame([new_row])
        ],
        ignore_index=True
    )
    st.success("Đã lưu giao dịch")

    df = st.session_state.data
    st.header("Danh sách giao dịch")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.header("Xóa giao dịch")
    if len(df)>0:
        row=st.selectbox(
            "Chọn đòng cần xóa",
            df.index
        )

    if st.button("Xóa giao dịch"):
        st.session_state.data=(
            st.session_state.data
            .drop(row)
            .reset_index(drop=True)
        )
        st.success("Đã xóa thành công")
        st.rerun()

    st.header("Bộ lọc")
    col1, col2 = st.columns(2)

    with col1:
        filter_type = st.selectbox(
            "Loại",
            ["Tất cả", "Thu", "Chi"]
        )
    with col2: 
        categories = ["Tất cả"]+list(df["Danh mục"].unique())

        filter_category = st.selectbox(
            "Danh mục",
            categories
        )
    filtered_df = df.copy()
    if filter_type != "Tất cả":
        filtered_df=filtered_df[
            filtered_df["Loại"]==filter_type
        ]
    if filter_category != "Tất cả":
        filtered_df=filtered_df[
            filtered_df["Danh mục"]==filter_category
        ]