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

This project explored how NBA Draft Combine metrics relate to long-term career success, using Box Plus/Minus (BPM), True Shooting % (TS%), and Games Played as outcome variables. After cleaning and merging Combine and career data for hundreds of players, we generated a full correlation matrix to evaluate which traits — if any — were predictive.

### 📊 Key Findings:
- **Wingspan → BPM:** `–0.00` — virtually no correlation
- **Sprint Time → BPM:** `–0.07` — slightly faster players had better impact, but effect is minimal
- **Vertical Leap → BPM:** `+0.05` — no real link
- **Lane Agility → BPM:** `–0.01` — no significant relationship
- **Height → USG%:** `–0.21` — taller players use fewer possessions
- **TS% ↔ BPM:** `+0.24` — stronger impact correlation came from *in-game efficiency*, not Combine stats

### 🎯 Interpretation
> Combine traits like wingspan, vertical, and sprint time show **weak or negligible** correlation with career performance (BPM), efficiency (TS%), or availability (GP). The strongest signal came from `TS% → BPM`, which reflects **on-court skill** not Combine measurements.

### 📌 Takeaway
> Combine metrics **do not reliably predict NBA success**. Traits like speed or size may influence role fit, but they should be combined with contextual scouting and skill-based metrics for better draft decisions.

### 🔬 Future Directions
- Re-merge full Combine metrics (e.g., body fat %, max vert)
- Build a regression model to evaluate multiple-trait prediction
- Cluster “overachievers” and “combine stars” to find edge cases
