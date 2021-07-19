def countingVowelsInASentence(sentence):

    sentence = str(input('What is the sentence?: '))

    vowel  = set("a,e,i,o,u")

    noOfVowels = 0

    for v in sentence :
         if v in vowel:
            noOfVowels+=1

    print( noOfVowels , sep =' ')

    countingVowelsInASentence(sentence)
