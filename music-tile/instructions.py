import pygame

pygame.font.init()

FONT = pygame.font.Font('Exo-Regular.ttf', 15)
fontcolour = (255, 255, 255)

surface1 = FONT.render('Instructions:', True, fontcolour)
surface2 = FONT.render('Increase tile size with:', True, fontcolour)
surface3 = FONT.render('width: y/h          height: t/g', True, fontcolour)
surface4 = FONT.render('Increase tile number with:', True, fontcolour)
surface5 = FONT.render('x tiles: i/k        y tiles: u/j', True, fontcolour)
surface6 = FONT.render('Change delay with:', True, fontcolour)
surface7 = FONT.render('Increase: Up arrow  Decrease: Down arrow', True, fontcolour)
surface8 = FONT.render('Hide/show isntructions with: O', True, fontcolour)
surface9 = FONT.render('4:3 mode to 16:9 mode with: V', True, fontcolour)
surface10 = FONT.render('Toggle colour modes with: C', True, fontcolour)


