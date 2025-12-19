
questions=("what is extention for python files?",
          "which of the following is used to get user input?",
          "Which of the following is used to get user output?",
          "what will be the output of: pow(3,3).",
          "Which of the following is remove the last element in in list?")
options=(("A.pt","B.pyt","C.pyth","d.py"),
        ("A.input()","B.get()","C.scanf","D.user_input()"),
        ("A.Output()","B.prnt()","C.printf()","D.print()"),
        ("A.18","B.33","C.27","D.9"),
        ("A.remove(index)","B.pop()","C,clear()","D.del list"))
answers=("D","A","D","C","B")
guesses=[]
score=0
question_num=0
for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"Correct answer is {answers[question_num]}")
    question_num+=1

print("*********************")
print("      Results        ")
print("*********************")

print("Answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()          
  
total=int(score/len(questions)*100)
print(f"Your score is {total}%")
