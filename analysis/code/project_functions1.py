import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
.assign(Total_Yellow_Cards=lambda x: x ["Home Team Yellow Cards"] + x["Home Team Second Yellow Cards"] + x["Away Team Yellow Cards"]
       +  x["Away Team Second Yellow Cards"])   
.assign(Total_Red_Cards=lambda x: x ["Home Team Red Cards"] +x["Away Team Red Cards"])  
.loc[:,["Home Team", "Away Team", "Score", "Home Team Fouls", "Home Team Yellow Cards","Home Team Second Yellow Cards", "Home Team Red Cards", "Away Team Fouls", "Away Team Yellow Cards", "Away Team Second Yellow Cards","Away Team Red Cards", "year"]]
       )     

    # Make sure to return the latest dataframe

    return df2 
