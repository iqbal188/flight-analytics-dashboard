import streamlit as st
import pandas as pd
from dbhelper import Database
import plotly.express as px
import plotly.graph_objects as go

db = Database()

st.sidebar.title('Flight Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = sorted(db.fetch_city_names())

    with col1:
        source = st.selectbox('Source', city)
    with col2:
        destination = st.selectbox('Destination', city)

    if st.button('Search'):
        if source == destination:
            st.warning("Source and Destination cannot be same")
        else:
            results = db.fetch_all_flights(source, destination)
            if results:
                df = pd.DataFrame(
                    results,
                    columns=['Airline', 'Route', 'Departure Time', 'Duration', 'Price']
                )

                st.dataframe(df)
            else:
                st.error("No flights found")

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="percent+label"
        )
    )

    st.header('Airline Distribution')
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()

    fig = px.bar(
        x=city,
        y=frequency1,
        labels={'x': 'City', 'y': 'Number of Flights'},
        title='Busiest Airports'
    )

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    date, frequency2 = db.daily_frequency()

    fig = px.line(
        x=date,
        y=frequency2,
        labels={'x': 'Date', 'y': 'Flights'},
        title='Daily Flight Trend'
    )

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    st.title('Flight Analytics Dashboard')
    st.write("Use the sidebar to explore flight data and analytics.")

