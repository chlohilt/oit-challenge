#Chloe Hilton
#BYU OIT Code Challenge: Hangman
#this took me about two hours
#November 20, 2021

from random import *
#Greet the user
print("Welcome to the game of Hangman!") 

#bool to see if they want to play another round
playAgain = True
#The program randomly selects a word from a list of 10 words 
randomWordsList = ["technology", "program", "computer", "OIT", "interface", "python", "coding", "BYU", "software", "binary"]
while (playAgain):
  #number of guesses counter
  userGuessesNum = 0
  #number of correct guesses
  correctGuesses = 0
  #bool to check if word is correct
  notCorrect = True
  #set the random word
  randomWord = randomWordsList[randint(0,9)]
  #tell user how many letters are in the word
  print("Your word has " + str(len(randomWord)) + " letters.")
  #create a correct list for positions of letters
  correctWordList = list(randomWord)
  #list of already guessed letters
  alreadyGuessedIncorrect = []
  alreadyGuessedCorrect = []
  for x in randomWord:
    alreadyGuessedCorrect.append('_')

  #program askes user for guesses until all letters in word are guessed correctly 
  while(notCorrect):
    #user is asked to guess a letter  
    userGuess = input("\nPlease guess a letter: ")
    userGuessesNum += 1
    #a. letter is in the word, the letter displayed incorrect position of the word with all previously  guessed correct letters  
    if userGuess in randomWord:
      for x in range(0, len(correctWordList)):
        if (correctWordList[x] == userGuess):
          correctIndex = x 
          alreadyGuessedCorrect[x] = userGuess
          correctGuesses += 1
      print(alreadyGuessedCorrect)
      if correctGuesses == len(correctWordList):
        #all letters of the word correct
        #a. the program tells the user they have correctly guessed the word  
        #b. and indicates the number of guesses it took 
        print(randomWord)
        print("Good job! You got the word :)")
        print("Your effort took you " + str(userGuessesNum) + " guesses!")
        #asks the user if they would like to try again or quit  
        checkPlay = input("\nWould you like to play again? (y/n)")
        if (checkPlay == 'n' or checkPlay == 'N'):
          print("Thank you for playing Hangman!")
          playAgain = False
        break
    else: #b. letter not in the word, display letter indicating not in the word previously guessed  letters not in word 
      print(userGuess + " is not in the word \n")
      alreadyGuessedIncorrect.append(userGuess)
      print("Incorrect letters guessed so far: ") 
      for x in alreadyGuessedIncorrect:
        print(x)
    
    #how many guesses have been made, correct and incorrect
    print("You have made " + str(userGuessesNum) + " guesses so far. You have made " + str(len(alreadyGuessedIncorrect)) + " incorrect guesses and " + str(userGuessesNum - len(alreadyGuessedIncorrect)) + " correct guesses")
