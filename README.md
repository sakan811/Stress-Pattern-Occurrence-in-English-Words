# Stress Pattern Occurrence in English Words

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

According to the result from **cmudict** module, 
the same type of **Stress Pattern** sometimes occurs many times in a word. 
Only the first of the given type is considered.

# Visualizations
Check out [Instagram Post](https://www.instagram.com/p/C4TVCbuu31d/) and
[Facebook Post](https://www.facebook.com/permalink.php?story_fbid=pfbid034JSCYjYkMJp1meHhDFG8qhw4NxzSqxxjqj6TNYt2CdmBquZtJceky64s7HrzoSb4l&id=61553626169836):     


# Codes
```extract_stress_pattern.py```
- Load **SubtlexUS** dataset
- Group words by syllable count
- Extract stress patterns
- 

# Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
