import pygame
from snake import Snake
from food import AddFood, SubFood, MulFood, DivFood
from score import ScoreManager
from menu import Menu
from gameover import GameOverScreen 

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20


class StartScreen:
    def __init__(self, screen):
        self.selected_snake = {
            "color": (0,255,0),
            "img": "assets/snake1.png"
        }
        self.screen = screen
        self.font_title = pygame.font.SysFont(None, 72)
        self.font_button = pygame.font.SysFont(None, 40)

        #  FONT KHUSUS INSTRUCTION (LEBIH KECIL)
        self.font_instruction = pygame.font.SysFont(None, 30)

        try:
            self.font_emoji = pygame.font.SysFont("Segoe UI Emoji", 40)
        except:
            self.font_emoji = self.font_button

        
        self.show_color_menu = False

    def run(self):
        while True:
            self.screen.fill((30, 30, 30))

            # Judul
            title = self.font_title.render("SNAKE MATH", True, (0, 255, 200))
            self.screen.blit(title, (130, 150))

            # Start
            mulai_rect = pygame.Rect(230, 300, 140, 50)
            pygame.draw.rect(self.screen, (0, 150, 255), mulai_rect)
            text = self.font_button.render("Mulai", True, (255, 255, 255))
            self.screen.blit(text, (mulai_rect.x + 30, mulai_rect.y + 10))

            # Instruction (LEBIH KECIL )
            petunjuk_rect = pygame.Rect(230, 370, 140, 50)
            pygame.draw.rect(self.screen, (100, 100, 255), petunjuk_rect)
            text2 = self.font_instruction.render("Petunjuk", True, (255, 255, 255))
            self.screen.blit(text2, (petunjuk_rect.x + 15, petunjuk_rect.y + 12))

            # Tombol ular
            ular_rect = pygame.Rect(230, 440, 140, 50)
            pygame.draw.rect(self.screen, (150, 150, 150), ular_rect)

            try:
                text3 = self.font_emoji.render("🐍", True, (0, 0, 0))
            except:
                text3 = self.font_button.render("Snake", True, (0, 0, 0))

            self.screen.blit(text3, (ular_rect.x + 45, ular_rect.y + 8))

            # Pilihan warna
            colors = [
            {"color": (255,0,0), "img": "assets/snake3.png", "x":180},
            {"color": (255,255,0), "img": "assets/snake2.png", "x":240},
            {"color": (0,255,0), "img": "assets/snake1.png", "x":300},
            {"color": (0,0,255), "img": "assets/snake4.png", "x":360}
]

            if self.show_color_menu:
                for data in colors:
                    color = data["color"]
                    x = data["x"]

                    rect = pygame.Rect(x, 510, 40, 40)
                    pygame.draw.rect(self.screen, color, rect)

                    if self.selected_snake == data:
                        pygame.draw.rect(self.screen, (255,255,255), rect, 3)

                    if pygame.mouse.get_pressed()[0]:
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            self.selected_snake = data

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mulai_rect.collidepoint(event.pos):
                        return self.selected_snake

                    if petunjuk_rect.collidepoint(event.pos):
                        self.show_petunjuk()

                    if ular_rect.collidepoint(event.pos):
                        self.show_color_menu = not self.show_color_menu

    def show_petunjuk(self):
        while True:
            self.screen.fill((20, 20, 20))
            font = pygame.font.SysFont(None, 28)

            lines = [
                "Gunakan tombol panah untuk bergerak",
                "Makan jawaban yang benar",
                "Jawaban salah = Permainan berakhir",
                "Hindari tabrakan dengan dinding atau tubuh ular",
                "Tekan ESC untuk kembali"
            ]

            for i, line in enumerate(lines):
                text = font.render(line, True, (255, 255, 255))
                self.screen.blit(text, (80, 150 + i * 40))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return


class Game:
    def __init__(self):
        pygame.init()
        
        pygame.mixer.music.load("jawa.mp3")  # music game
        pygame.mixer.music.play(-1)
        
        self.selected_snake = {
            "color": (0,255,0),
            "img": "assets/snake1.png"
        }

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Math")
        self.clock = pygame.time.Clock()

        # Start screen
        start_screen = StartScreen(self.screen)
        self.snake_data = start_screen.run()

        # Menu
        self.menu = Menu(self.screen)
        self.operation, self.mode = self.menu.run()

        # Mode setting
        if self.mode == "EASY":
            self.speed = 6
            self.food_count = 1
        elif self.mode == "MEDIUM":
            self.speed = 10
            self.food_count = 1
        elif self.mode == "HARD":
            self.speed = 14
            self.food_count = 3

        self.snake = Snake(self.snake_data)
        food_classes = {
            "ADD": AddFood,
            "SUB": SubFood,
            "MUL": MulFood,
            "DIV": DivFood
        }

        self.food = food_classes[self.operation](self.food_count)
        self.score_manager = ScoreManager()

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            if self.mode == "EASY":
                speed = self.speed

            elif self.mode == "MEDIUM":
                speed = self.speed + len(self.snake.body) // 8

            elif self.mode == "HARD":
                speed = 6 + len(self.snake.body) // 2

            self.clock.tick(speed)

        game_over = GameOverScreen(
            self.screen,
            self.score_manager.score
        )

        result = game_over.show()

        if result == "restart":
            self.__init__()
            self.run()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.snake.change_direction(keys)

    def update(self):
        self.snake.move()

        for food in self.food.foods:
            if self.snake.head_position() == food["pos"]:

                if food["correct"]:
                    self.snake.grow()
                    self.score_manager.add_score()
                else:
                    self.running = False

                self.food.respawn(self.snake.body)
                break

        if self.snake.check_collision():
            self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.score_manager.draw(self.screen)

        font = pygame.font.SysFont(None, 32)
        question = font.render(
            f"Soal: {self.food.question}",
            True,
            (255, 255, 255)
        )
        self.screen.blit(question, (200, 10))
        pygame.display.update()
