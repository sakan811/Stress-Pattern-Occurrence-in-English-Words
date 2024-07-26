# Stress Pattern Occurrence in English Words
Project Latest Update: 26 July 2024

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

## Codebase Details
### Test Status
[![CodeQL](https://github.com/sakan811/Stress-Pattern-Occurrence-in-English-Words/actions/workflows/codeql.yml/badge.svg)](https://github.com/sakan811/Stress-Pattern-Occurrence-in-English-Words/actions/workflows/codeql.yml)

[![Python application](https://github.com/sakan811/Stress-Pattern-Occurrence-in-English-Words/actions/workflows/python-app.yml/badge.svg)](https://github.com/sakan811/Stress-Pattern-Occurrence-in-English-Words/actions/workflows/python-app.yml)

### To Run the Script to Get the English Words' Stress Pattern data
- Execute ```main.py```
  - **Data** is loaded to a local **SQLite** database automatically.
    - A local **SQLite** database is created **automatically** if not exist in the given path.
    - You can change the path by adjusting this variable:
      ```
      db = 'eng_stress_pattern.db'
      ```

### ```stress_pattern_finder``` Package

```eng_stress_pattern_finder.py```
- Find the stress pattern of the English words with the given dataset.

### ```stress_pattern_etl``` Package

```extract_data.py```
- Extract data from **SubtlexUS** dataset.

```transform_data.py```
- Transform data to find a syllable count and stress pattern of each English word.
  - Words that aren't in the dictionary will be filtered out.

```load_to_sqlite.py```
- Load data to SQLite database tables.

## Database Details
Tables:
- StressPattern
  - **Main table** 
  - Store **syllable count**, **stress pattern**, and **primary** and **secondary stress position** of each word
- SyllableGroup
  - Store **syllable count** of each word

## Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
