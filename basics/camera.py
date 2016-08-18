import pygame
import pygame.camera

pygame.camera.init()
camlist = pygame.camera.list_cameras() #camera detected or not
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))
    cam.start()
else:
    print "No camera's detected"
