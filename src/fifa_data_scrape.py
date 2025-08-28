from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import unicodedata
import re
import time

# Define columns for the output CSV
columns = [
    "FIFA Version Name", "Name", "Position", "Age", "Overall rating", "Potential", "Team", 
    "Contract Dates", "Height", "Weight", "Foot", "Best overall", "Best position", "Joined", 
    "Value", "Wage", "Release clause", "Total attacking", "Crossing", "Finishing",
    "Heading accuracy", "Short passing", "Volleys", "Total skill", "Dribbling", "Curve",
    "FK Accuracy", "Long passing", "Ball control", "Total movement", "Acceleration",
    "Sprint speed", "Agility", "Reactions", "Balance", "Total power", "Shot power",
    "Jumping", "Stamina", "Strength", "Long shots", "Total mentality", "Aggression",
    "Interceptions", "Att. Position", "Vision", "Penalties", "Composure", "Total defending",
    "Marking", "Standing tackle", "Sliding tackle", "Total goalkeeping", "GK Diving",
    "GK Handling", "GK Kicking", "GK Positioning", "GK Reflexes", "Total stats",
    "Base stats", "Weak foot", "Skill moves", "Attacking work rate", "Defensive work rate",
    "International reputation", "Body type", "Real face", "Pace / Diving",
    "Shooting / Handling", "Pacing / Kicking", "Dribbling / Reflexes", "Defending / Pace",
    "Physical / Positioning", "Nationality", "Player Specialities", "Club League Name", 
    "Club Position", "Club Kit Number", "Contract Valid Until", "National Team Position", 
    "National Team Kit Number", "Player Image URL", "Profile URL"
]


def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('utf-8', 'ignore').decode('utf-8').strip()

def clean_rating(text):
    match = re.match(r'^\s*(\d+)\s*([+-]\d+)?\s*$', text)
    return match.group(1) if match else text

def clean_specialities(specialities_list):
    return [normalize_text(s.text.strip()).lstrip('#') for s in specialities_list]

def scrape_players(driver, fifa_version, max_players, url):
    data = []
    current_count = 0
    page_player_index = 0

    while current_count < max_players:
        # Wait for table to load
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        time.sleep(2)

        # Get all rows in the table
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Stop if no more players on the page
        if page_player_index >= len(rows) - 1:
            break

        # Process one player
        row = rows[page_player_index + 1]  # Skip header
        cols = row.find_elements(By.TAG_NAME, "td")

        # Get name, profile link, and positions
        name = normalize_text(cols[1].text.split('\n')[0])
        position_elements = cols[1].find_elements(By.CLASS_NAME, "pos")
        position = ", ".join(normalize_text(elem.text) for elem in position_elements) if position_elements else "Unknown"
        profile_link = cols[1].find_element(By.TAG_NAME, "a").get_attribute("href") or "Unknown"

        # Collect main table data
        row_data = []
        clean_indices = {3, 4, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                         25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                         41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                         57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69}
        for i in range(len(cols)):
            if i == 5:  # Team and Contract
                team = normalize_text(cols[5].find_element(By.TAG_NAME, "a").text or "Unknown")
                contract = normalize_text(cols[5].find_element(By.CLASS_NAME, "sub").text or "Unknown")
                row_data.extend([team, contract])
            elif i in [0, 1, 12, 72]:  # Skip image, name, extra column, hidden column
                continue
            else:
                text = normalize_text(cols[i].text or "Unknown")
                row_data.append(clean_rating(text) if i in clean_indices else text)

        # Visit player profile for additional data
        driver.get(profile_link)
        # Wait for player image (present on all profiles)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//img[@data-type="player"]')))
        time.sleep(1)

        # Get profile data
        nationality_elements = driver.find_elements(By.XPATH, '//p[contains(., "y.o.")] / a[contains(@href, "/players?na=")]')
        nationality = normalize_text(nationality_elements[0].get_attribute("title") or "Unknown") if nationality_elements else "Unknown"

        specialities = driver.find_elements(By.XPATH, '//div[h5="Player specialities"]/p/a')
        player_specialities = ', '.join(clean_specialities(specialities)) if specialities else "Unknown"

        # Club-related fields
        league_elements = driver.find_elements(By.XPATH, '//div[h5="Club"]/p/a[img[contains(@class, "flag")]]')
        club_league_name = normalize_text(league_elements[0].text or "Unknown") if league_elements else "Unknown"

        position_elements = driver.find_elements(By.XPATH, '//div[h5="Club"]/p[span[contains(@class, "pos")]]/span')
        club_position = normalize_text(position_elements[0].text or "Unknown") if position_elements else "Unknown"

        kit_number_elements = driver.find_elements(By.XPATH, '//div[h5="Club"]/p[label="Kit number"]')
        kit_number = normalize_text(kit_number_elements[0].text.replace("Kit number", "") or "Unknown") if kit_number_elements else "Unknown"

        contract_valid_elements = driver.find_elements(By.XPATH, '//div[h5="Club"]/p[label="Contract valid until"]')
        contract_valid = normalize_text(contract_valid_elements[0].text.replace("Contract valid until", "") or "Unknown") if contract_valid_elements else "Unknown"

        # National team fields
        national_team_position_elements = driver.find_elements(By.XPATH, '//div[h5="National team"]/p[span[contains(@class, "pos")]]/span')
        national_team_position = normalize_text(national_team_position_elements[0].text or "Unknown") if national_team_position_elements else "Unknown"

        national_team_kit_number_elements = driver.find_elements(By.XPATH, '//div[h5="National team"]/p[label="Kit number"]')
        national_team_kit_number = normalize_text(national_team_kit_number_elements[0].text.replace("Kit number", "") or "Unknown") if national_team_kit_number_elements else "Unknown"

        # Get player image URL
        image_elements = driver.find_elements(By.XPATH, '//img[@data-type="player"]')
        image_url = normalize_text(image_elements[0].get_attribute("data-src") or "Unknown") if image_elements else "Unknown"

        # Combine data
        final_row_data = [fifa_version, name, position] + row_data + [nationality, player_specialities, club_league_name, club_position, kit_number, contract_valid, national_team_position, national_team_kit_number, image_url, profile_link]
        data.append(final_row_data)
        current_count += 1
        page_player_index += 1

        # Go back to main page
        driver.back()

        # Move to next page if needed
        if page_player_index >= len(rows) - 1 and current_count < max_players:
            next_buttons = driver.find_elements(By.XPATH, '//a[@aria-label="Next"]')
            if next_buttons:  # Click Next button if it exists
                next_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Next"]')))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", next_button)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(3)
            else:  # Fallback to URL with offset
                print("No Next button found, using offset navigation.")
                offset = current_count
                driver.get(f"{url}&offset={offset}")
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
                time.sleep(3)
            page_player_index = 0  # Reset for new page

    return data, current_count

def main():
    # Settings
    max_players = 100
    fifa_name = "FC 25"
    url = "https://sofifa.com/players?r=250044&set=true&col=oa&sort=desc&showCol%5B%5D=ae&showCol%5B%5D=hi&showCol%5B%5D=wi&showCol%5B%5D=pf&showCol%5B%5D=oa&showCol%5B%5D=pt&showCol%5B%5D=bo&showCol%5B%5D=bp&showCol%5B%5D=jt&showCol%5B%5D=le&showCol%5B%5D=vl&showCol%5B%5D=wg&showCol%5B%5D=rc&showCol%5B%5D=ta&showCol%5B%5D=cr&showCol%5B%5D=fi&showCol%5B%5D=he&showCol%5B%5D=sh&showCol%5B%5D=vo&showCol%5B%5D=ts&showCol%5B%5D=dr&showCol%5B%5D=cu&showCol%5B%5D=fr&showCol%5B%5D=lo&showCol%5B%5D=bl&showCol%5B%5D=to&showCol%5B%5D=ac&showCol%5B%5D=sp&showCol%5B%5D=ag&showCol%5B%5D=re&showCol%5B%5D=ba&showCol%5B%5D=tp&showCol%5B%5D=so&showCol%5B%5D=ju&showCol%5B%5D=st&showCol%5B%5D=sr&showCol%5B%5D=ln&showCol%5B%5D=te&showCol%5B%5D=ar&showCol%5B%5D=in&showCol%5B%5D=po&showCol%5B%5D=vi&showCol%5B%5D=pe&showCol%5B%5D=cm&showCol%5B%5D=td&showCol%5B%5D=ma&showCol%5B%5D=sa&showCol%5B%5D=sl&showCol%5B%5D=tg&showCol%5B%5D=gd&showCol%5B%5D=gh&showCol%5B%5D=gc&showCol%5B%5D=gp&showCol%5B%5D=gr&showCol%5B%5D=tt&showCol%5B%5D=bs&showCol%5B%5D=wk&showCol%5B%5D=sk&showCol%5B%5D=aw&showCol%5B%5D=dw&showCol%5B%5D=ir&showCol%5B%5D=bt&showCol%5B%5D=hc&showCol%5B%5D=pac&showCol%5B%5D=sho&showCol%5B%5D=pas&showCol%5B%5D=dri&showCol%5B%5D=def&showCol%5B%5D=phy"

    # Start browser
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    # Scrape data
    data, player_count = scrape_players(driver, fifa_name, max_players, url)

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Print requested information
    print(f"Number of players scraped: {player_count}")
    print(f"Columns: {', '.join(columns)}")
    print(f"DataFrame shape: {df.shape}")

    # Save to CSV
    csv_filename = f"fifa_players_{fifa_name.replace(' ', '_').lower()}.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"Data saved to {csv_filename}")

    # Close browser
    driver.quit()

if __name__ == "__main__":
    main()