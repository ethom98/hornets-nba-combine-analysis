
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the datasets
combine_df = pd.read_csv('Draft Combine - Kaggle.csv')
career_df = pd.read_csv('all_seasons.csv')
advanced_df = pd.read_csv('advanced.csv')

# Convert Combine player names from 'Last, First' to 'First Last'
def reformat_name(name):
    parts = name.split(', ')
    return f"{parts[1]} {parts[0]}".lower().strip() if len(parts) == 2 else name.lower().strip()

combine_df['player_name'] = combine_df['PLAYER'].apply(reformat_name)
career_df['player_name'] = career_df['player_name'].str.lower().str.strip()
advanced_df['player_name'] = advanced_df['year-name'].str.extract(r'^\d{4}-(.*)$')[0].str.lower().str.strip()

# Select relevant columns
combine_clean = combine_df[['player_name', 'YEAR', 'HGT', 'WNGSPN', 'STNDVERT', 'LANE', 'SPRINT']].copy()
combine_clean.columns = ['player_name', 'draft_year', 'height', 'wingspan', 'vertical', 'lane_agility', 'sprint_time']

career_clean = career_df[['player_name', 'gp', 'ts_pct', 'usg_pct']]
advanced_clean = advanced_df[['player_name', 'BPM']]



# Merge datasets by player_name
merged_df = pd.merge(combine_clean, career_clean, on='player_name', how='inner')
final_df = pd.merge(merged_df, advanced_clean, on='player_name', how='left')

# Drop rows with missing key fields
final_df.dropna(subset=['height', 'wingspan', 'vertical', 'lane_agility', 'sprint_time', 
                        'gp', 'ts_pct', 'usg_pct', 'BPM'], inplace=True)

final_df.shape



# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(final_df[['height', 'wingspan', 'vertical', 'lane_agility', 'sprint_time', 
                      'gp', 'ts_pct', 'usg_pct', 'BPM']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix: Combine Metrics vs Career Stats")
plt.tight_layout()
plt.show()



# Wingspan vs BPM
sns.regplot(data=final_df, x='wingspan', y='BPM')
plt.title('Wingspan vs Box Plus/Minus (BPM)')
plt.xlabel('Wingspan (inches)')
plt.ylabel('BPM')
plt.tight_layout()
plt.show()



# Lane Agility vs Games Played
sns.regplot(data=final_df, x='lane_agility', y='gp', color='green')
plt.title('Lane Agility vs Games Played')
plt.xlabel('Lane Agility Time (seconds)')
plt.ylabel('Career Games Played')
plt.tight_layout()
plt.show()



# Vertical vs TS%
sns.regplot(data=final_df, x='vertical', y='ts_pct', color='purple')
plt.title('Vertical Jump vs True Shooting %')
plt.xlabel('Standing Vertical (inches)')
plt.ylabel('TS%')
plt.tight_layout()
plt.show()
