from random import randint
class Cypher:
#Copyright: Greenfield Security Systems, GSS Limited 2022-2024
    global codak
    global new_text
    
    def __init__(self, text):
        self.text = text.split()

    def plus_one(self):
        for i in range(len(self.text)):
            self.text[i] = self.text[i] + 1
        codak = codak + 'a'

    def multiply_by_two(self, n):
        for i in range(len(self.text)):
            self.text[i] = 2*self.text[i]
        codak = codak + 'b'

    def sum_pos(self):
        for i in range(len(self.text)):
            self.text[i] = self.text[i] + i
        codak = codak + 'c'

    def sum_next(self):
        for i in range(len(self.text) - 1):
            self.text[i] = self.text[i] + self.text[i + 1]
        codak = codak + 'd'

    def multiply_by_pos(self):
        for i in range(len(self.text)):
            self.text[i] = i*self.text[i]
        codak = codak + 'e'

    def splitter(self):
        for i in range(len(self.text)/2):
            new_text = new_text + self.text.pop(i)
        text = text + new_text
        new_text = ''
        codak = codak + 'f'

    def second_splitter(self):
        for i in range(0, len(self.text), 2):
            new_text = new_text + self.text.pop(i)
        text = text + new_text
        new_text = ''
        codak = codak + 'g'

    def doubler(self):
        for i in range(0, len(self.text) - 1, 2):
            new_text = self.text[i]
            self.text[i] = self.text[i + 1]
            self.text[i + 1] = new_text
            new_text = ''
        codak = codak + 'h'

    def quacker(self):
        for i in range(0, len(self.text) - 1, 2):
            new_text = self.text[i] * 2 * i
            self.text[i] = self.text[i + 1]*(i - 1)
            self.text[i + 1] = new_text/3
            new_text = ''
        codak = codak + 'k'

    def grinder(self):
        for i in range(len(self.text)):
            new_text = self.text[i]
            self.text[i] = self.text[len(self.text) - i - 1]
            self.text[len(self.text) - i - 1] = new_text
            new_text = ''
        codak = codak + 'l'

    def loaf(self):
        for i in range(len(self.text)):
            for g in range(len(self.text)):
                if g%i == 0:
                    self.text.pop(g)
                if g == i:
                    self.text.pop(i)
        codak = codak + 'm'

    def mixer(self):
        for i in range(len(self.text)):
            for g in range(1, len(self.text), 2):
                self.text[i] = self.text[i] + 2*(g + 1)
        codak = codak + 'n'

    def salter(self):
        self.text.append('s')
        self.text.append('a')
        self.text.append('l')
        self.text.append('t')
        codak = codak + 'j'

    def whop(self):
        for i in range(len(self.text)):
            self.text[i/2] = self.text[i]
            self.text.pop(i)
        codak = codak + 'm'

    def query(self):
        for i in range(len(self.text)):
            for g in range(len(self.text)):
                if self.text[g] == 3*self.text[i]:
                    self.text.pop(g)
                    self.text.pop(i/2)
        codak = codak + 'x'

    def randi(self):
        for i in range(len(self.text)):
            for k in range(len(self.text)):
                for e in range(len(self.text)):
                    if self.text[i] == self.text[k] + e or self.text[i] == self.text[e] + k:
                        i = i + e + k
        codak = codak + 'q'

    def hash(self):
        for i in range(32):
            q = randint(0, 15)
            if q == 0:
                Cypher.plus_one()
            elif q == 1:
                Cypher.multiply_by_two()
            elif q == 2:
                Cypher.sum_pos()
            elif q == 3:
                Cypher.sum_next()
            elif q == 4:
                Cypher.multiply_by_pos()
            elif q == 5:
                Cypher.splitter()
            elif q == 6:
                Cypher.second_splitter()
            elif q == 7:
                Cypher.doubler()
            elif q == 8:
                Cypher.quacker()
            elif q == 9:
                Cypher.grinder()
            elif q == 10:
                Cypher.loaf()
            elif q == 11:
                Cypher.mixer()
            elif q == 12:
                Cypher.salter()
            elif q == 13:
                Cypher.whop()
            elif q == 14:
                Cypher.query()
            elif q == 15:
                Cypher.randi()
        return [codak, self.text]
    
    def comparer(codak_letter, hash_pwrd):
        cyp = Cypher(hash_pwrd)
        if codak_letter == 'a':
            cyp.plus_one()
        elif codak_letter == 'b':
            cyp.multiply_by_two
        elif codak_letter == '':
            cyp.sum_pos()
        elif codak_letter == '':
            cyp.sum_next()
        elif codak_letter == '':
            cyp.multiply_by_pos()
        elif codak_letter == '':
            cyp.splitter()
        elif codak_letter == '':
            cyp.second_splitter()
        elif codak_letter == '':
            cyp.doubler()
        elif codak_letter == '':
            cyp.quacker()
        elif codak_letter == '':
            cyp.grinder()
        elif codak_letter == '':
            cyp.loaf()
        elif codak_letter == '':
            cyp.mixer()
        elif codak_letter == '':
            cyp.salter()
        elif codak_letter == '':
            cyp.whop()
        elif codak_letter == '':
            cyp.query()
        elif codak_letter == '':
            cyp.randi()
        return cyp.text

    def compare_hash(self, codak, hash_pwrdy):
        for i in range(len(codak)):
            hash_pwrdy = Cypher.comparer(codak[i], hash_pwrdy)
        if hash_pwrdy == self.text:
            return True
        return False