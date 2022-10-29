import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
# base_font = pygame.font.Font(None,50)
# input_rect = pygame.Rect(360,300,140,36)
# colur = pygame.Color("lightskyblue3")
img = pygame.image.load("C:\\Users\HP\\Desktop\\box.jpg")
img_react = img.get_rect()
imgO = pygame.image.load("C:\\Users\HP\\Desktop\\O2.png")
O_react = imgO.get_rect()
imgX = pygame.image.load("C:\\Users\HP\\Desktop\\X.png")
X_react = imgX.get_rect()
user_text = ''
activate = True
a = ""
while activate:

    # text_surface = base_font.render(user_text, True, (255, 255, 255))
    # screen.fill((255, 0, 0))
    # screen.blit(img, (0,0))
    # pygame.draw.rect(screen, colur, input_rect, 4)
    # screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # input_rect.w = max(text_surface.get_width() + 10, 78)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activate = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # screen.blit(imgO, (95, 400))
                a = a + "o1"
            if event.key == pygame.K_2:
                # screen.blit(imgO, (95, 400))
                x_o = 279
                y_o = 406
                a = a + "o2"
            if event.key == pygame.K_3:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o3"
            if event.key == pygame.K_4:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o4"
            if event.key == pygame.K_5:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o5"
            if event.key == pygame.K_6:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o6"
            if event.key == pygame.K_7:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o7"
            if event.key == pygame.K_8:
                # screen.blit(imgO, (95, 400))
                x_o = 93
                y_o = 404
                a = a + "o8"

            if event.key == pygame.K_9:
                x_x = 93
                y_x = 404
                a = a + "o9"
            # for j in range(1,10):
            #     if event.key == pygame.K_(j):
            #         x_x = 93
            #         y_x = 404
            #         a = a + "x"
    # screen.fill((255, 0, 0))
    screen.blit(img, (0, 0))
    # if a == "o":
    #     screen.blit(imgO, (93,404))
    # elif a == "x":
    #     screen.blit(imgX, (x_x, y_x))
    for j in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        d = "o" + j
        d1 = d + j
        c = []
        c.append(j)
        if d in a:
            if "1" in c:
                screen.blit(imgO, (93, 404))
            if "2" in c:
                screen.blit(imgO, (279, 406))
            if "3" in c:
                screen.blit(imgO, (455, 404))
            # if a in ("o",j):
            #     screen.blit(imgO, (93, 404))
            # if a in ("o",j):
            #     screen.blit(imgO, (93, 404))
            # if a in ("o",j):
            #     screen.blit(imgO, (93, 404))
        pygame.display.update()
