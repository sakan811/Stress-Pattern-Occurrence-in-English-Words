# Stress Pattern Occurrence in English Words
Update Mar 11th, 2024

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

# Disclaimers
According to the result from **cmudict** module, 
the same type of **Stress Pattern** sometimes occurs many times in a word. 
Only the first of the given type is considered.

# Visualizations
[Instagram](https://www.instagram.com/p/C4Ycgo2PHJA/?utm_source=ig_web_copy_link)  
[Facebook](https://www.facebook.com/permalink.php?story_fbid=pfbid0nTKpe1Wx9BVbQJ8KZpQQfRCwp4zQn5TLDasiyiq9ec8u9fwBbJutnVa4FtXpsSfTl&id=61553626169836)    


# Codes
```extract_stress_pattern.py```
- Load **SubtlexUS** dataset
- Group words by syllable count
- Extract stress patterns
- Find **Primary and Secondary Stress Position**
  - Save to additional columns
- Save to TSV

# Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
