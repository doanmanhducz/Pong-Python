import pygame, sys, random

# Define the scale_image function here
# def scale_image(image, width, height):
#     image_ratio = image.get_width() / image.get_height()
#     screen_ratio = width / height
#     if screen_ratio < image_ratio:
#         scale = width / image.get_width()
#     else:
#         scale = height / image.get_height()
#     return pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

screen_width = 1280
screen_height = 800

initial_ball_speed = 6  # Reset the ball speed
# Store the original size of the bars
original_bar_height = 100
player1 = pygame.Rect(50, screen_height // 2, 10, original_bar_height)
player2 = pygame.Rect(screen_width - 50, screen_height // 2, 10, original_bar_height)

# Store the original size of the ball
original_ball_size = 20
ball = pygame.Rect(screen_width // 2 - 10, screen_height // 2 - 10, original_ball_size, original_ball_size)

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x = initial_ball_speed  # Reset the ball speed
    ball_speed_y = initial_ball_speed  # Reset the ball speed
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])

def point_won(winner):
    global ball_speed, player2_points, player1_points

    if winner == "player2":
        player2_points += 1
    if winner == "player1":
        player1_points += 1
    ball_speed = initial_ball_speed
    # Reset the bar sizes
    player1.height = original_bar_height
    player2.height = original_bar_height

    # Reset the size of the ball
    ball.width = original_ball_size
    ball.height = original_ball_size
    
    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.colliderect(item):
        ball_speed_x *= 1.2
        ball_speed_y *= 1.2
        # Move the item to a new random position
        item.x = random.randint(0, screen_width)
        item.y = random.randint(0, screen_height)

    if ball.colliderect(item2):
        ball_speed_x *= 0.8
        ball_speed_y *= 0.8
        item2.x = random.randint(0, screen_width)
        item2.y = random.randint(0, screen_height)

    if ball.colliderect(item3):
        ball_speed_y *= -1
        item3.x = random.randint(0, screen_width)
        item3.y = random.randint(0, screen_height)

    # if ball.colliderect(item4):
    #     # Double the points for the winner
    #     if ball_speed_x > 0:  # Ball is moving to the right, player2 wins
    #         player2_points += 2
    #     else:  # Ball is moving to the left, player1 wins
    #         player1_points += 2
    #     # End the round and start a new one
    #     ball.center = (screen_width // 2, screen_height // 2)  # Reset the ball's position
    #     ball_speed_y = 3 if random.choice((0, 1)) == 0 else -3  # Reset the ball's speed
    #     ball_speed_x = 3 if random.choice((0, 1)) == 0 else -3  # Reset the ball's speed
    #     player1.center = (50, screen_height // 2)  # Reset player1's position
    #     player2.center = (screen_width - 50, screen_height // 2)  # Reset player2's position

    #     # Move the fourth item to a new random position
    #     item4.x = random.randint(0, screen_width)
    #     item4.y = random.randint(0, screen_height)

    if ball.colliderect(item5):
        # Increase the length of the player's bar by 1.5 times
        if ball_speed_x > 0:  # Ball is moving to the right, player2's bar increases
            player2.height *= 1.5
        else:  # Ball is moving to the left, player1's bar increases
            player1.height *= 1.5
        item5.x = random.randint(0, screen_width)
        item5.y = random.randint(0, screen_height)

    if ball.colliderect(item6):
        if ball_speed_x > 0:
            player1.height *= 0.75
        else:
            player2.height *= 0.75
        item6.x = random.randint(0, screen_width)
        item6.y = random.randint(0, screen_height)

    if ball.colliderect(item7):
        # Increase the size of the ball by 1.5 times
        ball.width *= 1.5
        ball.height *= 1.5
        item7.x = random.randint(0, screen_width)
        item7.y = random.randint(0, screen_height)
    
    if ball.colliderect(item8):
        # Decrease the size of the ball by 0.75 times
        ball.width *= 0.75
        ball.height *= 0.75
        item8.x = random.randint(0, screen_width)
        item8.y = random.randint(0, screen_height)

    if ball.colliderect(item9):
        # Create a new ball
        ball2 = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
        ball2_active = True
        item9.x = random.randint(0, screen_width)
        item9.y = random.randint(0, screen_height)

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        point_won("player2")

    if ball.left <= 0:
        point_won("player1")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        

def animate_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.y += player1_speed
    if keys[pygame.K_DOWN]:
        player1.y += player1_speed

    if keys[pygame.K_w]:
        player2.y -= player2_speed
    if keys[pygame.K_s]:
        player2.y += player2_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

pygame.mixer.init()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!")

clock = pygame.time.Clock()

ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

player2 = pygame.Rect(0,0,20,100)
player2.centery = screen_height/2

player1 = pygame.Rect(0,0,20,100)
player1.midright = (screen_width, screen_height/2)


ball_speed_x = 6
ball_speed_y = 6
player1_speed = 0
player2_speed = 6

player2_points, player1_points = 0, 0

score_font = pygame.font.Font(None, 100)

#Load background
background_image = pygame.image.load('img/background1.jpg').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load the bar image
# bar_width = 100  # Define the width of the bar
# bar_height = 20  # Define the height of the bar
# bar1_image = pygame.image.load('img/bar.png').convert_alpha()
# bar1_image = pygame.transform.scale(bar1_image, (bar_width, bar_height))  # Adjust the size to fit your bar

# bar2_image = pygame.image.load('img/bar.png').convert_alpha()
# bar2_image = pygame.transform.scale(bar2_image, (bar_width, bar_height))  # Adjust the size to fit your bar


# Load the item image
item_image = pygame.image.load('img/tangtoc.jpg')
item_image = pygame.transform.scale(item_image, (30, 30)).convert_alpha()

# Create the item
item = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the second item image
item2_image = pygame.image.load('img/giamtoc.jpg')
item2_image = pygame.transform.scale(item2_image, (30, 30)).convert_alpha()

# Create the second item
item2 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the third item image
item3_image = pygame.image.load('img/doihuong.png')
item3_image = pygame.transform.scale(item3_image, (30, 30)).convert_alpha()

# Create the third item
item3 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# # Load the fourth item image
# item4_image = pygame.image.load('img/x2diem.png')
# item4_image = pygame.transform.scale(item4_image, (30, 30)).convert_alpha()

# # Create the fourth item
# item4 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the fifth item image
item5_image = pygame.image.load('img/x2diem.png')
item5_image = pygame.transform.scale(item5_image, (30, 30)).convert_alpha()

# Create the fifth item
item5 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the sixth item image
item6_image = pygame.image.load('img/smallerbar.png')
item6_image = pygame.transform.scale(item6_image, (30, 30)).convert_alpha()

# Create the sixth item
item6 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the seventh item image
item7_image = pygame.image.load('img/bigball.png')
item7_image = pygame.transform.scale(item7_image, (30, 30)).convert_alpha()

# Create the seventh item
item7 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the eighth item image
item8_image = pygame.image.load('img/smallball.png')
item8_image = pygame.transform.scale(item8_image, (30, 30)).convert_alpha()

# Create the eighth item
item8 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the nineth item image
item9_image = pygame.image.load('img/plusball.png')
item9_image = pygame.transform.scale(item9_image, (30, 30)).convert_alpha()

# Create the nineth item
item9 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

#Load and play backkground music:
pygame.mixer.music.load('sounds/background_music.mp3')
pygame.mixer.music.play(-1)  # The -1 makes the music loop indefinitely

# Define ball2 and ball2_active before the game loop
ball2 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)
ball2_active = False
ball2_speed_x = 6
ball2_speed_y = 6

while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed = -6
            if event.key == pygame.K_DOWN:
                player1_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1_speed = 0
    # If the game is over, stop the background music
    game_over = False
    if game_over:
        pygame.mixer.music.stop()

    #Change the positions of the game objects
    animate_ball()
    animate_player()
    #Check if a player has reached 10 points
    if player1_points >= 10:
        win_surface = score_font.render("You win!", True, "white")
        screen.blit(win_surface, (screen_width/2, screen_height/2))
        pygame.display.update()
        pygame.time.wait(6000)
        break
    elif player2_points >= 10:
        win_surface = score_font.render("You win!", True, "white")
        screen.blit(win_surface, (screen_width/4, screen_height/2))
        pygame.display.update()
        pygame.time.wait(6000)
        break

    #Check for a collision with the ninth item
    if ball.colliderect(item9):
    # Clone the ball
        ball2 = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
        ball2_active = True
        # Give ball2 a different speed or direction
        ball2_speed_x = -ball_speed_x
        ball2_speed_y = -ball_speed_y
        item9.x = random.randint(0, screen_width)
        item9.y = random.randint(0, screen_height)

    if ball2_active:
        ball2.x += ball2_speed_x
        ball2.y += ball2_speed_y

    if ball2.bottom >= screen_height or ball2.top <= 0:
        ball2_speed_y *= -1

    if ball2.right >= screen_width:
        point_won("player2")
        ball2_active = False

    if ball2.left <= 0:
        point_won("player1")
        ball2_active = False

    if ball2.colliderect(player1) or ball2.colliderect(player2):
        ball2_speed_x *= -1

    # #Clear the screen
    screen.fill('black')

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the bars
    # screen.blit(bar1_image, player1.topleft)  # Replace 'player1' with your bar's Rect object
    # screen.blit(bar2_image, player2.topleft)  # Replace 'player2' with your bar's Rect object

    #Draw the score
    player2_score_surface = score_font.render(str(player2_points), True, "white")
    player1_score_surface = score_font.render(str(player1_points), True, "white")
    screen.blit(player2_score_surface,(screen_width/4,20))
    screen.blit(player1_score_surface,(3*screen_width/4,20))

    #Draw the game objects
    pygame.draw.aaline(screen,'white',(screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen,'white',ball)
    # Draw ball2
    if ball2_active:
        pygame.draw.ellipse(screen, 'black', ball2)
    pygame.draw.rect(screen,'white',player2)
    pygame.draw.rect(screen,'white',player1)

    # Draw the item
    screen.blit(item_image, item)
    
    # Draw the second item
    screen.blit(item2_image, item2)

    # Draw the third item
    screen.blit(item3_image, item3)
    
    # # Draw the fourth item
    # screen.blit(item4_image, item4)

    # # Draw the fourth item only if it's not off-screen
    # if item4.x >= 0 and item4.y >= 0:
    #     screen.blit(item4_image, item4)

    # Draw the fifth item
    screen.blit(item5_image, item5)

    # Draw the sixth item
    screen.blit(item6_image, item6)

    # Draw the seventh item
    screen.blit(item7_image, item7)

    # Draw the eighth item
    screen.blit(item8_image, item8)

    # Draw the ninth item
    screen.blit(item9_image, item9)

    # Update the display
    pygame.display.flip()

    #Update the display
    pygame.display.update()
    clock.tick(60)