import streamlit as st
import pandas as pd
import plotly.express as px
loan = pd.read_pickle('data_input/loan_clean')

st.set_page_config(
page_title = "Demo Dashboard",
page_icon =  "👍" #klik windows + titik untuk membuka emoji
)

st.markdown("<h1 style='text-align: center;'>Financial Insights Dashboard: Loan Performance & Trends</h1>", unsafe_allow_html=True)

st.markdown("---") #Menambahkan garis

st.sidebar.header("Dashboard Filters and Features")

st.sidebar.markdown(
'''
- **Overview**: Provides a summary of key loan metrics.
- **Time-Based Analysis**: Shows trends over time and loan amounts.
- **Loan Performance**: Analyzes loan conditions and distributions.
- **Financial Analysis**: Examines loan amounts and distributions based on conditions.
'''
)


loan['purpose'] = loan['purpose'].str.replace("_", " ")


st.title("Financial Analysis")

option = st.selectbox("Select Loan Condition",["Good Loan","Bad Loan"])

#Kondisi Good Loan

if option == "Good Loan":
    with st.container(border=True):
        tab1, tab2 = st.tabs(['Loan Amount Distribution', 'Loan Amount Distribution by Purpose'])
        with tab1:
            loan_condition = loan[loan['loan_condition'] == 'Good Loan']
            fig = px.histogram(loan_condition,
                        x = 'loan_amount', color = 'term', nbins = 20,
                        title = 'Loan Amount Distribution',
                        template='seaborn',
                labels={
                    'loan_amount':'Loan Amount',
                    'term':'Loan Term'}
                        )
            st.plotly_chart(fig)

        with tab2:
            fig = px.box(
            loan_condition,
                x = 'purpose', 
                y = 'loan_amount',
                color = 'term', 
                title = 'Loan Amount Distribution by Purpose',
                template='seaborn',
            labels={
                'loan_amount':'Loan Amount',
                'purpose':'Loan Purpose',
                'term' : 'Loan Term'
            }
            )
            st.plotly_chart(fig)

#Kondisi Bad Loan

if option == "Bad Loan":
    with st.container(border=True):
        tab1, tab2 = st.tabs(['Loan Amount Distribution', 'Loan Amount Distribution by Purpose'])
        with tab1:
            loan_condition = loan[loan['loan_condition'] == 'Bad Loan']
            fig = px.histogram(loan_condition,
                        x = 'loan_amount', color = 'term', nbins = 20,
                        title = 'Loan Amount Distribution',
                        template='seaborn',
                labels={
                    'loan_amount':'Loan Amount',
                    'term':'Loan Term'}
                        )
            st.plotly_chart(fig)

        with tab2:
            fig = px.box(
            loan_condition,
                x = 'purpose', 
                y = 'loan_amount',
                color = 'term', 
                title = 'Loan Amount Distribution by Purpose',
                template='seaborn',
            labels={
                'loan_amount':'Loan Amount',
                'purpose':'Loan Purpose',
                'term' : 'Loan Term'
            }
            )
            st.plotly_chart(fig)