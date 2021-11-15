import streamlit as st
import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib import rcParams


rcParams['font.family'] = 'monospace'


titles = [
    'Silicone DMC Price Chart',
    'Metall Silicon Price Chart',
    'Ferrosilicon Price Chart',
    'Polysilicon Price Chart',
]

dbs = [
    'https://github.com/patrickbickenbach/st_commodity_price_db_test/tree/main/db/db_silicone_dmc.csv',
    'https://github.com/patrickbickenbach/st_commodity_price_db_test/tree/main/db/db_metall_silicon.csv',
    'https://github.com/patrickbickenbach/st_commodity_price_db_test/tree/main/db/db_ferrosilicon.csv',
    'https://github.com/patrickbickenbach/st_commodity_price_db_test/tree/main/db/db_polysilicon.csv',
]

df = pd.DataFrame(dbs,titles)


def plot(selected_chart):

    label_color = 'black'

    date = []
    price = []

    with open(df.at[selected_chart,0],'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            date.append(row[0])
            price.append(float(row[1]))

    fig = plt.figure()
    plt.plot(date, price, color='#008800', linestyle='solid', marker='o')
    plt.xticks(rotation = 25)
    plt.xlabel('Date', color=label_color)
    plt.ylabel('Price (RMB/mt)', color=label_color)
    plt.title(selected_chart, fontsize = 20, color=label_color)
    plt.grid()
    st.pyplot(fig)


st.sidebar.title('Commodity Price Database')
selected_chart = st.sidebar.selectbox('', titles)

for i in range(len(df)):
    if selected_chart == df.index[i]:
        chart = plot(selected_chart)
