# DomoRobotoSan
Japanese sentence generator constructed using object orientated programming language C++. This is essentially Japanese revision. I hate flashcards but can cope with programming.

## The Plan
A sentence is a vector of word objects. 
A word object can be a particle, adjective, noun, adverb etc using inheritance.
Different words have different functions attached.
Sentence generator which starts with a random starter word and constructs rest of sentence from there.

### Example 1
For an object or subject to a sentence we could group a few words. Like an adjective and a noun. The mouldy cat for example. Pick a noun and adjective at random.

### Example 2
To describe how something looks or appears to be you add -soo onto the adjective. 
Thus the function Adjective::SooIfy() will exist (name TBC).

You would call this SooIfy when in an appropriate sentence.

Some appropriate sentence structures would be:
\[object\] \[adjective\] \[verb\]
Hashi wa muzukashi-soo desu
or
\[adjective\] \[verb\]
Oishi-soo desu ne

SooIfy would take the string contained in the Adjective and add soo onto the end appropriately.

### To do list
As this is a pet project I do not want to be too meticulous planning everything at start with a spec. The main aim of this project is for me to actually learn Japanese by deconstructing and constructing Japanese grammar this way. Therefore I will start development accordingly:

1.  Create skeletons of the class hierarchy
2.  Create a way and syntax for storing a list of Japanese words in a text file (complete with all variations - all tenses for verbs for example and parameters). Might use hex for parameters eg store parameters as A5 for bools 1010 0101.
3.  Create basic sentence generator function.
4.  I will take a chapter of the text book adding vocabularly to the word list and adding sentence structures to the sentence generator function. If sentence structures is conditional on the words then we add paramaters and functions to the word objects to tell which words we can use for a given sentence structure. 
⋅⋅*E.g. -na adjectives are essentially nouns. All the conjugation rules for both nouns and na-adjectives are the same. These adjectives can modify nouns by adding na in-between. 
⋅⋅*-i adjectives however are completely different.
5. I will then test the code and debug it accordingly.
6. GOTO $4

# CHANGELOG
Will update this once I complete a step or other extraordinary changes to the code. All commits will also have comments with further detail.

0.01  Readme.md created (first go at markdown properly - probably will need to commit many more times than once)
