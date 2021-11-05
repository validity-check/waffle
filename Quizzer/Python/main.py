"""The main project file for the Quizzer App"""
# main.py
# -------------------------------------
# Quizzer App
# -------------------------------------
# Work of @validity-check
# Github: https://github.com/validity-check/QuizzerPy

# This is the library we will use to ask questions.
# We will use it because it will make the handling of
# invalid prompts easier and it will look more appealing
# to the user. It is also used in question_handler.py

from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, message_dialog
from prompt_toolkit.validation import ValidationError, Validator

# Import question_handler.py which exists to make main.py smaller
import question_handler


# We are creating a validator to check if the input the user it gives is valid
# It inherits the "Validator" class which means that prompt_toolkit can easily recognise it as a Validator
class NumberValidator(Validator):
    """Make sure the input is a number greater than 5"""

    # We need this function because we inherited Validator
    # The function will be run once input is entered
    # It will take one argument other than self, which is the thing to validate
    def validate(self, document):
        """Make sure the input is a number greater than 5"""
        # The actual text is stored in document.text
        text = document.text
        # This message is used twice which is why I made it a variable
        invalid_msg = "Please enter a valid integer greater than 5"
        try:
            # We want to first see if the input can be converted to an integer
            # If not, it will throw an error and we will fall back to the except statement below
            # We also want to make sure that the number is not less then 5. We do not want it to be negative and if the number is too low then it will be too easy to get 100%.
            if int(text) < 5:
                raise ValidationError(message=invalid_msg,
                                      cursor_position=document.cursor_position)
        except:
            # prompt_toolikt's ValidationError needs an invalid message to show to the user if their input is invalid
            # It also needs a position of where to place the cursor
            # Since we do not want to point to a specific position, we leave the cursor as is.
            raise ValidationError(message=invalid_msg,
                                  cursor_position=document.cursor_position)


# Display a welcoming message to the user
message_dialog(title="Welcome to Quizzer", text="Press OK to continue.").run()

# Ask questions required to start the quiz
# Firstly, we want to know how difficult the user wants to play and adjust the game accordingly
difficulty = radiolist_dialog(
    title="Difficulty",
    text="Which difficulty would you like to choose?",
    values=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"),
            ("Impossible", "Impossible")]).run()

# Then, we want to know how many questions the user wants to be asked
# We need to add a validator to make sure that the number is valid and greater then 5
# We need to make sure that the number is greater than 5 because otherwise a user would be able to go on to impossible mode and answer one question and then see a special 100% message
question_numbers = input_dialog(
    title="Number of questions",
    text="How many questions would you like to be asked",
    validator=NumberValidator()).run()

# We initialise the question_handler module, giving it the difficulty and the number of questions
ask_questions = question_handler.question_handler(difficulty,
                                                  question_numbers[0])

# We then let the question_handler module do the rest of the work for us by calling this function
ask_questions.ask_questions()
