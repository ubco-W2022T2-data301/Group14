import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    
    #Method Chain #1, Loading Data, Filling in Missing values
    
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
    )
    
    #Method Chain #2, Adding Columns that are necessary
    df_subset = (
        df1
         .assign(Total_Fouls=lambda x: x["Home Team Fouls"] + x["Away Team Fouls"])
        .assign(Total_Yellow_Cards=lambda x: x["Home Team Yellow Cards"] + x["Away Team Yellow Cards"])
        .assign(Total_Red_Cards=lambda x: x["Home Team Red Cards"] + x["Away Team Red Cards"])
        .loc[:, ["Home Team", "Away Team", "Score", "Match Excitement", "Home Team Fouls", "Home Team Yellow Cards", "Home Team Second Yellow Cards", "Home Team Red Cards", "Away Team Fouls", "Away Team Yellow Cards", "Away Team Second Yellow Cards", "Away Team Red Cards", "year", "Total_Fouls", "Total_Yellow_Cards", "Total_Red_Cards"]]
    )
    return df_subset