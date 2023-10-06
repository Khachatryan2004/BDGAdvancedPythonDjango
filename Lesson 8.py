import random


class HarryPotter:
    def __init__(self, magic_words):
        self.magic_words = magic_words

    def game_process(self):
        score = 0
        for i in range(3):
            magic_word = input('Your magic word:\t').lower()
            lord_voldemort_word = random.choice(magic_words)

            if magic_word == lord_voldemort_word.lower():
                score += 1
                print(f"Lord Voldemort word is: {lord_voldemort_word}.")
            else:
                score -= 1
                print(f"Lord Voldemort word is: {lord_voldemort_word}.")

        if score >= 2:
            print("You win")
        else:
            print("You lose")


magic_words = ['Avada Kedavra', 'Crucio', 'Imperio']
harry_potter = HarryPotter(magic_words)
harry_potter.game_process()
