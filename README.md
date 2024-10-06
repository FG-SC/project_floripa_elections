# project_floripa_elections
dashboard for Candidates from Floripa


### README for GitHub Project: Florianópolis Municipal Campaign Data Analysis

# Florianópolis Municipal Campaign Data Analysis

This project provides an interactive exploratory analysis of the 2024 municipal election campaign data in Florianópolis, Brazil. The data includes information on candidates, political parties, financial resources, and demographic characteristics. The main goal is to allow users to investigate the distribution of campaign resources, demographic representation, and financial contributions among candidates and parties.

## Project Overview

The app is built using **Streamlit**, **Pandas**, and **Plotly**, offering a user-friendly interface that visualizes key campaign metrics. Users can filter by political party and explore various data points, including:

- Candidate demographics (age, gender, race, education level)
- Financial declarations, including the total assets declared by each candidate
- Campaign expenses and resources received
- A ranking of the top political parties by total campaign expenses
- Candidates who have run for office multiple times
- Candidates with the highest party fund contributions

## Features

1. **Party Selection**: Choose a political party from the sidebar to see detailed statistics specific to that party or select "Todos" (All) to view an overview of all parties.
2. **Demographic Distribution**: Charts illustrating the age, gender, race, and education level of the candidates.
3. **Financial Insights**: Explore declared assets, total expenses, and funds received by candidates and parties.
4. **Interactive Visualizations**: Dynamic and sortable bar charts, pie charts, and histograms powered by Plotly for seamless exploration.
5. **Top 5 Party Insights**: Special analysis on the parties with the largest contracted expenses.

## Requirements

To run this project locally, you need the following dependencies:

```bash
pip install streamlit pandas plotly
```

## Usage

Run the application with the following command:

```bash
streamlit run app.py
```

The app will open in your default web browser. Navigate through the sidebar to select a party or visualize insights for all parties.

## Data Source

The data used in this project comes from the publicly available data of the 2024 Florianópolis municipal election at [CNN Website](https://www.cnnbrasil.com.br/eleicoes/quem-sao-os-candidatos-a-vereador-em-florianopolis/), provided by the Brazilian Electoral Tribunal.

## Future Enhancements

- Additional filtering options (e.g., by candidate's experience level, or by year of candidacy)
- More advanced financial analytics (e.g., correlation between financial contributions and election results)
