# Stress Pattern Occurrence in English Words
Update Mar 11th, 2024

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

## Disclaimers
According to the result from **cmudict** module, 
the same type of **Stress Pattern** sometimes occurs many times in a word. 
Only the first of the given type is considered.

## Visualizations
[Instagram](https://www.instagram.com/p/C4Ycgo2PHJA/?utm_source=ig_web_copy_link)  
[Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid0nTKpe1Wx9BVbQJ8KZpQQfRCwp4zQn5TLDasiyiq9ec8u9fwBbJutnVa4FtXpsSfTl&id=61553626169836)    


## ```stress_pattern_etl``` Package

```extract_and_transform_syllable_data.py```
- Extract data from **SubtlexUS** dataset
- Transform data to find a syllable count and stress pattern of each English word

```load_to_sqlite.py```
- Load data to SQLite database tables

## To Run the ETL Process
```main.py```

- Execute the script

# Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
