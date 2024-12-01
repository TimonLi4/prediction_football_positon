import pandas as pd


df = pd.read_csv('players_15.csv')

# print(df.head())
# print(df.info())
# print(df.describe())


# best players 

def top_30_by_postion(position):
    return df[df['player_positions'].str.contains(position)].sort_values(by='overall',ascending=False).head(30)



#def
position = 'LW'
top_def = top_30_by_postion(position)[['short_name','age','club','nationality','player_positions','potential','overall']]
print(top_def)
