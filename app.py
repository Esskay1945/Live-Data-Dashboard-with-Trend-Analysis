import streamlit as st
import pandas as pd
import time

file_path = r'C:\Users\64 Home\OneDrive - MSFT\data.csv'

st.title("Live Data Dashboard with Analysis")

# Use session state to keep track of previous data between runs
if 'prev_data' not in st.session_state:
    st.session_state.prev_data = None

# Filter selection UI
data = pd.read_csv(file_path)
names = data['name'].unique()
selected_names = st.multiselect("Select names to display", options=names, default=names)
filtered_data = data[data['name'].isin(selected_names)]

# Show bar chart
st.bar_chart(filtered_data.set_index('name')['score'])

# Calculate stats
avg_score = filtered_data['score'].mean()
max_score = filtered_data['score'].max()
min_score = filtered_data['score'].min()

# Check trends compared to previous data
prev_data = st.session_state.prev_data
if prev_data is not None:
    merged = pd.merge(filtered_data, prev_data, on='name', suffixes=('', '_prev'))
    merged['trend'] = merged['score'] - merged['score_prev']
    rising = merged[merged['trend'] > 0]['name'].tolist()
    falling = merged[merged['trend'] < 0]['name'].tolist()
else:
    rising, falling = [], []

st.markdown(f"""
**Average Score:** {avg_score:.2f}  
**Max Score:** {max_score}  
**Min Score:** {min_score}  

**Rising Scores:** {', '.join(rising) if rising else 'None'}  
**Falling Scores:** {', '.join(falling) if falling else 'None'}  
""")

# Save current filtered data as previous for next run
st.session_state.prev_data = filtered_data

# Auto-refresh every 2 seconds
st.experimental_rerun()
time.sleep(2)
