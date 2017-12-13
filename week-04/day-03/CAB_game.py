import random


class CAB:
    list_digit = []

    def __init__(self, game_state="playing", counter=0, number=random.randint(1000,9999)):
        self.game_state = game_state
        self.number = number
        self.counter = counter
        for i in range(4):
            self.list_digit.append((self.number//10**i) % 10)

    def guess(self, guess_number):
        self.counter += 1
        answer = []
        for i in range(4):
            if (guess_number//10**i) % 10 == self.list_digit[i]:
                answer.append("cow")
            else:
                answer.append("bull")
        answer.reverse()
        if answer == ["cow","cow","cow","cow"]:
            self.game_state = "finished"
        return answer
