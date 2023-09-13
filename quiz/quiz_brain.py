class QuizBrain:
    def __init__(self,question):
        self.question_number=0
        self.score=0
        self.question_list=question 

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}:{current.text}(True/False):")
        self.check_answer(user_answer,current.answer)


    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score +=1
            print("You are right")
        else:
            print("Wrong Answer")
        print(f"/nTo correct answer was:{correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")

