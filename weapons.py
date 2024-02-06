"""Weapons management"""
import pygame


class Weapon:
    """Arme générique"""

    def __init__(self, texture: str):
        """
        Constructeur ...
        :param texture: Chemin vers la texture
        """
        self.power = 100

    def pg_blit(self, surface: pygame.Surface):
        """Pygame Blit : Fonction d'affichage spécifique au worm"""
        pass


class StGrenade(Weapon):
    """Exemple d'objet spécifique : la St Grenade"""
    pass
