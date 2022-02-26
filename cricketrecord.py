class cricket:
    def detail(self):
        self.score1=input('enter the score of team1:')
        self.score2=input('enter the score of team2:')
    def display(self):
             print(f"The score of team 1 is {self.score1} and the score of team 2 is {self.score2}.")
a=cricket()
a.detail()
a.display()