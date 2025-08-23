Top FIFA Players: Analyzing Performance and Value (2012–2024)
Project Background
The FIFA video game series, transitioning to EA FC in recent years, provides a rich dataset of player statistics reflecting real-world football performance. This capstone project analyzes player data from FIFA 12 to FC 25 (2012–2024) sourced from SoFIFA. The goal is to uncover insights into player performance, market value trends, and cost-effective signings by leveraging data scraping, cleaning, and analysis techniques. The project focuses on top leagues (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) and serves as a showcase of data science applications in sports analytics.
Objectives

Who to Buy: Identify high-potential, cost-effective players using metrics like potential rating, value-to-wage ratio, and performance growth across FIFA editions.
Who’s the Best: Rank top performers and consistent stars based on overall ratings, key attributes (e.g., pace, dribbling, defending), and career longevity.
Player Value: Analyze relationships between player value, performance, and market trends, exploring factors like age, position, and market inflation.

Project Steps

Data Scraping:

Use fifa_scrape.py to scrape player data from SoFIFA.com for FIFA 12 to FC 25.
Collects attributes like ratings, wages, and contract details, saving each version to a CSV (e.g., fifa_players_fifa_12.csv).


Data Combination:

Use fifa_players_2012_2025_csv.py to merge individual CSVs into a single dataset (fifa_players_2012_2025.csv).


Data Processing and Transformation:

Use the Jupyter Notebook (Data Processing, Transformation, Manipulation.ipynb) to clean and transform data (e.g., parse dates, standardize units, calculate contract durations).
Filter for top leagues and compute derived metrics like value-to-performance ratios.


Analysis:

Perform exploratory data analysis (EDA) to identify top players, cost-effective signings, and market trends.
Example analyses: sort by wages in top leagues, subset financial columns (value, wage, etc.).


Visualization/Reporting:

Extend the notebook with visualizations (e.g., Matplotlib/Seaborn) or build dashboards for insights.
Summarize findings for stakeholders like gamers or analysts.



Installation

Clone the repository:
git clone https://github.com/your-username/fifa-players-analysis.git
cd fifa-players-analysis


Install dependencies:
pip install -r requirements.txt

Contents of requirements.txt:

pandas
selenium


Additional setup:

Install ChromeDriver compatible with your Chrome browser and add it to your system's PATH.
For the Jupyter Notebook: pip install jupyterlab numpy matplotlib seaborn (optional for visualization).



Usage
Step 1: Scraping Data
Run fifa_scrape.py to scrape player data from SoFIFA:
python fifa_scrape.py


Default Behavior: Scrapes the top 100 players for FC 25, saving to fifa_players_fc_25.csv.
Customization:
Edit fifa_name and url in main() for other FIFA versions (e.g., FIFA 12: https://sofifa.com/players?r=120002&set=true&...).
Adjust max_players to scrape more/fewer players.
Find URLs for older versions on SoFIFA’s archive.


Important Notes:
Respect SoFIFA’s terms of service and robots.txt. Avoid excessive scraping to prevent IP bans.
Add time.sleep() or proxies if needed to handle rate limits.
To scrape multiple versions, modify the script to loop over URLs (not implemented by default to avoid server overload).
Ethical Scraping: Check SoFIFA’s policies before scraping. Pre-scraped CSVs can be used if scraping is restricted.



Step 2: Combining CSVs
Place all scraped CSVs in the project directory and run:
python fifa_players_2012_2025_csv.py

This generates fifa_players_2012_2025.csv.
Step 3: Data Processing and Analysis
Open the Jupyter Notebook:
jupyter lab


Navigate to Data Processing, Transformation, Manipulation.ipynb.
Load the combined CSV/Excel and run cells to clean, transform, and analyze data.
Extend with visualizations or custom analyses (e.g., plotting value trends).

Project Structure
fifa-players-analysis/
├── fifa_scrape.py                  # Script to scrape SoFIFA data
├── fifa_players_2012_2025_csv.py   # Script to combine CSVs
├── Data Processing, Transformation, Manipulation.ipynb  # Notebook for analysis
├── requirements.txt                # Dependencies
├── fifa_players_2012_2025.csv      # Combined dataset (generated)
├── fifa_players_*.csv              # Individual FIFA version CSVs (generated)
└── README.md                       # This file

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

Report issues or suggest improvements via GitHub Issues.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Data sourced from SoFIFA.com.
Built with Python, Pandas, Selenium, and Jupyter.
Thanks to the open-source community for tools and libraries.
