'''
For a given phrase, we need to encrypt with the help of cyclic shift in their reversed indices:

INPUT:

yum

OUTPUT:

avm

In obove example, yum is given as input. When reverse indexed, index of y = 2, u = 1, m = 0.
Now we need to replace existing alphabets such that theird reverse index is added to existing alphabet to result in new alphabet.
i.e , m + 0 = m ; u + 1 = v ; y + 2 = a

'''


phrase = input("")

def encrypt_phrase(phrase):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', \
    'v', 'w', 'x', 'y', 'z']

    phrase_words = phrase.split()
    
    #iterating over words in phrase
    new_phrase = []
    
    for word in phrase_words:
    
        rev_chars = list(word)[::-1]
        new_alphas = [] 
    
        #iterating over letters in words
        for i, alphabet in enumerate(rev_chars):
            idx = rev_chars.index(alphabet, i)
            new_idx = alphabets.index(alphabet) + idx
            print(alphabet, idx, new_idx)
            
            if new_idx > 25:
                new_idx = new_idx - 25 - 1 
                
            new_alphas.append(alphabets[new_idx])
            
        new_phrase.append("".join(new_alphas[::-1]))
    
    return " ".join(new_phrase)
    
print(encrypt_phrase(phrase))
