# 🏀 Hornets NBA Combine Analysis

This project analyzes how NBA Draft Combine metrics relate to long-term NBA success and durability.

## 🎯 Objectives
- Explore the correlation between physical metrics (wingspan, vertical jump, lane agility, etc.) and NBA performance.
- Use advanced stats like Box Plus/Minus (BPM), True Shooting %, and Games Played to measure success.
- Assist teams (e.g. Charlotte Hornets) in identifying under-the-radar value in prospects.

## 📊 Key Visualizations

### Wingspan vs BPM
![Wingspan vs BPM](https://github.com/ethom98/hornets-nba-combine-analysis/blob/main/Plots/wingspan_vs_bpm.png?raw=true)

More plots are available in the `Plots/` folder.

## 🧪 Tools Used
- Python
- pandas, seaborn, matplotlib
- Jupyter Notebooks
- Git & GitHub

## 🔧 Data Cleaning Steps
- Reformatted Combine player names from `"Last, First"` to `"First Last"`
- Normalized all player names to lowercase
- Merged three datasets (Combine, Career, Advanced stats) on `player_name`
- Removed rows with missing core metrics (BPM, wingspan, TS%, etc.)

## 📂 Project Deliverables

- 📎 [Hornets Report Slide Deck (PDF)](Hornets_Report.pdf)
- 📊 [Jupyter Notebook Analysis](analysis.ipynb)
- 📁 [Final Merged Dataset](Data/final_merged_dataset.csv): Contains all players with complete Combine + career stats used for analysis
- 📊[Correlation Matrix](Plots/correlation_matrix.png)

## ✅ Conclusion
This analysis revealed that NBA Draft Combine metrics like wingspan, agility, and vertical jump have only **weak to moderate correlations** with long-term career impact as measured by Box Plus/Minus (BPM), games played, and true shooting percentage.

Key takeaways:
- **Wingspan** showed a very weak positive correlation with BPM
- **Agility and sprint times** were slightly more predictive of durability (games played)
- **Vertical jump and height** showed almost no meaningful correlation with long-term success

While Combine metrics provide useful baseline traits, they are **not strong standalone predictors** of NBA impact. Successful draft strategy should combine measurable data with **contextual scouting**, **role fit**, and **skill evaluation** to better project a player's career trajectory.

Future work could include:
- Incorporating **qualitative scouting grades**
- Exploring **clustering** or **regression modeling**
- Comparing combine results of overachievers vs. busts

