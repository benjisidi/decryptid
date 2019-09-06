def parseClue(clue):
    parsedClue = {
        'features': set(),
        'complement': False
    }
    words = clue.split(' ')
    stopWords = [
        'or',
        'space', 'spaces',
        'within',
        'standing',
        'abandoned',
        'a', 'an',
        'of',
        'structure',
        'territory'
    ]
    featureClasses = {
        'shack': 'structureTypes',
        'stone': 'structureTypes',
        'blue': 'structureColors',
        'black': 'structureColors',
        'green': 'structureColors',
        'white': 'structureColors',
        'bear': 'territories',
        'cougar': 'territories',
        'desert': 'terrains',
        'forest': 'terrains',
        'mountain': 'terrains',
        'swamp': 'terrains',
        'water': 'terrains'
    }
    digits = {
        'on': 0,
        'one': 1,
        'two': 2,
        'three': 3
    }
    filteredWords = filter(lambda word: word not in stopWords, words)
    for word in filteredWords:
        if word == 'not':
            parsedClue['complement'] = True
        elif word in featureClasses:
            parsedClue['features'].add(word)
            parsedClue['featureClass'] = featureClasses[word]
        else:
            parsedClue['radius'] = digits[word]
    return parsedClue

# ToDo: Automated tests?
print(parseClue('not within three spaces of an abandoned shack'))
print(parseClue('on swamp or mountain'))
print(parseClue('not within one space of mountain'))
print(parseClue('within two spaces of cougar territory'))
print(parseClue('within three spaces of a white structure'))
clue = parseClue('within three spaces of a white structure')