def word_mind():
    import random
    
    teller = 1
    woorden = ["groen", "brand", "broek", "aarde", "atlas", "feest", "beest", "breed", "wreed", "brood", "broed", "bloed", "wroet"]

    final_word= random.choice(woorden)
    punten = len(final_word)
    ppunten = punten * "-"
    print("The secret word: " + str(ppunten))
    guess = input("Guess the word: ")
    guess_final = len(final_word)
    guess_guess = len(guess)
    gh = '----- '
    if guess == final_word:
        print("Word " + '"' + final_word + '"' + " found!")

    #  controle wat goed is en wat niet goed of op de verkeerde plaats is
    while not guess == final_word:
        teller = teller + 1
        p = 0
        for letr in guess:
            checker = guess.index(letr)
            if letr in final_word and guess.index(letr) == final_word.index(letr):
                gh = gh[:p]+letr +gh[p+1:]
                checker = final_word.index(letr)
                
            elif letr in final_word and not letr.index(letr)== final_word.index(letr):
                gh = gh[:p]+'?' +gh[p+1:]
                
            elif not letr in final_word: 
                gh = gh[:p]+'-' +gh[p+1:]
                
            elif not guess_final == guess_guess:
                gh = gh[:p]+'-' +gh[p+1:]
            p +=1 
        print(gh)

        gh = '01234 '
        p=0
        if not guess == final_word:
            guess = input("Guess the word: ")
            
            if guess == final_word:
                print("Word " + '"' + final_word + '"' + " found!")
            guess_final = len(final_word)
            guess_guess = len(guess)

  
    
    print("Your average is " + str(teller)  + ".00")       
    ja_nee = input("another game (Y/N)? ")
    
    if ja_nee == "Y":
        while ja_nee == "Y":
            word_mind()
    
            
            
word_mind()
