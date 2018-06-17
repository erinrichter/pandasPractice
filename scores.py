import pandas as pd


# Reading in all football games and scores
df = pd.read_csv('football_games.csv')
#print(df)


########### Questions to follow #############

# Find the average score any team has ever made 2002 - 2017
df1 = pd.concat([df['home_team_points'], df['away_team_points']])
#print(df1)
print(df1.mean())

# Find the average score of each team


# Find the average score of each team by year

# Find the team with the highest score ever made

# Find the team with the most points scored overall

# Find how many games have ended in a tie

# Show how many points were scored in total by year
