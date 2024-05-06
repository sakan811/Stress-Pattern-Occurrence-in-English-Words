# Stress Pattern Occurrence in English Words
Update May 6th, 2024

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

## Disclaimers
According to what is mentioned on the CMU Pronouncing Dictionary website, 
"Stress is difficult to get right and people disagree about it."

## Visualizations
[Instagram](https://www.instagram.com/p/C4Ycgo2PHJA/?utm_source=ig_web_copy_link)  
[Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid0nTKpe1Wx9BVbQJ8KZpQQfRCwp4zQn5TLDasiyiq9ec8u9fwBbJutnVa4FtXpsSfTl&id=61553626169836)    

## To Run the ETL Process
```main.py```
- Execute the script

## ```stress_pattern_finder``` Package

```eng_stress_pattern_finder.py```
- Find the stress pattern of the English words with the given dataset

## ```stress_pattern_etl``` Package

```extract_and_transform_syllable_data.py```
- Extract data from **SubtlexUS** dataset
- Transform data to find a syllable count and stress pattern of each English word
  - Words that aren't in the dictionary will be filtered out

```load_to_sqlite.py```
- Load data to SQLite database tables

## Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
