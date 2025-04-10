# Assignment No.09: Quiz Creator


print("--------QUIZ MAKER--------")
#1. Get the questions that the user wants (I will use while loop here also)

while True:
    question = input("Enter question (or enter 'quit' to exit): ")
    if question.lower() == "quit":
        break
    
    option = []             #2. Get the options that the user will put in the question and the correct answer (I will use while loop here also)
    for letter in ["a", "b", "c", "d"]:
        option.append(input(f"Enter option {letter}: "))

#3. Get the file of the questions using while loop
