# CSIT 505 Final Project

Data Sets

The scripts from Star Wars Episodes IV, V, and VI come from available on kaggle.com:
https://www.kaggle.com/xvivancos/star-wars-movie-scripts

The scripts are formatted with a series three strings; the first is the line number, the second is the character, the third is the line of spoken dialogue.

Preprocessing the Data
For each film's script, the script will be read in one line at a time and will be initially formatted as lists ["line number", "character", "sentence"]. Then, the lists will be converted into tuples. These tuples will counted by character, so the number of times a character speaks in the movie will be determined. 

Sentiment Lexicons

The positive and negative sentiment lexicons came from a data science lab site, found via kaggle.com:
https://sites.google.com/site/datascienceslab/projects/multilingualsentiment .

Analysis

There was great difficulty in analying the corpus data from the three Star Wars movie scripts. While the lexicons were able to be imported from the .txt files, they were unable to be looped through and compared to the scripts. I attempted to treat the lexicons as sets and check for a script's membership in the set, but the counters that I set up to find how many words belonged to the positive and negative sentiment lexions.

I was able to find which charcters had the most lines in the each of the films as can be found in the Visual Aids program. 

