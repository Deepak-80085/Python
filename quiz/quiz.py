import random

class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0
    
    def add_question(self, question, options, correct_answer):
        """Add a question to the quiz."""
        self.questions.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })
    
    def load_default_questions(self):
        """Load some default questions into the quiz."""
        self.add_question(
            "What is the capital of France?",
            ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
            "C"
        )
        self.add_question(
            "Which planet is known as the Red Planet?",
            ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "B"
        )
        self.add_question(
            "What is 2 + 2?",
            ["A. 3", "B. 4", "C. 5", "D. 6"],
            "B"
        )
        self.add_question(
            "Who wrote 'Romeo and Juliet'?",
            ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
            "B"
        )
        self.add_question(
            "What is the largest ocean on Earth?",
            ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "D"
        )
        
    def display_question(self, question_data):
        """Display a single question with its options."""
        print("\n" + question_data['question'])
        for option in question_data['options']:
            print(option)
        
        user_answer = input("\nYour answer (A/B/C/D): ").upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.c")
            user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == question_data['correct_answer']:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['correct_answer']}.")
        
        self.total_questions += 1
    
    def play_round(self):
        """Play a round of the quiz game with all available questions."""
        if not self.questions:
            print("No questions available. Please add questions first.")
            return
        
        self.score = 0
        self.total_questions = 0
        
        # Shuffle questions for variety
        random.shuffle(self.questions)
        
        for question in self.questions:
            self.display_question(question)
        
        print(f"\nQuiz completed! Your score: {self.score}/{self.total_questions}")
        print(f"Percentage: {(self.score/self.total_questions)*100:.2f}%")
    
    def add_custom_question(self):
        """Allow the user to add their own question."""
        question = input("Enter your question: ")
        
        options = []
        print("Enter 4 options (A, B, C, D):")
        options.append("A. " + input("A: "))
        options.append("B. " + input("B: "))
        options.append("C. " + input("C: "))
        options.append("D. " + input("D: "))
        
        correct_answer = input("Enter the correct option (A/B/C/D): ").upper()
        while correct_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            correct_answer = input("Enter the correct option (A/B/C/D): ").upper()
        
        self.add_question(question, options, correct_answer)
        print("Question added successfully!")

def main():
    print("Welcome to the Interactive Quiz Game!")
    quiz = QuizGame()
    quiz.load_default_questions()
    
    while True:
        print("\nMENU:")
        print("1. Play Quiz")
        print("2. Add Custom Question")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            quiz.play_round()
        elif choice == '2':
            quiz.add_custom_question()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()