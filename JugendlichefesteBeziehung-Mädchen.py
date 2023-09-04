import streamlit as st
import pandas as pd
import altair as alt

st.header("Anteil der Jugendlichen, die bereits eine feste Beziehung hatten - Mädchen")
st.subheader("")

source = pd.DataFrame({
        'Anteil (%)': [17, 27, 42, 64, 63, 75, 85],
        'Alter': ['11', '12', '13', '14', '15', '16', '17']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Alter:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Deutschland; Mai 2009
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista")