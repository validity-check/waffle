"""The module which handles the asking of questions, keeping main.py clean."""
# question_handler.py
# -------------------------------------
# Quizzer App
# -------------------------------------
# Work of @validity-check
# Github: https://github.com/validity-check/waffle

# Question Handler does logic related to questions to keep main.py clean and not overloaded

# Randomises questions' operators and numbers included
from random import choice, randint

# Used to ask questions and give fancy prompts
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.shortcuts import input_dialog, message_dialog

# This package allows us to write powers in superscript, making it look better than using "^"
# The package allows for superscript and subscript but we only need superscript hence we use "from"
# The package always prints a message when it is imported for some reason, but that is okay because it is not seen by the user
from supsubscript import superscript


# We have a validator over here to make sure that the number given is a valid one
# For a more in depth look at what the validators are, and what they do, look at the one in main.py
# The only difference between this one and that one is this one needs to be able to accept any float
class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        try:
            # We try converting to float, and if it fails, it will fall back to except giving the user a prompt
            float(text)
        except:
            raise ValidationError(message="Please enter a valid number.",
                                  cursor_position=document.cursor_position)


class question_handler:
    '''Handles question related logic'''

    def __init__(self, difficulty: str, question_numbers: int):
        '''Initialises question_handler class'''
        # We create a score variable so that the score can be used throughout the program
        self.score = 0
        # Makes the difficulty variable available throughout the program
        self.difficulty = difficulty
        # Make the question_numbers variable available throughout the program
        self.question_numbers = question_numbers
        # We want to ask multiplication, division, addition and subtraction but we will also do powers if in Hard or Impossible Mode
        self.operators = ["×", "÷", "+", "-"]
        if difficulty == "Hard" or difficulty == "Impossible":
            # Symbol will be used to represent powers, however, superscript numbers will be used in practice instead of this
            # This will be acheived with help of the supsubscript module
            self.operators.append("^")
        # We want to have different difficulties of questions for different difficulty modes
        if difficulty == "Easy":
            # The highest number that should be included in the question
            self.max_num = 20
            # Should the answers always be integers or can they have decimals?
            self.always_int = True
            # Does the answer have to be positive?
            self.always_positive = True
        elif difficulty == "Medium":
            self.max_num = 50
            self.always_int = True
            self.always_positive = False
        elif difficulty == "Hard":
            self.max_num = 100
            self.always_int = False
            self.always_positive = False
        # The only way the "else" case can be reached is by choosing impossible mode
        else:
            self.max_num = 9999
            self.always_int = False
            self.always_positive = False

    def ask_question(self, question_number: int):
        '''The function to create and ask a single question'''

        # We define a separate function because this code needs to be used twice
        # It is nested because it is not used in any other component of the program
        def create_numbers():
            '''The code in the ask_questions function to generate the maths question'''
            # Randomise the number which will be asked
            num1 = randint(1, self.max_num)
            num2 = randint(1, self.max_num)
            # Randomise the operation to be asked
            chosen_operation = choice(self.operators)
            # We begin an array which will be returned
            ret_arr = [num1, num2, chosen_operation]

            # Now we want to answer our question and return our results
            # We add two things to our ret_arr:
            #  - The answer which was calculated (as an int)
            #  - Whether or not this question is suitable for Easy or Medium mode (as a boolean)
            # The ret_arr is then returned
            if chosen_operation == "×":
                answer = num1 * num2
                # The extend function is used instead of append since it allows us to append several items to the list
                ret_arr.extend([answer, True])
            elif chosen_operation == "÷":
                answer = num1 / num2
                # If the answer is a float then it is may not be suitable for some game modes
                if isinstance(answer, float) and self.always_int:
                    ret_arr.extend([answer, False])
                else:
                    ret_arr.extend([answer, True])
            elif chosen_operation == "+":
                answer = num1 + num2
                ret_arr.extend([answer, True])
            elif chosen_operation == "-":
                answer = num1 - num2
                # Having a negative answer may not be suitable for some game modes
                if answer <= 0 and self.always_positive:
                    ret_arr.extend([answer, False])
                else:
                    ret_arr.extend([answer, True])
            elif chosen_operation == "^":
                answer = pow(num1, num2)
                ret_arr.extend([answer, True])
            # There are some questions which are too large to be computed (mostly made in Impossible mode)
            # This is why we use a try except statement to test if it can be computed
            try:
                float(answer)
                int(answer)
            except:
                # This message will not actually be seen by the user because of the dialogs
                # It is quite unnecessary to show this to the user though
                print(
                    "Created question which cannot be computed, making a new one..."
                )
                return [0, 0, "", 0, False]
            return ret_arr

        valid = False
        while not valid:
            # We want to continue creating new numbers until we find something which will work for the player
            [num1, num2, chosen_operation, answer, valid] = create_numbers()

        # All of the operations have similar presentation syntax except powers
        if chosen_operation != "^":
            question = f"{question_number}: What is {num1} {chosen_operation} {num2}?"
        # For powers we will use our special "supsubscript" module
        else:
            question = f"{question_number}: What is {num1}{superscript(str(num2))}?"

        # We ask for the user's answer
        # We don't have to worry with try/except statements because prompt_toolkit validates with the validator we are passing it
        user_answer = float(
            input_dialog(question, validator=NumberValidator()).run())

        # We now check if the user's answer is the correct answer
        # If it is, we add one to the score
        if user_answer == float(answer):
            self.score += 1

    def ask_questions(self):
        # We loop through the question numbers and ask them
        # We add one to the question numbers because the top number is ignored
        for i in range(1, int(self.question_numbers) + 1):
            self.ask_question(i)

        # We calculate the percentage
        percentage = self.score / int(self.question_numbers)
        percentage = percentage * 100

        print(f"Your score was {percentage}%")
        score = f"Your score was {percentage}%"
        # We tell the user their score
        message_dialog(title=f"{percentage}%", text=score).run()

        # We give the user a message based on how they did
        if percentage < 10:
            message_dialog(
                text="...\nLooks like you need to improve your maths skills..."
            ).run()
        elif percentage < 30:
            message_dialog(
                text="Maybe pay a bit more attention in class next time..."
            ).run()
        elif percentage < 50:
            message_dialog(
                text="You are getting there, but maybe need a bit more practice"
            ).run()
        elif percentage < 70:
            message_dialog(
                text="You are very close to a good score, but not there yet"
            ).run()
        elif percentage < 90:
            message_dialog(text="A good pass!").run()
        elif percentage < 99:
            message_dialog(
                text="This, here, is an extremely high score!").run()
        elif percentage == 100 and self.difficulty == "Impossible":
            # It is extremely unlikely to get this score without a calculator
            message_dialog(text="This score is that of a calculator").run()
        else:
            message_dialog(text="You are a perfectionist").run()
