from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # file=open("Angelia\Day_19_20_SnakeGame\data.txt")
        # h_score=file.read()
        self.score=0
        with open("Angelia\Day_19_20_SnakeGame\data.txt") as data:
            content=data.read()
            self.high_score=int(content)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT) 

    def increase_score(self):
        self.score +=1
        #self.write(f"Score:{self.score}", align="center",font=("Arial",24,"normal")) 
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score>self.high_score:
            with open("Angelia\Day_19_20_SnakeGame\data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)


