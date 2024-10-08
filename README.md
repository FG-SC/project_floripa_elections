# project_floripa_elections
dashboard for Candidates from Floripa

### README for GitHub Project

---

# Municipal Campaign Analysis in Florianópolis

This project focuses on analyzing data from the municipal elections in Florianópolis. Using **Python**, **Pandas**, and **Plotly**, the project explores candidate demographics, financial resources, and historical candidacy patterns. The data was collected from [CNN Brasil](https://www.cnnbrasil.com.br/eleicoes/quem-sao-os-candidatos-a-vereador-em-florianopolis/) and processed through a **Jupyter Notebook** that scrapes and prepares the data in a structured format.

![image](https://github.com/user-attachments/assets/90816f86-345b-4bc7-a0bf-2deda3a73580)


The results are presented in an interactive **Streamlit** web app, offering insights such as party spending, candidate demographics, and resource allocation. This tool is designed to help citizens, researchers, and policymakers better understand the dynamics of local elections.

## Features

- **Party Filter**: Select a specific party to visualize detailed data on candidates.
- **Demographic Distribution**: Analyze age, gender, race, and education levels of candidates.
- **Financial Insights**: View declared assets, total funds received, and expenses for each candidate.
- **Candidacy History**: Identify the candidates with the most candidacies and the highest funding.
- **Additional Insights**: Explore the parties with the most candidates and highest expenditures, and other campaign-related data.

## Data Collection

The data was scraped from a CNN webpage using a custom Jupyter Notebook. This notebook is included in the repository and can be used to update or extend the data. The CSV file generated from this notebook is used as the main data source for the Streamlit app.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repo-url>
    ```
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Repository Structure

- **/notebooks**: Contains the Jupyter Notebook for web scraping.
- **/data**: The CSV file generated by the Notebook.
- **app.py**: Streamlit app code for data visualization.
- **requirements.txt**: List of dependencies required to run the app.

## Usage

1. Load the web app in your browser after starting Streamlit.
2. Use the sidebar to select a political party or analyze all available data.
3. View insights such as spending, demographic distribution, and historical data.
