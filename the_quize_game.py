# ----------------------------------
def quiz_game():
    guesses = []
    correct_answers = 0
    question_num = 1
    # survey_count = 0
    survey_count1 = 0
    survey_count2 = 0

    for key in questions:
        print("\n# -------------------- Question: " + str(question_num))
        print(key)
        for i in options[question_num-1]:
            print(i)

        taken_reply = ["A", "B", "C", "D"]
        given_reply = None

        while given_reply not in taken_reply:
            given_reply = input("Enter (A, B, C or D): ").upper()
            survey_count1 += 1

        survey_count2 += 1
        guesses.append(given_reply)

        correct_answers += check_answers(questions.get(key), given_reply)
        question_num += 1

    # survey_count = survey_count1 - survey_count2
    display_score(correct_answers, guesses, (survey_count1 - survey_count2))


# ----------------------------------
def check_answers(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# ----------------------------------
def display_score(correct_answers, guesses, survey_count):

    print("\n#----------------------------------")
    print("RESULT")
    print("#----------------------------------")

    print("Correct Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_answers/len(questions))*100)
    print("You scored: " + str(score) + "%\n")

    survey_count0 = survey_count
    play_again(survey_count0)


# ----------------------------------
def play_again(survey_count0):
    another_round = ["YES", "NO"]
    play_reply = None

    while play_reply not in another_round:
        play_reply = input("Play again...? (Yes/No): ").upper()

    if play_reply == "YES":
        quiz_game()

    else:
        survey(survey_count0)
        print("\nThank you for playing!\nWatch out for more tests! ADIOS!!")


# ----------------------------------

def survey(survey_count):

    print("You entered a total of " + str(survey_count) + " invalid answers")


questions = {
    "Who was the first President of Kenya under the new constitution?: ": "A",
    "Who was the Second Prime Minister of Kenya?: ": "B",
    "How many colors doe the flag of Kenya have?: ": "D",
    "In which year did Kenya become a protectorate of Britain?: ": "C"
}
options = [["A: Uhuru Kenyatta", "B: Mwai Kibaki", "C: Jomo Kenyatta", "D: William Ruto"],
           ["A: Musalia Mudavadi", "B: Raila Odinga", "C: Jomo Kenyatta", "D: Oginga Odinga"],
           ["A: 6", "B: 3", "C: 5", "D: 4"],
           ["A: 1963", "B: 1964", "C: 1920", "D: 1895"]]

quiz_game()
