# Steps for the solution: 
# 1. I need some questions in a box
# 2. I need to choose some questions randomly
# 3. I need to make a score for the user
# 4. I need to ask the user the questions
# 5. I need to check if the answer is correct, print correct and give one point. else, print wrong and give nothing
# 6. I need to print the final score for the user

import random

questions = {
    'What is the keyword to define a funtion in python?': 'def', 
    'Which data type is used to store True or False values?':'boolean',
    'What is the correct fine extension for Python files?':'.py',
    'Which symbol is used to comment in python?':'#',
    'What function is used to get input from the user?':'input',
    'How do you start a for loop in python?':'for',
    'What is the output of 2 ** 3 in python?':'8'
}

def trivia_game () :
    score = 0
    total_questions = 5
    questions_list = list(questions.keys())

    selected_questions = random.sample(questions_list, total_questions)

    for i, question in enumerate(selected_questions) :
        print (f'{i+1}. {question}')
        user = input("Enter your answer please: ").lower().strip()

        correct_answer = questions[question]
        if user == correct_answer.lower() :
            print ("Correct!\n")
            score += 1
        else:
            print (f"Wrong! The correct answer is: {correct_answer}\n")

    print (f"Game over! Your final score is : {score} / {total_questions}")

trivia_game()