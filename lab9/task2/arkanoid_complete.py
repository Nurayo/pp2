import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (255, 255, 255)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('task2/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = []
color_list = []  
for i in range(10):
    for j in range(4):
        if random.random() < 0.2:  # 20% chance of unbreakable block
            block_list.append(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50))
            color_list.append((0, 0, 0))  # Black color for unbreakable block
        else:
            block_list.append(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50))
            color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
print(block_list)

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)

score_position = (20, 20)
def update_score_display():
    score_text = game_score_fonts.render(f'Score: {game_score}', True, (0, 0, 0))
    screen.blit(score_text, score_position)

#settings
game_parameters = {
    'paddle_speed': 20,
    'ball_speed': 6
}

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

time_elapsed = 0
speed_increase_interval = 8
shrink_paddle_interval = 8 
initial_paddle_width = paddleW

paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Player presses "P" to pause and access settings
                paused = not paused
                render_pause_text()
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                paused = False
                            elif event.key == pygame.K_s:
                                settings_menu()
        def settings_menu():
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:  # Player presses "S" again to exit settings
                            running = False
                    # Handle key presses to adjust parameters
                        elif event.key == pygame.K_UP:  # Increase paddle speed
                            game_parameters['paddle_speed'] += 1
                        elif event.key == pygame.K_DOWN:  # Decrease paddle speed
                            game_parameters['paddle_speed'] -= 1
                        elif event.key == pygame.K_RIGHT:  # Increase ball speed
                            game_parameters['ball_speed'] += 1
                        elif event.key == pygame.K_LEFT:  # Decrease ball speed
                            game_parameters['ball_speed'] -= 1
        def render_pause_text():
            pause_font = pygame.font.SysFont('comicsansms', 60)
            pause_text = pause_font.render('PAUSE', True, (255, 0, 0))
            pause_text_rect = pause_text.get_rect(center=(W // 2, H // 2))
            screen.blit(pause_text, pause_text_rect)
    paddleSpeed = game_parameters['paddle_speed']
    ballSpeed = game_parameters['ball_speed']
    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # drawing blocks
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        if hitColor != (0, 0, 0):  # Check if block is breakable
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        else:  # Unbreakable block
            dx, dy = detect_collision(dx, dy, ball, hitRect)

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    update_score_display()

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    
    # Increase ball speed after every 8 seconds
    time_elapsed += clock.get_time() / 1000
    if time_elapsed >= speed_increase_interval:
        ballSpeed += 1 
        time_elapsed = 0 
    if time_elapsed >= shrink_paddle_interval:
        paddleW = max(initial_paddle_width - 20, 50)  # Reduce paddle width by 20 pixels, minimum width of 50 pixels
        paddle.width = paddleW
        time_elapsed = 0  
    pygame.display.flip()
    clock.tick(FPS)