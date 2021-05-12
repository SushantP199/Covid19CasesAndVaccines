import streamlit as st
import vaccines
import cases

st.title("COVID-19 Vaccines & Cases Dashboard")

# Vaccines details
selected_country = vaccines.vaccines()

# Cases details
cases.cases(selected_country)

# Addition info
with st.beta_expander("Know More about Terms"):
    st.write("""
        _New vaccines given_ indicates new doses given last day,  _Total vaccines given_ indicates total number of doses given to people till last day,
        _People fully vaccinated_ means more than one dose of vaccine given a person or some vaccines requires more than one dose and _Percent of 
        population fully vaccinated_ indicates percentage of how many people got fully vaccinated out of total population.
    """)

with st.beta_expander("Data Credits"):
    st.write("Postman : https://covid-19-apis.postman.com/")
    st.write("Our World in Data : https://ourworldindata.org/covid-vaccinations?country=CHN")


with st.beta_expander("Note"):
    st.write("""
        All the data related to vaccination details is of every last day i.e. data of day before you are reading this line.
        And all the data related to case details is of today i.e. of ongoing day.
     """)
     
st.write("*Contribution by Sushant Pagam*")
