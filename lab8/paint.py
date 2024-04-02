import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_UP:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)
                elif event.key == pygame.K_SPACE:
                    points = []
            
        if pressed[pygame.K_LEFT]:
            x -= 5
        elif pressed[pygame.K_RIGHT]:
            x += 5
        if pressed[pygame.K_UP]:
            y -= 5
        elif pressed[pygame.K_DOWN]:
            y += 5
        
        # draw all points
        if pygame.mouse.get_pressed()[0] or any(pressed):
            points.append((x, y))
        
        screen.fill((255, 255, 255))
        
        # draw all points
        for i in range(len(points) - 1):
            drawShapeBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawShapeBetween(screen, index, start, end, width, mode):
    if mode == 'erase':
        color = (0, 0, 0)  # Eraser color
    else:
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))
        
        if mode == 'blue':
            color = (c1, c1, c2)
        elif mode == 'red':
            color = (c2, c1, c1)
        elif mode == 'green':
            color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if mode == 'rectangle':
            pygame.draw.rect(screen, color, (x - width/2, y - width/2, width, width))
        elif mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), width // 2)
        elif mode == 'erase':
            pygame.draw.circle(screen, color, (x, y), width)

main()
