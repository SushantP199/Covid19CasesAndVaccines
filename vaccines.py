import streamlit as st
import requests as req
import pandas as pd


def vaccines():
    # Requesting vaccines data from api
    vaccinations_data_request_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json"
    vaccinations_data_response = req.get(vaccinations_data_request_url)
    vaccinations_data = vaccinations_data_response.json()

    # Extracting all countries from api to pass into country selection box
    countries = []
    for i in range(len(vaccinations_data)):
        countries.append(vaccinations_data[i]['country'])
    countries_dataframe = pd.DataFrame(countries)
    selected_country = st.selectbox('Select Country', countries_dataframe)

    # Extracting all required fields from api for selected country
    index = 0
    show_graph = True
    for i in range(len(vaccinations_data)):
        if vaccinations_data[i]['country'] == selected_country:
            recent_vaccination_data = vaccinations_data[i]['data'][-1]
            index = i
            try:
                new_vaccines_given = recent_vaccination_data['daily_vaccinations_raw']
            except:
                new_vaccines_given = "No data found"
                show_graph = False

            try:
                total_vaccines_given = recent_vaccination_data['total_vaccinations']
            except:
                total_vaccines_given = "No data found"
                show_graph = False

            try:
                people_fully_vaccinated = recent_vaccination_data['people_fully_vaccinated']
            except:
                people_fully_vaccinated = "No data found"
                show_graph = False

            try:
                percentage_of_population_fully_vaccinated = str(
                    recent_vaccination_data['people_fully_vaccinated_per_hundred']) + "%"
            except:
                percentage_of_population_fully_vaccinated = "No data found"
                show_graph = False

            break

    # We decide if all data available then only go for calculations required for graph
    if show_graph:
        dates = []
        new_doses_given_each_day = []

        for i in range(1, 8):
            dates.append(vaccinations_data[index]['data'][-i]['date'])
            new_doses_given_each_day.append(
                vaccinations_data[index]['data'][-i]['daily_vaccinations_raw'])

        dates.reverse()
        new_doses_given_each_day.reverse()

        new_given_in_recent_seven_days_dataframe = pd.DataFrame(
            {
                "New doses given": new_doses_given_each_day,
            },
            index=dates,
        )

    # Adding UI components
    st.header(f"💉 {selected_country}'s Vaccination Details")

    st.subheader(f"New vaccines given : {new_vaccines_given}")
    st.subheader(f"Total vaccines given : {total_vaccines_given}")
    st.subheader(f"People fully vaccinated : {people_fully_vaccinated}")
    st.subheader(
        f"Percent of population fully vaccinated : {percentage_of_population_fully_vaccinated}"
    )

    st.subheader("Visualization of new doses given in recent seven days")
    if show_graph:
        st.line_chart(new_given_in_recent_seven_days_dataframe)
        st.write(
            "Above chart shows number of new doses given on particular date accordingly for recent 7 days.")
    else:
        st.write("Due to incomplete data graph cannot be displayed.")

    return selected_country
