# Stress-Pattern-Occurrence-in-English-Words
This is a personal analysis project about Stress Pattern Occurrence in English Words.

This project is intended to provide English learners with data that allows them to do a data-driven guess 
when encountering words that they aren't sure where to stress, as stress is important in English pronunciation.  

The stress pattern was based on The CMU Pronouncing Dictionary.   

The 'cmudict' module from the 'NLTK' library was used to extract the stress pattern from the dataset.    

The English words dataset was based on the “SubtlexUS” dataset.     

# Result and Further Details
Check out the link below to see the full result and more details on the project.  
https://sakan811.github.io/Stress-Pattern-Occurrence-in-English-Words/

# Codes
```extract_stress_pattern.py```:
- Load "SubtlexUS".
- Count words' syllables in the "SubtlexUS".
- Export into TSV, grouped by syllables.
- Load TSV of each syllable from 2 to 6 syllables.
- Extracted the stress pattern of each word in the given category using 'cmudict'.
- Save the stress pattern of each word as a new column of the same file.
- Export into TSV, grouped by syllables.

```create_chart.py```:
- Load TSV of each syllable from 2 to 6 syllables.
- Visualized all the stress patterns of each syllable category using Altair with 2 types of charts:
  - The one that show all stress pattern in the given syllable.
  - The one that show top 5 stress pattern in the given syllable.
- Save charts into SVGs.
  
# Sources
The CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict   
“SubtlexUS” dataset: http://www.lexique.org/?page_id=241  
