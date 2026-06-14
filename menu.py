import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

        self.operations = [
            ("Penjumlahan", "ADD"),
            ("Pengurangan", "SUB"),
            ("Perkalian", "MUL"),
            ("Pembagian", "DIV"),
        ]

        self.modes = [
            ("Easy", "EASY"),
            ("Medium", "MEDIUM"),
            ("Hard", "HARD")
        ]

    def run(self):
        selected = 0

        # ====================
        # PILIH OPERASI
        # ====================
        while True:
            self.screen.fill((0, 0, 0))

            title = pygame.font.SysFont(None, 44).render(
                "Pilih Operasi Matematika", True, (0, 255, 255)
            )
            self.screen.blit(title, (100, 120))

            for i, (label, _) in enumerate(self.operations):
                color = (255, 255, 0) if i == selected else (255, 255, 255)
                text = self.font.render(label, True, color)
                self.screen.blit(text, (220, 200 + i * 40))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(self.operations)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(self.operations)
                    elif event.key == pygame.K_RETURN:
                        operation = self.operations[selected][1]
                        break
            else:
                continue
            break

        # ====================
        # PILIH MODE
        # ====================
        selected = 0

        while True:
            self.screen.fill((0, 0, 0))

            title = pygame.font.SysFont(None, 44).render(
                "Pilih Mode", True, (255, 100, 255)
            )
            self.screen.blit(title, (180, 120))

            for i, (label, _) in enumerate(self.modes):
                color = (255, 255, 0) if i == selected else (255, 255, 255)
                text = self.font.render(label, True, color)
                self.screen.blit(text, (260, 200 + i * 40))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(self.modes)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(self.modes)
                    elif event.key == pygame.K_RETURN:
                        mode = self.modes[selected][1]
                        return operation, mode