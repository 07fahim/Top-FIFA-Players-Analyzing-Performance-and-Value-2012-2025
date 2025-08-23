# Top FIFA Players: Analyzing Performance and Value (2012–2024)

Analyze a decade of player ratings, wages, and market values from the FIFA/EA FC series (FIFA 12 → FC 25) to uncover **who to buy**, **who’s the best**, and **how value evolves** across leagues.

> **Data source:** [SoFIFA](https://sofifa.com) (see **Ethical Scraping** below).

![Banner](./assets/hero.png)

---

## 🧭 Table of Contents

* [Background](#background)
* [Objectives](#objectives)
* [Project Structure](#project-structure)
* [Quick Start](#quick-start)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run the Scraper](#run-the-scraper)
  * [Combine CSVs](#combine-csvs)
  * [Process & Analyze](#process--analyze)
* [Usage Details](#usage-details)

  * [Scraping Options](#scraping-options)
  * [Combining Options](#combining-options)
  * [Notebook Workflow](#notebook-workflow)
* [Metrics & Analyses](#metrics--analyses)
* [Visualizations & Dashboards](#visualizations--dashboards)
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

## Quick Start

### Prerequisites

* **Python 3.9+**
* **Google Chrome** (latest) and a matching **ChromeDriver**
* (Optional) **JupyterLab** for notebooks, **Tableau/Power BI** for dashboards

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

### Notebook Workflow

Within `Data Processing, Transformation, Manipulation.ipynb` you will:

1. **Load** the combined CSV
2. **Clean & Standardize**: parse dates, standardize currency/units, normalize positions
3. **Engineer Features**: contract duration, per-90 stats (if available), value-to-wage ratios
4. **Filter** Top-5 leagues and relevant seasons
5. **Explore** with EDA and charts
6. **Export** curated tables for dashboards (CSV/Excel)

---

## Metrics & Analyses

Starter ideas you can adapt:

* **Top Performers**: average/peak overall; attribute leaders (pace, dribbling, defending)
* **Consistency**: standard deviation of overall across editions; streaks above threshold
* **Who to Buy**: high potential growth with low wages and favourable value-to-wage
* **Age Curves**: attribute/overall vs age by position groups
* **Inflation**: value trends by league/season; compare nominal vs inflation-adjusted
* **Wage vs Value**: correlation and outliers (undervalued/overvalued)
* **Footedness & Role**: left/right/weak foot distribution by position and league

**Example Pandas snippets**

```python
# Top wages in Top-5 leagues
mask = df["league"].isin(["Premier League","La Liga","Bundesliga","Serie A","Ligue 1"])
(df[mask]
 .groupby(["edition","club"])["wage"].sum()
 .sort_values(ascending=False)
 .head(20))

# Value-to-wage ratio and shortlist
df["value_to_wage"] = df["value"].div(df["wage"]).replace([np.inf, -np.inf], np.nan)
shortlist = (df[mask]
             .query("overall >= 78 and potential - overall >= 3 and age <= 24")
             .sort_values("value_to_wage", ascending=False)
             .head(50))
```

---

## Visualizations & Dashboards

* **Notebook charts**: Matplotlib/Seaborn for quick EDA
* **Dashboard-ready extracts**: export tidy tables (e.g., `players_top50.csv`, `value_trends.csv`)
* **BI Tools**: Build a dashboard in **Tableau** (suggested views):

  * *Top 50 value-to-wage players* (filterable by position/league)
  * *Wage vs Value correlation* over time
  * *Attribute leaders* (pace/dribbling/defending) by edition
  * *Footedness distribution* pie/bar by league
  * *Origin → League flow* (Sankey/stacked bar if Sankey unavailable)

> **Tip:** For Tableau, ensure clean dimensions (e.g., `nation`, `club`, `league`, `position`) and numeric measures (`value`, `wage`, `overall`, `potential`).

---

## Data Dictionary (Core Columns)

(Your exact columns may vary based on scraper selectors.)

| Column                                | Type     | Description                                                           |
| ------------------------------------- | -------- | --------------------------------------------------------------------- |
| `player_id`                           | int/str  | Stable SoFIFA player identifier (useful for tracking across editions) |
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

### Badges (optional)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![pandas](https://img.shields.io/badge/pandas-✓-informational)
![selenium](https://img.shields.io/badge/selenium-✓-success)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

> Replace badge links and add CI, pre-commit, or Docker badges as needed.
