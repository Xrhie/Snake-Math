import pygame

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score

    def show(self):
        while True:
            self.screen.fill((10, 10, 10))

            font_big = pygame.font.SysFont(None, 60)
            font_mid = pygame.font.SysFont(None, 40)
            font_small = pygame.font.SysFont(None, 28)

            text = font_big.render("GAME OVER", True, (255, 0, 0))
            self.screen.blit(text, (140, 200))

            try_again = font_mid.render(
                "Try Again?",
                True,
                (255, 255, 255)
            )
            self.screen.blit(try_again, (200, 270))

            score_text = font_small.render(
                f"Score: {self.score}",
                True,
                (200, 200, 200)
            )
            self.screen.blit(score_text, (240, 330))

            info = font_small.render(
                "R = Restart | ESC = Exit",
                True,
                (150, 150, 150)
            )
            self.screen.blit(info, (190, 370))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                        return "restart"

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()