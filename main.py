import pygame, sys
from pygame.locals import *
import random

pygame.init()



game_clock = pygame.time.Clock()


#loading the background music
pygame.mixer.music.load('background - Copy.mp3')
pygame.mixer.music.play()


#loading the lossing music
game_over_sound = pygame.mixer.Sound('game_over - Copy.mp3')


GameWindow = pygame.display.set_mode(
    (600, 600),
    0,
    32,
)

pygame.display.set_caption('Taklif')




Font = pygame.font.SysFont('comicsans', 21)

end_text = Font.render('Game Over . press R to try again', True, (255, 0, 0))



#end_text_score_Font = pygame.font.SysFont('comicsans', 21)
#end_text_score = end_text_score_Font.render()



score_text_Font = pygame.font.SysFont('comicsans', 20)
score_text = score_text_Font.render('score:', True, (0 ,0 ,0))

 
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (600, 600))


player_png = pygame.image.load('player.png')
player_png = pygame.transform.scale(player_png, (60, 60))


squares = []

player_position_x = 350
player_position_y = 300

counter = 10



is_game_over = False



score_count = 0
best_score = 0


while True:
    for event in pygame.event.get():             #===============================
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()


    score_text = score_text_Font.render(str(score_count), True, (0,0,0))

    if is_game_over == True:
        GameWindow.fill([0, 0, 0])
        GameWindow.blit(end_text, [140, 300])
        end_score_text = score_text_Font.render(f'your score is:{score_count}', True, (250,255,0))
        end_best_score_text = score_text_Font.render(f'best score:{best_score}', True, (250,250,0))
        
        GameWindow.blit(end_score_text, [20, 30])
        GameWindow.blit(end_best_score_text, [20, 80])
        
        if score_count > best_score:
            best_score = score_count


        clicked_keys = pygame.key.get_pressed()
        if clicked_keys[K_r]:
            is_game_over = False
            score_count = 0
            squares = []
            player_position_x = 350
            player_position_y = 300
            counter = 10
            pygame.mixer.music.play()
    else:
           
        GameWindow.blit(background_image, (0, 0))

        score_text = score_text_Font.render(f'your score is:{score_count}', True, (0,0,0))
        best_score_text = score_text_Font.render(f'best score:{best_score}', True, (0,0,0))

        GameWindow.blit(score_text, [20, 30])
        GameWindow.blit(best_score_text, [20, 80])


        # GameWindow.fill(
        #     (0, 255, 247)
        # )


        clicked_keys = pygame.key.get_pressed()
        
        if clicked_keys[K_UP]:
            player_position_y -= 10
        if clicked_keys[K_DOWN]:
            player_position_y += 10
        if clicked_keys[K_RIGHT]:
            player_position_x += 10
        if clicked_keys[K_LEFT]:
            player_position_x -= 10           

        GameWindow.blit(player_png, [player_position_x, player_position_y])
        


        player_rect = pygame.Rect(
            player_position_x, player_position_y,
            70, 70,

        )

        

        
        counter  -= 1
        if counter < 0 :

            new_squares = {
            'x': random.randint(0, 700),
            'y': -100,
            'speed': random.randint(1, 10)   
            }
            squares.append(new_squares)
            counter = 10

                                                                            

        for square in squares:
            square['y'] += square['speed']
            if square['y'] > 600:
                squares.remove(square)
                score_count += 1
            else:
                square_rect = pygame.Rect(
                    square['x'] , square['y'] , 40 , 40
                )

                hamburger_image = pygame.image.load('hamburger.png')
                hamburger_image = pygame.transform.scale(hamburger_image, (40 , 40))
                GameWindow.blit(hamburger_image, [square['x'] , square['y']])

                if player_rect.colliderect(square_rect):
                    is_game_over = True
                    pygame.mixer.music.stop()
                    game_over_sound.play()
    

    game_clock.tick(30)

    
    pygame.display.update()