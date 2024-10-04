import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CENTERx, CENTERy = round(WIDTH * 0.5), round(HEIGHT * 0.5)
FONT = pygame.font.SysFont("Courier New", 24, True)
FONTxsmall = pygame.font.SysFont("Courier New", 18, False)
FONTsmall = pygame.font.SysFont("Courier New", 20, True)
FONTbig = pygame.font.SysFont("Courier New", 36, True)
COLOR = (123, 179, 255)
pygame.display.set_caption("Cookie Clicker")

CLOCK = pygame.time.Clock()
FPS = 60

COOKIE_IMAGE = pygame.image.load(os.path.join("data", "cookie.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("data", "upgrade.png"))
CLICKER_IMAGE = pygame.image.load(os.path.join("data", "mouse.png"))


class Button():
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.angle = 0
        self.clicked = False

    def draw(self):
        WINDOW.blit(self.image, (self.x - int(self.width / 2), self.y - int(self.height / 2)))

        action = False

        self.rect.x = self.x - int(self.width / 2)
        self.rect.y = self.y - int(self.height / 2)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and (pygame.mouse.get_pressed()[0] == 1 and not self.clicked):
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def drawRotate(self, speed):
        self.angle = self.angle + speed
        imageCopy = pygame.transform.rotate(self.image, self.angle)
        WINDOW.blit(imageCopy, (self.x - int(imageCopy.get_width() / 2), self.y - int(imageCopy.get_height() / 2)))

        action = False

        self.rect.x = self.x - int(self.width / 2)
        self.rect.y = self.y - int(self.height / 2)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and (pygame.mouse.get_pressed()[0] == 1 and not self.clicked):
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action


cookieButton = Button(CENTERx - 300, CENTERy + 50, COOKIE_IMAGE, 1)
upgradeButton = Button(1550, 460, UPGRADE_IMAGE, 0.15)
clickerButton = Button(1430, 800, CLICKER_IMAGE, 0.1)

cookieBalance = 0
highScore = 0
upgradesPurchased = 0
clickersPurchased = 0
cps = 0
cookiesPerClick = 0
second = True
pygame.time.set_timer(second, 1000)
upgradeCost = 0
clickerCost = 0


def gameText():
    global cookieBalance
    global highScore
    global cookiesPerClick
    global clickersPurchased
    global cps
    global cookiesPerClick
    global upgradeCost

    cookieBalanceText = FONTbig.render(f"Печенек:  {str(cookieBalance)}", False, (0, 0, 0))
    WINDOW.blit(cookieBalanceText, (215, 30))

    infoText1 = FONTxsmall.render("Кликай на печеньку, чтобы испечь печеньки", False, (0, 0, 0))
    WINDOW.blit(infoText1, (480, 670))

    infoText2 = FONTxsmall.render("Кликай на иконки Улучшения и Кликера, чтобы купить их", False, (0, 0, 0))
    WINDOW.blit(infoText2, (400, 690))

    upgradesinfoText1 = FONTsmall.render("Покупай Улучшение, чтобы", False, (0, 0, 0))
    WINDOW.blit(upgradesinfoText1, (720, 130))

    upgradesinfoText2 = FONTsmall.render("увеличить кол-во печенек за клик", False, (0, 0, 0))
    WINDOW.blit(upgradesinfoText2, (718, 160))

    upgradesPurchasedText = FONT.render(f"Куплено Улучшений: {str(upgradesPurchased)}", False, (0, 0, 0))
    WINDOW.blit(upgradesPurchasedText, (750, 250))

    upgradeCostText = FONT.render(f"Стоимость покупки Улучшения: {str(upgradeCost)}", False, (0, 0, 0))
    WINDOW.blit(upgradeCostText, (720, 190))

    clickerCostText = FONT.render(f"Стоимость покупки Кликера: {str(clickerCost)}", False, (0, 0, 0))
    WINDOW.blit(clickerCostText, (720, 460))

    clickersinfoText1 = FONTsmall.render("Покупай Кликеры, чтобы", False, (0, 0, 0))
    WINDOW.blit(clickersinfoText1, (720, 400))

    clickersinfoText2 = FONTsmall.render("увеличить авто-клик в секунду", False, (0, 0, 0))
    WINDOW.blit(clickersinfoText2, (718, 430))

    highScoreText = FONT.render(f"Рекорд печенек: {str(highScore)}", False, (0, 0, 0))
    WINDOW.blit(highScoreText, (10, 685))

    clickersPurchasedText = FONT.render(f"Куплено Кликеров: {str(clickersPurchased)}", False, (0, 0, 0))
    WINDOW.blit(clickersPurchasedText, (750, 540))

    cpsText = FONTsmall.render(f"Печенек в секунду: {str(cps)}", False, (0, 0, 0))
    WINDOW.blit(cpsText, (200, 150))

    cookiesPerClickText = FONTsmall.render(f"Печенек за клик: {str(cookiesPerClick)}", False, (0, 0, 0))
    WINDOW.blit(cookiesPerClickText, (215, 100))


def update_balances():
    global cookieBalance
    global highScore
    global cookiesPerClick
    global upgradeCost
    global clickerCost
    global cps

    cps = round(0.1 * clickersPurchased, 2)

    if pygame.event.get(second):
        cookieBalance = round((cookieBalance + cps), 2)

    cookiesPerClick = upgradesPurchased + 1

    if cookieBalance > highScore:
        highScore = round(cookieBalance, 2)

    if upgradesPurchased == 0:
        upgradeCost = 10
    else:
        upgradeCost = upgradesPurchased * 23 + 10
    clickerCost = 3 * (clickersPurchased + 1)


def draw_window():
    global cookieBalance
    global upgradesPurchased
    global clickersPurchased
    WINDOW.fill(COLOR)
    gameText()

    if cookieButton.drawRotate(-0.5):
        cookieBalance = round((cookieBalance + cookiesPerClick), 2)
    if upgradeButton.draw() and cookieBalance >= upgradeCost:
        upgradesPurchased += 1
        cookieBalance = round((cookieBalance - upgradeCost), 2)
    if clickerButton.draw() and cookieBalance >= clickerCost:
        clickersPurchased += 1
        cookieBalance = round((cookieBalance - clickerCost), 2)

    pygame.display.update()


def main():
    run = True
    while run:
        CLOCK.tick(FPS)
        update_balances()
        draw_window()

        # Event handler
        for event in pygame.event.get():

            # Quit game
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
