import json
import os

dirname = os.path.dirname(__file__)

wordleAnswersFilename = os.path.join(dirname, 'words/answers.json')
wordlePossibleAnswersFilename = os.path.join(dirname, './words/possibleAns.json')

ansFile = open(wordleAnswersFilename)
answers = json.load(ansFile)

possAnsFile = open(wordlePossibleAnswersFilename)
possAns = json.load(possAnsFile)

print(len(answers['answers']))
print(len(possAns['answers']))