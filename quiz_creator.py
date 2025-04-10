# Assignment No.09: Quiz Creator

file = input("Enter a file name for your quiz file (without its extenstion): ") + ".txt" 

print("--------QUIZ MAKER--------")
#1. Get the questions that the user wants (I will use while loop here also)

with open(file, "a") as f:  #3. Get the file of the questions using while loop
    while True:
        question = input("Enter question (or enter 'quit' to exit): ")
        if question.lower() == "quit":
            break
    
        options = []             #2. Get the options that the user will put in the question and the correct answer (I will use while loop here also)
        for letter in ["a", "b", "c", "d"]:
            options.append(input(f"Enter option {letter}: "))

        correct = input("Correct answer (a-d): ").lower()
        while correct not in ["a", "b", "c", "d"]:
            print("Please enter a, b, c, or d")
            correct = input("Correct answer (a-d): ").lower()

        f.write(f"Q: {question}\n")
        for i, option in enumerate(options):
            f.write(f"{chr(97+i)}) {option}\n")
        f.write(f"Correct: {correct}\n\n")

        while True:
            choice = input("Add another question? (y/n): ").lower()
            if choice in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'")

        if choice == "n":
            break

print(f"\nAll questions saved to {file}")

