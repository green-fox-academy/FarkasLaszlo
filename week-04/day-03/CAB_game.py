import random


class CAB:

    def __init__(self, game_state = 'playing', counter = 0, number = random.randint(1000, 9999)):
        self.game_state = game_state
        self.number = number
        self.counter = counter

    def guess(self, guess_number):
        self.counter += 1
        answer = []
        for i in range(4):
            if (guess_number // 10 ** i) % 10 == (self.number // 10 ** i) % 10:
                answer.append('cow')
            else:
                answer.append('bull')
        answer.reverse()
        if answer == ['cow', 'cow', 'cow', 'cow']:
            self.game_state = 'finished'
        return answer
