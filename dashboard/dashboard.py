import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    df = pd.read_csv('/submission/dashboard/main_data.csv')
    return df

def season_chart(df):
    seasons = df.groupby('season')['cnt'].sum().reset_index()
    season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    seasons['season_name'] = seasons['season'].map(season_names)

    plt.figure(figsize=(8, 5))
    sns.barplot(x='season_name', y='cnt', data=seasons)
    plt.title('Total Bike Rentals by Season', fontsize=14)
    plt.xlabel('Season', fontsize=10)
    plt.ylabel('Total Rentals', fontsize=10)
    plt.xticks(rotation=0)
    
    return plt.gcf(), seasons

def weather_chart(df):
    weather = df.groupby('weathersit')['cnt'].mean().reset_index()
    weather_names = {1: 'Clear',2: 'Cloudy',3: 'Rain'}
    weather['weather_name'] = weather['weathersit'].map(weather_names)
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(weather['weather_name'], weather['cnt'])
    plt.title('Average Rentals by Weather', fontsize=14)
    plt.xlabel('Weather Condition', fontsize=10)
    plt.ylabel('Average Rentals', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0)
    
    
    return plt.gcf(), weather

def main():
    st.set_page_config(layout="wide")
    st.title('Bike Sharing')
    df = load_data()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Season bar-chart')
        season_fig, season_data = season_chart(df)
        st.pyplot(season_fig)
        with st.expander("View Seasonal Data"):
            st.dataframe(season_data)
    with col2:
        st.subheader('Weather bar-chart')
        weather_fig, weather_data = weather_chart(df)
        st.pyplot(weather_fig)
        with st.expander("View Weather Data"):
            st.dataframe(weather_data)
    st.markdown("mee")
    st.subheader("Insight")
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    with insight_col1:
        best_season = season_data.loc[season_data['cnt'].idxmax(), 'season_name']
        st.metric("Best Season", best_season)
    with insight_col2:
        best_weather = weather_data.loc[weather_data['cnt'].idxmax(), 'weather_name']
        st.metric("Best Weather", best_weather)
    with insight_col3:
        total_rentals = df['cnt'].sum()
        st.metric("Total", f"{total_rentals:,}")
if __name__ == "__main__":
    main()