import json
import os

# gets current working directory path
dirname = os.path.dirname(__file__)

# opens json files from ./word/...
wordleAnswersFilename = os.path.join(dirname, 'words/answers.json')
wordlePossibleAnswersFilename = os.path.join(dirname, 'words/possibleAns.json')

ansFile = open(wordleAnswersFilename)
answers = json.load(ansFile)

possAnsFile = open(wordlePossibleAnswersFilename)
possAns = json.load(possAnsFile)

###################################
# gets the word arrays from JSON:
ansArr = answers['answers']
possAnsArr = possAns['answers']
###################################

#prints length of each arr
print(len(answers['answers']))
print(len(possAns['answers']))