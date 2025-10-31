import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Mi primera app en línea")

ticker = st.text_input("Ingrese el ticker de la acción", value="AAPL")

if ticker:
    data = yf.download(ticker, period="1y", interval="1d")
    st.write(f"Datos de {ticker}")
    st.dataframe(data.tail())

    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label='Precio de Cierre')
    ax.set_title(f'Precio de Cierre de {ticker} en el último año')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio de Cierre (USD)')
    ax.legend()
    st.pyplot(fig)
