# Initialize questions and answers
question_data = [
                {"text": "A slug's blood is green.", "answer": "True"},
                {"text": "The loudest animal is the African Elephant.", "answer": "False"},
                {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
                {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
                {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
                {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
                {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
                {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
                {"text": "Google was originally called 'Backrub'.", "answer": "True"},
                {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
                {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
                {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


# Make a question class that holds the question and associated answer
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# Create the quiz master class
class QuizMaster:
    # Initialize quiz master with question number, score and question bank
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # Method to check answer
    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            return True
        else:
            return False

    # Method to ask the next question and increment the question counter
    def next_question(self):
        next_Q = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1} {next_Q.text} (True/False)? ").lower()
        self.question_number += 1
        correct = self.check_answer(answer, next_Q.answer)

        if correct:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")

    # Method to check if there are still questions left
    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else: 
            return True


# Make a question bank to start off
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

# Initialize an instance of the quiz master with the question bank
my_QM = QuizMaster(question_bank)

# Run quiz while there are still questions left to ask
while my_QM.still_has_question():
    my_QM.next_question()
    print('\n')

# Output final score
print("Well done - you've completed the quiz!")
print(f"Your final score is {my_QM.score} out of {len(my_QM.question_list)}.")