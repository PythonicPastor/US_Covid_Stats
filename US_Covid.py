import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import requests

#data cleaning
url = 'https://data.cdc.gov/resource/9mfq-cb36.json'
df = pd.read_json(url)
df['submission_date'] = df['submission_date'].str.split('T', expand=True)[0]
df = df.loc[:, df.columns.intersection(['submission_date','tot_cases','new_case','new_death','tot_death'])]
df = df.sort_values(by="submission_date")
usPop = 333749517
df['infRate'] = round(df['tot_cases']/usPop*100,2)
df['deathRate'] = round(df['tot_death']/usPop*100,2)
df['deathRate'] = df['deathRate'].fillna(0)
plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": "black",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "white",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})
days = 30
fig, axes = plt.subplots(figsize=(20, 6), dpi=80)
plt.title("US Covid-19(#)")
axes.plot(df['submission_date'].tail(days), df['tot_cases'].tail(days), '-ob', label="Overall Cases(#)")
axes.fill_between(df['submission_date'].tail(days), df['tot_cases'].tail(days), color="blue", alpha=0.2)
axes.plot(df['submission_date'].tail(days), df['tot_death'].tail(days), '-oc', label="Overall Deaths(#)")
axes.fill_between(df['submission_date'].tail(days), df['tot_death'].tail(days), color="cyan", alpha=0.2)
axes.plot(df['submission_date'].tail(days), df['new_case'].tail(days), '-og', label="New Cases(per day)")
axes.fill_between(df['submission_date'].tail(days), df['new_case'].tail(days), color="green", alpha=0.2)
axes.plot(df['submission_date'].tail(days), df['new_death'].tail(days), '-oy', label="New Deaths(per day)")
axes.fill_between(df['submission_date'].tail(days), df['new_death'].tail(days), color="yellow", alpha=0.2)

axes.legend()
plt.title("US Covid-19(%)")
fig, axes = plt.subplots(figsize=(20, 6), dpi=80)
axes.plot(df['submission_date'].tail(days), df['infRate'].tail(days), '-or', label="Infection Rate(%)")
axes.fill_between(df['submission_date'].tail(days), df['infRate'].tail(days), color="red", alpha=0.2)
axes.plot(df['submission_date'].tail(days), df['deathRate'].tail(days), '-oy', label="Death Rate(%)")
axes.fill_between(df['submission_date'].tail(days), df['deathRate'].tail(days), color="yellow", alpha=0.2)
axes.legend()
