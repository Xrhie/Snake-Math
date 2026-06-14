import pygame
import random
from abc import ABC, abstractmethod
from interface import Drawable

CELL_SIZE = 20


# ABSTRACT CLASS
class Food(Drawable, ABC):
    def __init__(self, count):
        self.count = count
        self.foods = []
        self.respawn([])

    @abstractmethod
    def generate_question(self):
        pass

    def respawn(self, snake_body):
        self.foods = []

        # soal baru dari subclass
        self.correct_value, self.question = self.generate_question()

        # jumlah makanan sesuai mode
        values = [self.correct_value]

        while len(values) < self.count:
            wrong = self.correct_value + random.randint(-5, 5)

            if wrong != self.correct_value and wrong not in values:
                values.append(wrong)

        random.shuffle(values)

        # buat posisi makanan
        for val in values:
            while True:
                pos = (
                    random.randrange(0, 600, CELL_SIZE),
                    random.randrange(0, 600, CELL_SIZE)
                )

                if pos not in snake_body and pos not in [f["pos"] for f in self.foods]:
                    break

            self.foods.append({
                "pos": pos,
                "value": val,
                "correct": val == self.correct_value
            })

    def draw(self, screen):
        font = pygame.font.SysFont(None, 20)

        for food in self.foods:
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (*food["pos"], CELL_SIZE, CELL_SIZE)
            )

            text = font.render(
                str(food["value"]),
                True,
                (255, 255, 255)
            )

            screen.blit(
                text,
                (food["pos"][0] + 4, food["pos"][1] + 2)
            )


# SUBCLASS 1
class AddFood(Food):
    def generate_question(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        hasil = a + b
        soal = f"{a} + {b}"

        return hasil, soal


# SUBCLASS 2
class SubFood(Food):
    def generate_question(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        if b > a:
            a, b = b, a

        hasil = a - b
        soal = f"{a} - {b}"

        return hasil, soal


# SUBCLASS 3
class MulFood(Food):
    def generate_question(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        hasil = a * b
        soal = f"{a} × {b}"

        return hasil, soal
    

# SUBCLASS 4
class DivFood(Food):
    def generate_question(self):
        hasil = random.randint(1, 9)
        pembagi = random.randint(1, 9)
        angka = hasil * pembagi

        soal = f"{angka} ÷ {pembagi}"
        return hasil, soal