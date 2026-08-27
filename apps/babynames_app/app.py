from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Baby Names Explorer", layout="wide")


@st.cache_data
def load_data():
    return pd.read_parquet(Path(__file__).parent / "names.parquet")


df = load_data()
states = sorted(df["state"].unique())

st.title("Baby Names Explorer")
st.caption(
    "Social Security Administration state name files, 1910-2025. "
    "Rates are per 1,000 births of the selected sex in the state and year. "
    "Names with fewer than 5 occurrences in a state-year are not reported."
)

trends, mapping, top = st.tabs(["Trends over time", "Map a name", "Top names"])

with trends:
    c1, c2, c3 = st.columns([2, 1, 2])
    name = c1.text_input("Name", "Emma", key="t_name").strip().title()
    sex = c2.radio("Sex", ["F", "M"], horizontal=True, key="t_sex")
    chosen = c3.multiselect("States", states, default=["TX"], key="t_states")

    sub = df[(df["name"] == name) & (df["sex"] == sex) & (df["state"].isin(chosen))]
    if sub.empty:
        st.info("No data for that combination.")
    else:
        fig = px.line(
            sub.sort_values("year"),
            x="year",
            y="per1000",
            color="state",
            labels={"year": "Year", "per1000": "Per 1,000 births", "state": "State"},
        )
        st.plotly_chart(fig, use_container_width=True)

with mapping:
    c1, c2, c3 = st.columns([2, 1, 2])
    m_name = c1.text_input("Name", "Ailany", key="m_name").strip().title()
    m_sex = c2.radio("Sex", ["F", "M"], horizontal=True, key="m_sex")
    m_year = c3.slider("Year", 1910, 2025, 2025, key="m_year")

    sub = df[(df["name"] == m_name) & (df["sex"] == m_sex) & (df["year"] == m_year)]
    if sub.empty:
        st.info("No data for that combination.")
    else:
        fig = px.choropleth(
            sub,
            locations="state",
            locationmode="USA-states",
            color="per1000",
            scope="usa",
            color_continuous_scale="Blues",
            labels={"per1000": "Per 1,000"},
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            f"States with no color reported fewer than 5 babies named {m_name} in {m_year}."
        )

with top:
    c1, c2, c3 = st.columns([2, 1, 2])
    t_state = c1.selectbox("State", states, index=states.index("TX"), key="p_state")
    t_sex = c2.radio("Sex", ["F", "M"], horizontal=True, key="p_sex")
    t_year = c3.slider("Year", 1910, 2025, 2025, key="p_year")

    sub = (
        df[(df["state"] == t_state) & (df["sex"] == t_sex) & (df["year"] == t_year)]
        .nlargest(10, "n")[["name", "n", "per1000"]]
        .reset_index(drop=True)
    )
    sub.index = sub.index + 1
    st.dataframe(
        sub.rename(columns={"name": "Name", "n": "Count", "per1000": "Per 1,000"}),
        use_container_width=False,
    )
