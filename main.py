import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load data
folder = 'data/'
MTeams = pd.read_csv(folder + 'MTeams.csv')
Main_file = pd.read_csv('submission02.csv')

st.title("NCAA Men's Basketball Tournament")

# Team selection
team1 = st.selectbox('Select Team 1', Main_file['TeamID1'])
team2 = st.selectbox('Select Team 2', Main_file['TeamID2'])

# Ensure different teams are selected
if team1 == team2:
    st.write('Please select different teams')
    st.stop()

# Get team IDs
# team1_id = MTeams[MTeams['TeamName'] == team1]['TeamID'].values[0]
# team2_id = MTeams[MTeams['TeamName'] == team2]['TeamID'].values[0]

# Arrange so team1_id < team2_id
if team1 > team2:
    temp = team1
    team1 = team2
    team2 = temp

# Get win probability
team1_vs_team2 = Main_file[(Main_file['TeamID1'] == team1) & (Main_file['TeamID2'] == team2)]
team1_win_percentage = team1_vs_team2['Pred'].values[0]
team2_win_percentage = 1 - team1_win_percentage

# Create the probability bar using Plotly
fig = go.Figure()

fig.add_trace(go.Bar(
    x=[team1_win_percentage],  
    y=[""],
    name=team1,
    orientation='h',
    marker=dict(color='pink', line=dict(color='black', width=1)),
    text=f"{team1_win_percentage:.2%}",  
    textposition='inside',
    hoverinfo="none"
))

fig.add_trace(go.Bar(
    x=[team2_win_percentage],  
    y=[""],
    name=team2,
    orientation='h',
    marker=dict(color='gray', line=dict(color='black', width=1)),
    text=f"{team2_win_percentage:.2%}",
    textposition='inside',
    hoverinfo="none"
))

# Customize layout
fig.update_layout(
    barmode='stack',
    xaxis=dict(title="", range=[0, 1], showticklabels=False, fixedrange=True),
    yaxis=dict(showticklabels=False),
    showlegend=False,
    height=50,
    width=600,
    margin=dict(l=10, r=10, t=10, b=10),
    plot_bgcolor='white'
)

# Display
st.plotly_chart(fig, use_container_width=True, config={'staticPlot': True})

# Display win percentages
st.write(f"{team1} Win Probability: {team1_win_percentage:.2%}")
st.write(f"{team2} Win Probability: {team2_win_percentage:.2%}")
