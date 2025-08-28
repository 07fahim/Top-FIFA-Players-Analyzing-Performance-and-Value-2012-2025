# Top FIFA Players: Analyzing Performance and Value (2012–2025)

Analyze a decade of player ratings, wages, and market values from the FIFA/EA FC series (FIFA 12 → FC 25) to uncover **who to buy**, **who’s the best**, and **how value evolves** across leagues.

> **Data source:** [SoFIFA](https://sofifa.com) (see **Ethical Scraping** below).

![Banner](./assets/hero.png)

---

## Table of Contents

* [Background](#background)
* [Objectives](#objectives)
* [Project Structure](#project-structure)
* [Dashboards](#dashboards)
* [Quick Start](#quick-start)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run the Scraper](#run-the-scraper)
  * [Combine CSVs](#combine-csvs)
  * [Process & Analyze](#process--analyze)
* [Usage Details](#usage-details)

  * [Scraping Options](#scraping-options)
  * [Combining Options](#combining-options)
* [Data Dictionary (Core Columns)](#data-dictionary-core-columns)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [Badges](#badges)

---

## Background

The FIFA video game series—transitioning to **EA FC**—provides a rich, consistent snapshot of footballers’ attributes over time. This project scrapes and analyzes SoFIFA player data from **FIFA 12 to FC 25 (2012–2024)**, with a focus on the **Top-5 European leagues** (*Premier League, La Liga, Bundesliga, Serie A, Ligue 1*). It demonstrates practical data science skills: scraping, cleaning, feature engineering, analysis, and storytelling via dashboards.

## Objectives

**Who to Buy**

* Identify high-potential, cost-effective players using metrics such as potential rating growth, value-to-wage ratio, and trajectory across FIFA editions.

**Who’s the Best**

* Rank top performers and durable stars by overall rating, key attributes, and career consistency.

**Player Value**

* Study market value vs. performance by age, position, league, and edition-to-edition trends.

---


## Project Structure
```
fifa-players-analysis/
├── fifa_scrape.py                      # Script to scrape SoFIFA data
├── fifa_players_2012_2025_csv.py       # Script to combine per-version CSVs
├── Data Processing, Transformation, Manipulation.ipynb  # Cleaning & EDA
├── requirements.txt                    # Python dependencies
├── fifa_players_2012_2025.csv          # Combined dataset (generated)
├── fifa_players_*.csv                  # Per-version CSVs (generated)
├── assets/                             # Images for README/dashboard (optional)
└── README.md                           # This file
```

## [Dashboards](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/LeagueandClubDomianace2012-2025/Dashboard1) (You can visit the public dashboard here.)

### [League and Club Dominance (Dashboard 1)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/LeagueandClubDomianace2012-2025/Dashboard1)
**Problem Statements**
- Which leagues and clubs hold the most valued players (sum)?
- Which country has the highest potential players on average based on the top leagues?
- Which clubs have the most players with more than 3 specialties (La Liga and EPL)?
- Which are the top clubs in terms of players' average release clause (2025)?

**Findings**
- La Liga (Real Madrid), EPL (Man City), Serie A (Juventus), and Bundesliga (Bayern Munich) dominate in terms of the total market value of their players.
- Germany and the Bundesliga have the highest average potential players across the top leagues.
- Real Madrid, FC Barcelona, and Manchester City have the most players with more than 3 specialties in La Liga and the EPL.
- Real Madrid leads in average release clause for players in 2025, reflecting their high-value squad.

---

### [Player's Position Based Market Insights (Dashboard 2)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/PlayersPositionBasedMarketInsights/Dashboard1)
**Problem Statements**
- Who among the top 20 players provides the best market value for their wage?
- How do player attributes vary by best position?
- Which positions hold the highest market value?

**Findings**
- Lionel Messi and Cristiano Ronaldo consistently offer the best market value relative to their wages across 2012–2025.
- Attacking positions (ST, LW, RW, CAM) exhibit the highest attribute ratings, particularly in pace, dribbling, and shooting.
- Attackers and creative midfielders command higher market values compared to defenders and goalkeepers, driven by their offensive contributions.

---

### [Age Impact on Value & Performance (Dashboard 3)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/AgeImpactonValuePerformance/Dashboard1)
**Problem Statements**
- How have top players' ratings changed across FIFA versions over time?
- How does a player's age influence their market value and wages over time?
- Which young talents show the highest potential ratings and market values across different clubs and countries?

**Findings**
- Top players' ratings remain high, but aging stars like Messi and Ronaldo show gradual declines, while emerging talents like Kylian Mbappé, Vinícius Jr., and Erling Haaland rise to maintain the top-tier rating balance.
- Player market value peaks at ages 18–24 due to high potential, while wages peak later (27–30) with experience. Both metrics decline after age 30, with wages dropping more slowly.
- Young stars such as Mbappé, Vinícius Jr., Jude Bellingham, and Jamal Musiala exhibit exceptional potential and market value. Clubs like Real Madrid, PSG, and top English teams dominate, with Brazil, France, and England producing many high-value young talents.

---

### [Best FIFA Career Mode Signings 2012–2025 (Dashboard 4)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/BestFIFACareerModeSignings20122025/Dashboard1)
**Problem Statements**
- Which top FIFA players provide the best balance between transfer value and overall rating for potential signings in Career Mode?
- Which players dominate their respective positions in terms of overall rating for an elite starting XI?

**Findings**
- Legendary players like Cristiano Ronaldo and Lionel Messi, along with players rated 88–92 and valued under €40M–€50M, provide the best balance of quality and cost for Career Mode signings.
- An elite starting XI can be constructed from players with the highest overall ratings in their respective positions, ensuring top performance across all roles.

---

### [Football Data Insights 2012–2025 (Dashboard 5)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/FootballDataInsights2012-2025/Dashboard1)
**Problem Statements**
- What are the key market and rating insights for FIFA players from 2012–2025?
- What is the geographic distribution of Europe's most valuable football leagues?
- Which attribute (Movement, Skill, Attacking, Mentality, Defending) has remained most stable across versions?
- What percentage of players are in each position category?

**Findings**
- The FIFA player market features a vast total value, with players exhibiting high average ratings and significant growth potential across editions.
- The Premier League (England) leads in total market value, followed by La Liga (Spain), Bundesliga (Germany), Serie A (Italy), and Ligue 1 (France), significantly outvaluing other European competitions.
- Movement attributes remain the most stable and strongest across FIFA versions, while Defending is consistently the weakest and least valued attribute.
- Midfielders dominate the player distribution, accounting for over 40% of players in Europe's top leagues, reflecting a focus on midfield development in major football nations (Spain, UK, France, Germany, Italy).

---

## Quick Start

### Prerequisites
- Python 3.9+
- Google Chrome (latest) and a matching ChromeDriver

### Installation
```bash
# Clone
git clone https://github.com/your-username/fifa-players-analysis.git
cd fifa-players-analysis

# Base dependencies
pip install -r requirements.txt

# Optional (for notebook + visuals)
pip install jupyterlab numpy matplotlib seaborn
```

**Tip:** Consider locking versions with a pinned requirements file for reproducibility.

### Run the Scraper
```bash
python fifa_scrape.py
```
**Default:** Scrapes top 100 players for FC 25, saving to `fifa_players_fc_25.csv`.

### Combine CSVs
```bash
python fifa_players_2012_2025_csv.py
```
Produces `fifa_players_2012_2025.csv` in the project root.

### Process & Analyze
```bash
jupyter lab
```
Open `Data Processing, Transformation, Manipulation.ipynb` and run the cells to clean, transform, and analyze the combined dataset.

---

## Usage Details

### Scraping Options
To scrape data from SoFIFA, configure the `main()` function in `fifa_scrape.py` with the following parameters:

- **fifa_name**: A label for the FIFA edition (e.g., "fifa_12", "fc_25")
- **url**: The SoFIFA player list URL for the desired edition (see SoFIFA archive)
- **max_players**: Limit the number of rows to scrape (e.g., 100, 1000)

To obtain the correct URL with all necessary columns:

1. Visit the SoFIFA website for the desired FIFA edition (e.g., https://sofifa.com/players).
2. In the column selection section, select all required columns (e.g., name, age, nationality, league, club, position, overall, potential, value, wage, contract_until, foot, skill_moves, weak_foot, pace, dribbling, defending, etc.).
3. Click Apply to update the table with the selected columns.
4. Copy the updated URL from your browser's address bar.
5. Paste this URL into the `url` parameter in the `main()` function of `fifa_scrape.py`.

**Example (FIFA 12):**
```python
fifa_name = "fifa_12"
url = "https://sofifa.com/players?r=120002&set=true"
max_players = 100
```

**⚠️ Ethical Scraping:** Respect SoFIFA's Terms of Service and robots.txt. Add delays (e.g., `time.sleep`), retries, and backoff to avoid excessive requests. Consider proxying responsibly. When in doubt, use pre-scraped CSVs instead.

### Combining Options
Place all per-edition CSVs (e.g., `fifa_players_fifa_12.csv`, `fifa_players_fc_25.csv`) in the repo root and run:
```bash
python fifa_players_2012_2025_csv.py
```
This script concatenates per-edition files and writes `fifa_players_2012_2025.csv`.

---

## Data Dictionary (Core Columns)
*(Your exact columns may vary based on scraper selectors.)*

| Column | Type | Description |
|--------|------|-------------|
| name | str | Player name |
| edition | str | FIFA edition label (e.g., fifa_12, fc_25) |
| age | int | Player age in that edition |
| nationality | str | Player nationality |
| league | str | League (Top-5 filtered in analysis) |
| club | str | Club name |
| position | str | Primary position (normalize groups: GK/DEF/MID/FWD) |
| overall | int | Overall rating |
| potential | int | Potential rating |
| value | float | Market value (standardized currency) |
| wage | float | Weekly wage (standardized currency) |
| contract_until | date/str | Contract end |
| foot | str | Left/Right |
| skill_moves | int | Skill moves rating |
| weak_foot | int | Weak foot rating |
| pace, dribbling, defending, ... | int | Key attribute groups (varies by edition) |

---

## Troubleshooting

**ChromeDriver version mismatch**
- Ensure ChromeDriver matches your Chrome version.
- On Windows, place `chromedriver.exe` on PATH or set an explicit path in the script.

**Blocked/Rate Limited**
- Reduce request frequency; add `time.sleep` between pages.
- Respect robots.txt and ToS. Consider using saved CSVs.

**Encoding/Locale issues**
- Use UTF-8 when reading/writing CSVs: `encoding="utf-8"`.
- Normalize currency symbols; parse numbers with locale/regex.

**Inconsistent columns across editions**
- Use a canonical schema and reindex missing columns with NaN.
- Keep a `columns_map` to rename fields consistently.

---

## Contributing
Contributions are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

Please also:
- Open issues for bugs/ideas
- Add tests where practical
- Keep functions documented and type-annotated

---

## License
This project is licensed under the MIT License. See LICENSE for details.

## Acknowledgments
- **Data:** SoFIFA
- **Stack:** Python, Pandas, Selenium, Jupyter
- Thanks to the open-source community for tools and libraries.

---


## Badges
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-%E2%9C%94-lightgrey.svg)
![Selenium](https://img.shields.io/badge/selenium-%E2%9C%94-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

