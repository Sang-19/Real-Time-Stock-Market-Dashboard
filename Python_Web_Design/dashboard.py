import streamlit as st 
import yfinance as yf
import plotly.express as pe
st.title("Stock Dashboard")
st.sidebar.title("Details Required")
ticket_symbol = st.sidebar.text_input("Enter Stock Name","")
start_date = st.sidebar.date_input("Start Date:",value=None)
end_date = st.sidebar.date_input("End Date:",value=None)
ticket = yf.Ticker(ticket_symbol)
historical_data = ticket.history(start = start_date, end = end_date)
if start_date is not None and end_date is not None:
  st.subheader(f'{ticket_symbol} Stock View')
  stockData = yf.download(ticket_symbol,start = start_date, end = end_date)
  Price, Historical, Chart = st.tabs(["Price Summary", "Historical Summary", "Charts"])
  with Price:
    st.write("Price Summary")
    st.write(stockData)
  with Historical:
    st.write("Historical Data")
    st.write(historical_data)
  with Chart:
    st.write("Charts")
    stockData.columns = stockData.columns.get_level_values(0)
    line_charts = pe.line(stockData, stockData.index, y="Close", title=ticket_symbol)
    st.plotly_chart(line_charts)
  
