# Top FIFA Players: Analyzing Performance and Value (2012–2025)


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

---

## Background

The FIFA video game series—transitioning to **EA FC**—provides a rich, consistent snapshot of footballers’ attributes over time. This project scrapes and analyzes SoFIFA player data from **FIFA 12 to FC 25 (2012–2024)**, with a focus on the **Top-5 European leagues** (*Premier League, La Liga, Bundesliga, Serie A, Ligue 1*). It demonstrates practical data science skills: scraping, cleaning, feature engineering, analysis, and storytelling via dashboards.

## Objectives

**Who to Buy**
Identify high-potential, cost-effective players using metrics such as:

* Potential rating growth
* **Value-to-wage ratio**
* Trajectory across FIFA editions (form consistency, attribute deltas)

**Who’s the Best**
Rank top performers and durable stars by:

* Overall rating and key attributes (pace, dribbling, defending, etc.)
* Career longevity and consistency

**Player Value**
Study the relationship between market value and performance by:

* Age, position, league
* Macro trends (inflation, edition-to-edition shifts)

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

---

## Dashboards

### [League and Club Dominance (Dashboard 1)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/LeagueandClubDomianace2012-2025/Dashboard1?publish=yes)

**Problem Statements**

1. Which leagues and clubs hold the most valued players (sum)?
2. Which country has the highest potential players on average based on the top leagues?
3. Which clubs have most of the players with more than 3 Specialties (La Liga and EPL)?
4. Which are the top clubs in terms of players’ average release clause (2025)?

**Findings**

1. La Liga (Real Madrid), EPL (Man City), Serie A (Juventus), Bundesliga (Bayern) dominate most valued players.
2. Germany and Bundesliga have the highest average potential players.
3. Real Madrid, Barcelona, and Man City have most players with 3+ specialties.
4. Real Madrid tops in average release clause (2025).

---

### [Player’s Position Based Market Insights (Dashboard 2)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/PlayerPerformanceMarketValueInsights/Dashboard1?publish=yes)

**Problem Statements**

1. Who among the top 20 players provides the best market value for their wage?
2. How do player attributes vary by best position?
3. Which positions hold the highest market value?

**Findings**

1. Messi and Ronaldo provided best market value across 2012–2025.
2. Attacking positions (ST, LW, RW, CAM) have the strongest attributes.
3. Attackers and creative midfielders have higher values than defenders/goalkeepers.

---

### [Age Impact on Value & Performance (Dashboard 3)](https://public.tableau.com/app/profile/gazi.mohammad.fahimfaiyaz/viz/FIFAPlayerAnalyticsPerformanceRankingsLeagueInsights/Dashboard1?publish=yes)

**Problem Statements**

1. How have top players’ ratings changed across FIFA versions?
2. How does age influence market value and wages?
3. Which young talents show the highest potential?

**Findings**

1. Aging stars (Messi, Ronaldo) decline while new talents (Mbappé, Haaland, Vinícius Jr.) rise.
2. Value peaks at 18–24, wages peak at 27–30, both drop after 30.
3. Mbappé, Vinícius, Bellingham, Musiala dominate; clubs like Real Madrid & PSG lead.

---

### [Best FIFA Career Mode Signings 2012–2025 (Dashboard 4)](https://public.tableau.com/app/profile/gazi.mohammad.faiyaz/viz/FootballDataInsights2012-2025/Dashboard1?publish=yes)

**Problem Statements**

1. Which top players balance transfer value and rating best for Career Mode?
2. Which players dominate their positions for an elite XI?

**Findings**

1. Ronaldo, Messi, and 88–92 rated players under €40–50M offer best value.
2. Elite XI built from position-best rated stars.

---

### Football Data Insights 2012–2025 (Dashboard 5)

**Problem Statements**

1. What are the key market and rating insights for FIFA players from 2012–2025?
2. What is the geographic distribution of Europe’s most valuable leagues?
3. Which attribute has stayed most stable across versions?
4. What percentage of players are in each position group?

**Findings**

1. Huge player market, high ratings, strong growth potential.
2. EPL leads in market value, followed by La Liga, Bundesliga, Serie A, Ligue 1.
3. Movement = strongest, Defending = weakest attribute.
4. Midfielders dominate (>40% of players).

---

## Quick Start

### Prerequisites

* **Python 3.9+**
* **Google Chrome** (latest) and a matching **ChromeDriver**

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

> **Tip:** Consider locking versions with a pinned requirements file for reproducibility.

### Run the Scraper

```bash
python fifa_scrape.py
```

**Default:** Scrapes top 100 players for **FC 25**, saving to `fifa_players_fc_25.csv`.

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

Edit `main()` in **`fifa_scrape.py`** to control:

* `fifa_name`: A label (e.g., `"fifa_12"`, `"fc_25"`)
* `url`: SoFIFA list URL for the desired edition (see SoFIFA archive)
* `max_players`: Limit number of rows (e.g., `100`, `1000`)

**Example (FIFA 12):**

```python
fifa_name = "fifa_12"
url = "https://sofifa.com/players?r=120002&set=true"
max_players = 100
```

> **Ethical Scraping**: Respect SoFIFA’s **Terms of Service** and `robots.txt`. Add delays (e.g., `time.sleep`), retries, and backoff to avoid excessive requests. Consider proxying responsibly. When in doubt, **use pre-scraped CSVs** instead.

### Combining Options

Place all per-edition CSVs (e.g., `fifa_players_fifa_12.csv`, `fifa_players_fc_25.csv`) in the repo root and run:

```bash
python fifa_players_2012_2025_csv.py
```

This script concatenates per-edition files and writes `fifa_players_2012_2025.csv`.

---



## Data Dictionary (Core Columns)

(Your exact columns may vary based on scraper selectors.)

| Column                                | Type     | Description                                                           |
| ------------------------------------- | -------- | --------------------------------------------------------------------- |
| `name`                                | str      | Player name                                                           |
| `edition`                             | str      | FIFA edition label (e.g., `fifa_12`, `fc_25`)                         |
| `age`                                 | int      | Player age in that edition                                            |
| `nationality`                         | str      | Player nationality                                                    |
| `league`                              | str      | League (Top-5 filtered in analysis)                                   |
| `club`                                | str      | Club name                                                             |
| `position`                            | str      | Primary position (normalize groups: GK/DEF/MID/FWD)                   |
| `overall`                             | int      | Overall rating                                                        |
| `potential`                           | int      | Potential rating                                                      |
| `value`                               | float    | Market value (standardized currency)                                  |
| `wage`                                | float    | Weekly wage (standardized currency)                                   |
| `contract_until`                      | date/str | Contract end                                                          |
| `foot`                                | str      | Left/Right                                                            |
| `skill_moves`                         | int      | Skill moves rating                                                    |
| `weak_foot`                           | int      | Weak foot rating                                                      |
| `pace`, `dribbling`, `defending`, ... | int      | Key attribute groups (varies by edition)                              |

---

## Troubleshooting

**ChromeDriver version mismatch**

* Ensure ChromeDriver matches your Chrome version.
* On Windows, place `chromedriver.exe` on `PATH` or set an explicit path in the script.

**Blocked/Rate Limited**

* Reduce request frequency; add `time.sleep` between pages.
* Respect `robots.txt` and ToS. Consider using saved CSVs.

**Encoding/Locale issues**

* Use UTF-8 when reading/writing CSVs: `encoding="utf-8"`.
* Normalize currency symbols; parse numbers with `locale`/regex.

**Inconsistent columns across editions**

* Use a canonical schema and `reindex` missing columns with `NaN`.
* Keep a `columns_map` to rename fields consistently.

---

## Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

Please also:

* Open issues for bugs/ideas
* Add tests where practical
* Keep functions documented and type-annotated

---

## License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## Acknowledgments

* Data: **SoFIFA**
* Stack: **Python**, **Pandas**, **Selenium**, **Jupyter**
* Thanks to the open-source community for tools and libraries.

---

### Badges 

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![pandas](https://img.shields.io/badge/pandas-✓-informational)
![selenium](https://img.shields.io/badge/selenium-✓-success)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
