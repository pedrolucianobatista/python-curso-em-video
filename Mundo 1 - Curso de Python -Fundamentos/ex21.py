# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Mundo 1 - Fundamentos/assets/audio/ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
