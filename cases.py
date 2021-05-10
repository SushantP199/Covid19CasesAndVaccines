import streamlit as st
import requests as req
import pandas as pd


def cases(selected_country):
    # Requesting cases data from api
    cases_data_request_url = "https://corona.lmao.ninja/v2/countries/" + \
        selected_country + "?yesterday=true&strict=true&query"
    cases_data_response = req.get(cases_data_request_url)
    cases_data = cases_data_response.json()

    # Extracting relevant fields
    today_cases = cases_data['todayCases']
    total_cases = cases_data['cases']

    today_recovered = cases_data['todayRecovered']
    total_recovered = cases_data['recovered']

    today_deaths = cases_data['todayDeaths']
    total_deaths = cases_data['deaths']

    # recovery rate calculation
    recovery_rate = round(total_recovered / total_cases * 100, 2)

    # Dataframe creation required for plotting
    today_cases_dataframe = pd.DataFrame(
        {"Todays Data":  [today_cases, today_recovered, today_deaths], },
        index=["Today Cases", "Today Recovered", "Today Deaths"]
    )

    total_cases_dataframe = pd.DataFrame(
        {"All time Data":  [total_cases, total_recovered, total_deaths], },
        index=["Today Cases", "Today Recovered", "Today Deaths"]
    )

    # Adding UI components
    st.header(f"🦠 Cases Details in {selected_country}")

    st.subheader(
        f"Today Cases : {today_cases}, Today Deaths : {today_deaths}, Today Recovered : {today_recovered}"
    )
    st.subheader(
        f"Total Cases : {total_cases}, Total Deaths : {total_deaths},  Total Recovered : {total_recovered}"
    )
    st.subheader(f"Recovery Rate : {recovery_rate}%")

    st.subheader("Visualization of todays data")
    st.bar_chart(today_cases_dataframe)
    st.subheader("Visualization of all time data")
    st.bar_chart(total_cases_dataframe)

