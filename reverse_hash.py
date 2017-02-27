# Python 3 Loktra reverse hash
class Loktra:
    def __init__(self):
        self.letters = 'acdegilmnoprstuw'

    # hash algorithm
    def hash(self, s):
        h = 7
        for i in s:
            h = (h * 37 + self.letters.index(i))
        return h

    # reverse hash algorithm
    def reverse_hash(self, h):
        s = ""
        while h != 7:
            for i in range(len(self.letters)):
                if (h - i) % 37 == 0:
                    s = self.letters[i] + s
                    h = (h - i) / 37
                    break
        return s

from unittest import TestCase, main

class LoktraTests(TestCase):
    def test_reverse_hash(self):
        self.assertTrue(Loktra().reverse_hash(680131659347) == 'leepadg')

if __name__ == "__main__":
    print(Loktra().reverse_hash(930846109532517))
    main()