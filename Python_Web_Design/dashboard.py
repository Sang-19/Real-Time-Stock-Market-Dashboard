import streamlit as st 
import yfinance as yf

st.title("Stock Dashboard")
st.sidebar.title("Details Required")
ticket_symbol = st.sidebar.text_input("Enter Stock Name","MSFT")
start_date = st.sidebar.date_input("Start Date:",value=None)
end_date = st.sidebar.date_input("End Date:",value=None)

ticket = yf.Ticker(ticket_symbol)
st.write("Hello")
historical_data = ticket.history(start = start_date, end = end_date)
st.write(historical_data)
