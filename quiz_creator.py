# Assignment No.09: Quiz Creator

file_name = input("Enter a file name for your quiz file (without its extenstion): ") + ".txt" 

print("\n--------QUIZ MAKER--------")
#1. Get the questions that the user wants (I will use while loop here also)

with open(file_name, "a") as file:      #3. Get the file of the questions using while loop
    while True:
        question = input("Enter question (or enter 'quit' to exit): ")
        if question.lower() == "quit":
            break
    
        options = []            #2. Get the options that the user will put in the question and the correct answer (I will use while loop here also)
        for letter in ["a", "b", "c", "d"]:
            options.append(input(f"Enter option {letter}: "))
        
        while True:
            correct = input("Enter the correct answer/s (can be single letter like 'a', multiple like 'a and b', 'all', or 'none' if no correct answer): ").lower()

            if correct == "none":
                correct == "none"
                break

            if correct == "all":
                correct == "all"
                break

#Addition: Since I realized that there are some cases where the quiz/quizzes sometimes got a two correct answer or three or even all answers are correct or no answer are correct, I want to make it that the user will input if there will be 2 or more correct answer or no correct answer.

        correct = input("Correct answer (a-d): ").lower()
        while correct not in ["a", "b", "c", "d"]:
            print("Please enter a, b, c, or d")
            correct = input("Correct answer (a-d): ").lower()

        file.write(f"Q: {question}\n")
        for i, option in enumerate(options):
            file.write(f"{chr(97+i)}) {option}\n")
        file.write(f"Correct: {correct}\n\n")

        while True:
            choice = input("Add another question? (y/n): ").lower()
            if choice in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'")

        if choice == "n":
            break

print(f"\nAll questions saved to {file_name}")

