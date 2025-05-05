import random

# ASSIGNMENT NO.10: QUIZ READER FROM QUIZ CREATOR


#1. Make a menu for the user to choose either making a quiz or taking a quiz

print("\n-------- QUIZ PROGRAM --------")

while True:
    print("\n-------- MAIN MENU --------")
    print("1. Create a new quiz")
    print("2. Take a quiz")
    print("3. Exit")

    user_choice = input("Enter your choice (1-3): ")

#2. Make a function that will align in the menu

    if user_choice == "1":
        quiz_filename = input(
            "Enter a file name for your quiz file (without extension): "
        ) + ".txt"
        print("\n-------- QUIZ MAKER --------")

        with open(quiz_filename, "a") as quiz_file:
            while True:
                question_text = input("Enter question (or 'quit' to exit): ")
                if question_text.lower() == "quit":
                    break

                question_options = []
                for option_letter in ["a", "b", "c", "d"]:
                    option_text = input(f"Enter option {option_letter}: ")
                    question_options.append(option_text)

                while True:
                    prompt = "Enter correct answer/s (e.g., 'a', 'a and b', "
                    prompt += "'all', or 'none'): "
                    user_correct_answer = input(prompt).lower()

                    if user_correct_answer == "none":
                        formatted_correct_answer = "none."
                        break
                    if user_correct_answer == "all":
                        formatted_correct_answer = "all answers are correct."
                        break

                    valid_option_letters = []
                    for word in user_correct_answer.replace(',', ' ').split():
                        if word in ["a", "b", "c", "d"] and word not in valid_option_letters:
                            valid_option_letters.append(word)

                    if not valid_option_letters:
                        print("Invalid input! Use letters a-d, 'all', or 'none'.")
                        continue

                    if len(valid_option_letters) == 1:
                        formatted_correct_answer = valid_option_letters[0]
                    elif len(valid_option_letters) == 2:
                        formatted_correct_answer = " and ".join(valid_option_letters)
                    else:
                        formatted_correct_answer = ", ".join(
                            valid_option_letters[:-1]
                        ) + ", and " + valid_option_letters[-1]
                    break

                quiz_file.write(f"Question: {question_text}\n")
                for option_index, option_text in enumerate(question_options):
                    quiz_file.write(f"{chr(97+option_index)}) {option_text}\n")
                quiz_file.write(f"Correct: {formatted_correct_answer}\n\n")

                add_another = input("Add another question? (y/n): ").lower()
                if add_another != "y":
                    break

        print(f"Quiz saved to {quiz_filename}")