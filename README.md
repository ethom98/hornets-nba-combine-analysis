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
- 📁 [Final Merged Dataset](data/final_merged_dataset.csv)
