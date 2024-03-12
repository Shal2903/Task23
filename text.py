""" 
This program converts the adjective in the sentence to a verb. 

The function has 2 paramaters - the sentence and index. 
sentence: The input sentence with the adjective.
index: The index of the adjective in the sentence. 

The function returns the sentence with adjective replaced by a verb at the specified index. 
The 'en' suffix is added to adjective to convert it into a verb.
 
Prints the new sentence with the verb. 
"""

def adjective_to_verb(sentence, index): 
    new_sentence = ""
    for word in sentence.split(" ")[index]: 
        if word.isalpha(): 
            new_sentence += word
    return new_sentence + "en"
print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))

def add_prexfix(word):
    word = word + "un"
    return word
print (f" Prefix added to word: {add_prexfix("happy")}")
print (f" Prefix added to word: {add_prexfix("wanted")}")
