
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    
    #Method Chain #1, Loading Data, getting rid of N/A values
    
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
    )
    
    #Method Chain #2 adding columns and selecting necesarry columns
    df_4 = (pd.read_csv("../../Group14/data/raw/archive/matchesall2014-2020.csv")
    .dropna()
    .assign(possession_ratio=lambda x: x ['Home Team Possession %'] / x['Away Team Possession %'])   
    .assign(result_score_ratio=lambda x: x ['Home Team Goals Scored'] / x['Away Team Goals Scored'])
    .loc[:, ["Home Team", "Away Team", "Score", "Half Time Score", 'Match Excitement',
               'Home Team Rating', 'Away Team Rating', 'Home Team Possession %', 'Away Team Possession %', 
               'Home Team Total Shots', 'Away Team Total Shots',  'Home Team Pass Success %','Away Team Pass Success %', 
               'Home Team Fouls','Home Team Yellow Cards', 'Home Team Second Yellow Cards','Home Team Red Cards',
               'Away Team Fouls', 'Away Team Yellow Cards', 'Away Team Second Yellow Cards', 'Away Team Red Cards',
               'Home Team Goals Scored', 'Away Team Goals Scored', 'year']]
    )
    return df_4

