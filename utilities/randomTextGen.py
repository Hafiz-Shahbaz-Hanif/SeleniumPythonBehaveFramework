import random
import string


class RandomTextGen:
    @staticmethod
    def randomText():
        ranText = ''.join(random.choices(string.ascii_letters, k=8))
        return ranText
