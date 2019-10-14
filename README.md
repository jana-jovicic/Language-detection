# Language-detection

This is homework assignment for application to Petnica summer school of machine learning.
The goal is to create a software component which will automatically detect the language of a given text in the form of a paragraph, sentence, word, or a few letters. For a given text sequence program calculates the probability of it being written in given languages. Assignment is detaily explained in  _Language detection.pdf_.

Directory datasets contains 5 examples. Each of them contains: 
* seqences of text for which we need to detect in what language are they written 
* language directories that contain samples of text written in them

Directory desired_outputs is used for testing of the program. It contains desired output for each of the examples.

Run the program with command **python3 lang_detection.py** and then as input give path to the directory which contains corpus of plain text documents written in different languages and path to the file which contains text sequences for which you need to detect the language, e.g:
* datasets/4/corpus
* datasets/4/sequences.txt
