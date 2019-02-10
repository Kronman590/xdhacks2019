class Goals:

    def __init__(self, title):
        self.goalTitle = title
        self.goalDone = False

    def getGoal(self):
        return self.goalTitle

    def getFinished(self):
        return self.goalDone
