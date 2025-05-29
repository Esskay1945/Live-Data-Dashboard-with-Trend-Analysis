Live Data Dashboard
A simple Streamlit app that shows scores from a CSV file in a bar chart. You can filter by name and see if scores are going up or down. The page refreshes every 2 seconds to show live updates.






This project is a Streamlit-based web app designed to provide real-time visualization and analysis of score data loaded from a CSV file. It enables users to interactively filter data by names and view corresponding score trends in an easy-to-understand bar chart format.

Features
Data Filtering: Users can select one or multiple names from the dataset to display specific subsets of data.

Real-time Visualization: The app displays a dynamic bar chart representing the scores of selected names.

Statistical Insights: Key statistics such as average, maximum, and minimum scores are calculated and displayed for the selected data.

Trend Analysis: The app compares current scores with previous ones to identify which names have rising or falling scores.

Auto Refresh: The dashboard refreshes every 2 seconds to provide live updates, making it useful for monitoring rapidly changing data.

Session State Management: Utilizes Streamlit's session state to store previous data between runs, enabling accurate trend detection.

Use Cases
Monitoring performance scores over time.

Tracking changes in key metrics for selected groups.

Visualizing live updates from a data source for quick decision making.

How It Works
The app reads a CSV file containing columns like name and score.

It allows users to select names to filter the data.

It calculates statistics and displays a bar chart of scores.

It compares the current data with the previous run to detect score changes.

Rising and falling trends are highlighted for quick insight.

The dashboard refreshes automatically to update data and trends continuously.

Requirements
Python 3.x

Streamlit

pandas

Installation and Usage
Clone the repository.

Install dependencies: pip install streamlit pandas

Run the app: streamlit run app.py

Make sure to update the file_path variable with the path to your CSV file.
