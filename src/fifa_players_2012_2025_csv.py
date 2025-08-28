import pandas as pd
import os
from datetime import datetime

def combine_fifa_csvs(input_directory, output_filename="fifa_players_2012_2025.csv"):
    csv_files = [
        "fifa_players_fifa_12.csv",
        "fifa_players_fifa_13.csv",
        "fifa_players_fifa_14.csv",
        "fifa_players_fifa_15.csv",
        "fifa_players_fifa_16.csv",
        "fifa_players_fifa_17.csv",
        "fifa_players_fifa_18.csv",
        "fifa_players_fifa_19.csv",
        "fifa_players_fifa_20.csv",
        "fifa_players_fifa_21.csv",
        "fifa_players_fifa_22.csv",
        "fifa_players_fifa_23.csv",
        "fifa_players_fc_24.csv",
        "fifa_players_fc_25.csv"
    ]
    
    columns = [
        "FIFA Version Name", 
        "Name", 
        "Position",  
        "Age", 
        "Overall rating", 
        "Potential", 
        "Team", 
        "Contract Dates",
        "Height", 
        "Weight", 
        "Foot", 
        "Best overall", 
        "Best position", 
        "Joined",
        "Value", 
        "Wage", 
        "Release clause", 
        "Total attacking", 
        "Crossing", 
        "Finishing",
        "Heading accuracy", 
        "Short passing", 
        "Volleys", 
        "Total skill", 
        "Dribbling", 
        "Curve",
        "FK Accuracy", 
        "Long passing", 
        "Ball control", 
        "Total movement", 
        "Acceleration",
        "Sprint speed", 
        "Agility", 
        "Reactions", 
        "Balance", 
        "Total power", 
        "Shot power",
        "Jumping", 
        "Stamina", 
        "Strength", 
        "Long shots", 
        "Total mentality", 
        "Aggression",
        "Interceptions", 
        "Att. Position", 
        "Vision", 
        "Penalties", 
        "Composure", 
        "Total defending",
        "Marking", 
        "Standing tackle", 
        "Sliding tackle", 
        "Total goalkeeping", 
        "GK Diving",
        "GK Handling", 
        "GK Kicking", 
        "GK Positioning", 
        "GK Reflexes", 
        "Total stats",
        "Base stats", 
        "Weak foot", 
        "Skill moves", 
        "Attacking work rate", 
        "Defensive work rate",
        "International reputation", 
        "Body type", 
        "Real face", 
        "Pace / Diving",
        "Shooting / Handling", 
        "Pacing / Kicking", 
        "Dribbling / Reflexes", 
        "Defending / Pace",
        "Physical / Positioning", 
        "Nationality", 
        "Player Specialities", 
        "Club League Name", 
        "Club Position",
        "Club Kit Number", 
        "Contract Valid Until", 
        "National Team Position", 
        "National Team Kit Number",
        "Player Image URL", 
        "Profile URL"
    ]
    
    dfs = []
    
    # Read each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(input_directory, csv_file)
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path, encoding='utf-8-sig')
                print(f"Successfully read {csv_file}")
                df = df.reindex(columns=columns, fill_value=None)
                dfs.append(df)
            except Exception as e:
                print(f"Error reading {csv_file}: {e}")
        else:
            print(f"File not found: {csv_file}")
    
    if not dfs:
        print("No CSV files found to combine.")
        return
    
    # Combine all DataFrames
    try:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df = combined_df.reindex(columns=columns)
        output_path = os.path.join(input_directory, output_filename)
        combined_df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"Combined CSV saved successfully to {output_path}")
        print(f"Total rows in combined file: {len(combined_df)}")
        
    except Exception as e:
        print(f"Error combining CSV files: {e}")

def main():
    input_directory = os.getcwd()  
    output_filename = "fifa_players_2012_2025.csv"
    
    print(f"Combining FIFA CSV files from 2012 to 2025 into {output_filename}...")
    print(f"Current date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    combine_fifa_csvs(input_directory, output_filename)

if __name__ == "__main__":
    main()