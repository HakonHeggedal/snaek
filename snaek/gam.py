import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    pygame.init()
    fpss = pygame.time.Clock()

    pygame.display.set_caption("Snaek")
    icon = pygame.image.load("img/snaek_icon.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((240, 180), 0, 32)
    screen.fill(WHITE)
    running = True

    pygame.draw.rect(screen, BLUE, (20, 10, 10, 50))

    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("The up arrow key was pressed!")
                elif event.key == pygame.K_DOWN:
                    print("The down arrow key was pressed!")


if __name__ == "__main__":
    main()
