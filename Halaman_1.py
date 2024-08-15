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

with st.container(border=True): #Untuk menambahkan kotak/border pada suatu tulisan
    col1, col2 =st.columns(2) #Untuk mendefinisikan nama kolom
    
    with col1:
        st.metric('Total Loans', f"{loan['id'].count():,.0f}")
        st.metric('Total Loan Amount', f"${loan['loan_amount'].sum():,.0f}")
    with col2:
        st.metric('Average Interest Rate', f"{loan['interest_rate'].mean().round()}%")
        st.metric('Average Loan Amount', f"${loan['loan_amount'].mean():,.0f}")

with st.container(border=True):
    tab1, tab2, tab3 = st.tabs(['Loans Issued Over Time', 'Loan Amount Over Time', 'Issue Data Analysis'])
    with tab1:
        loan_date_count = loan.groupby('issue_date')['loan_amount'].count()

        fig = px.line(
            loan_date_count,
            markers=True,
            title="Number of Loans Issued Over Time",
            labels={
                "issue_date": "Issue Date",
                "value": "Number of Loans"
            }
        ).update_layout(showlegend = False)

        st.plotly_chart(fig)

    with tab2:
        loan_date_sum = loan.groupby('issue_date')['loan_amount'].sum()

        fig = px.line(
            loan_date_sum,
            markers=True,
            labels={
                'value':'Number of Loans',
                'issue_date':'Issue Date'
            },
            template='seaborn',
            title="Loans Amount Over Time",
        ).update_layout(showlegend = False)

        st.plotly_chart(fig)

    with tab3:
        loan_day_count = loan.groupby('issue_weekday')['loan_amount'].count()

        fig= px.bar(
            loan_day_count,
            category_orders = { #Mengatur urutan categori (hari)
                'issue_weekday' : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            },
            title ='Distribution of Loans by Day of the Week',
            labels = {
                'value' : 'Number of Loans',
                'issue_weekday' : 'Day of the Week'
            },
            template = 'seaborn'
            ).update_layout(showlegend =False)

        st.plotly_chart(fig)

st.title("Loan Performance")

with st.container(border=True):
    with st.expander("Click Here to Expand Visualization"):

        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.pie(
                loan,
                names = 'loan_condition',
                hole = 0.5,
                title = 'Distribution of Loans by Condition',
                template ='seaborn',
                color_discrete_sequence = ['indigo', 'tomato']
            )

            st.plotly_chart(fig)

        with col2:
            grade = loan['grade'].value_counts().sort_index()

            fig = px.bar(
                grade,
                title= "Distribution of Loans by Grade",
                labels={
                    'grade' : "Grade",
                    'value' : "Number of Loans"
                }
            ).update_layout(showlegend = False)

            st.plotly_chart(fig)


