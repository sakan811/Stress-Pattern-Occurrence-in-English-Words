# Stress Pattern Occurrence in English Words
Project Latest Update: 25 June 2024

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

## Disclaimers
According to what is mentioned on the CMU Pronouncing Dictionary website, 
"Stress is difficult to get right and people disagree about it."

## Visualizations
Visualizations Latest Update: 6 May 2024

[Power BI](https://app.powerbi.com/view?r=eyJrIjoiMzhkYmVjOGUtMmE5Ni00NmUxLWIzYWYtMzk2ODQ2YmU2NGM2IiwidCI6ImZlMzViMTA3LTdjMmYtNGNjMy1hZDYzLTA2NTY0MzcyMDg3OCIsImMiOjEwfQ%3D%3D)

[Instagram](https://www.instagram.com/p/C6oRlWmM5WL/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)  

[Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid0LQsXGdyJCBBxEvjQeF7tD4tvZVkK9vVvWknG4exkd94jtmVV3Ma8wfYbBUTW5C4Cl&id=61553626169836)    

## To Run the Script to Get the English Words' Stress Pattern data
- Execute ```main.py```.
  - For example, run the following in the terminal: 
    - ```
      python main.py
      ```
  - English stress pattern data is saved as a CSV and loaded to a local SQLite database automatically.
    - The 'data' folder for a CSV file is created automatically if not exist, and the CSV is saved to this folder.
    - A local SQLite database is created automatically if not exist during the process.
      - A local SQLite database is needed for the process to work properly.

## ```stress_pattern_finder``` Package

```eng_stress_pattern_finder.py```
- Find the stress pattern of the English words with the given dataset.

## ```stress_pattern_etl``` Package

```extract_data.py```
- Extract data from **SubtlexUS** dataset.

```transform_data.py```
- Transform data to find a syllable count and stress pattern of each English word.
  - Words that aren't in the dictionary will be filtered out.

```load_to_sqlite.py```
- Load data to SQLite database tables.

```utils.py```
- Contain utility functions.

## Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
