# Stress-Pattern-Occurrence-in-English-Words

The stress pattern was based on **The CMU Pronouncing Dictionary**.   

The **cmudict** module from the **NLTK** library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the **SubtlexUS** dataset.     

According to the result from **cmudict** module, 
the same type of **Stress Pattern** sometimes occurs many times in a word. 
Only first of the given type is considered.

# Result and Further Details
Check out the link below to see the full result and more details on the project.  
https://sakan811.github.io/Stress-Pattern-Occurrence-in-English-Words/

# Codes
- Divided the English words in the "SubtlexUS" into categories from 2 to 6-syllable words as tsv files.
- Converted each tsv into csv file.
- Extracted the stress pattern of each word in the given category using 'cmudict'.
- Save the stress pattern of each word as a new column of the same file.
- Visualized all the stress patterns of each syllable category using Altair.

# Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
