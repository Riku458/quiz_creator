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
                                #Addition: Since I realized that there are some cases where the quiz/quizzes sometimes got a two correct answer or three or even all answers are correct or no answer are correct, I tried to make it that the user will input if there will be 2 or more correct answer or no correct answer.
        while True:
            correct = input("Enter the correct answer/s (can be single letter like 'a', multiple like 'a and b', 'all', or 'none' if no correct answer): ").lower()

            if correct == "none":
                final_answer = "none."
                break

            if correct == "all":
                final_answer = "all answers are correct."
                break

            valid_answers = []
            for word in correct.replace(',', ' ').split():
                if word in ["a", "b", "c", "d"] and word not in valid_answers:
                    valid_answers.append(word)

            valid_answers.sort()

            if not valid_answers:
                print("Enter at least one valid answer as (a-d), 'all', or 'none'. Also check your input if it is correct according to the instruction given.")
                continue
            
            if len(valid_answers) > 3:
                print("It will make all the options to be correct. Put 'all' if you want all the answers to be correct.")
                continue

            if len(valid_answers) == 1:
                final_answer = valid_answers[0]
            elif len(valid_answers) == 2:
                final_answer = " and ".join(valid_answers)
            else:
                final_answer = ", ".join(valid_answers[:-1]) + ", and " + valid_answers[-1]
            break

        file.write(f"Question: {question}\n")
        for i, option in enumerate(options):
            file.write(f"{chr(97+i)}) {option}\n")
        file.write(f"Correct: {final_answer}\n\n")

        while True:
            choice = input("Add another question? (y/n): ").lower()
            if choice in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'")

        if choice == "n":
            break

print(f"\nAll questions saved to {file_name}")