import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ukuran layar
WIDTH = 800
HEIGHT = 600

# Kelas abstrak GameObject
class GameObject(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        pass

# Kelas Player yang mewarisi dari GameObject
class Player(GameObject):
    def __init__(self):
        super().__init__(RED, 50, 50)
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Kelas Projectile yang mewarisi dari GameObject
class Projectile(GameObject):
    def __init__(self, x, y):
        super().__init__(WHITE, 16, 16)
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# Kelas Enemy yang mewarisi dari GameObject
class Enemy(GameObject):
    def __init__(self):
        super().__init__(WHITE, 50, 50)
        self.rect.x = random.randrange(WIDTH - 50)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - 50)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 3)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Kelas Game
class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for _ in range(8):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.speed_x = -5
                    elif event.key == pygame.K_RIGHT:
                        self.player.speed_x = 5
                    elif event.key == pygame.K_SPACE:
                        projectile = Projectile(self.player.rect.centerx - 8, self.player.rect.top)
                        self.all_sprites.add(projectile)
                        self.projectiles.add(projectile)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.player.speed_x < 0:
                        self.player.speed_x = 0
                    elif event.key == pygame.K_RIGHT and self.player.speed_x > 0:
                        self.player.speed_x = 0

            self.all_sprites.update()
            # Cek tabrakan dengan enemy
            hits = pygame.sprite.groupcollide(self.enemies, self.projectiles, True, True)
            for hit in hits:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)

            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if hits:
                running = False

            screen.fill(BLACK)
            self.all_sprites.draw(screen)
            pygame.display.flip()

        pygame.quit()

# Fungsi main untuk memulai game
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
