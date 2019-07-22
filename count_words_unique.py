from collections import Counter


with open('sentence.txt', 'r') as f:
    contents=f.read()
    lines = contents.split('\n')
    print (lines, len(lines))
    

    for line in lines:
        words=line.split(' ')

    print (words)
    
    #for word in words:
        #if (word.endswith('.') or word.endswith('\n')):
            #print(word)            
            #word=word.strip('.')

    #count_of_words=Counter(words)

    #for key, value in count_of_words.items():
        #print ("{} has {} occurences".format(key,value))
