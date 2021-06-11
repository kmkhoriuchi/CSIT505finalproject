# CSIT 505 Final Project

Data Sets

The scripts from Star Wars Episodes IV, V, and VI come from available on kaggle.com:
https://www.kaggle.com/xvivancos/star-wars-movie-scripts

The scripts are formatted with a series three strings; the first is the line number, the second is the character, the third is the line of spoken dialogue.

Preprocessing the Data:
For each film's script, the script will be read in one line at a time and will be initially formatted as lists ["line number", "character", "sentence"]. Then, the lists will be converted into tuples. These tuples will counted by character, so the number of times a character speaks in the movie will be determined. 

Sentiment Lexicon

The positive and negative sentiment lexicons came from a data science lab site, found via kaggle.com:
https://sites.google.com/site/datascienceslab/projects/multilingualsentiment

