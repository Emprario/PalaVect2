"""
Gestions des worms
    - Sous forme de Sprite ?
"""
import pygame
from physics import get_angle, get_dist, get_full_line


class Worm:
    """Classe du ver de terre"""

    def __init__(self, camp: int, x: int, y: int, hp=100):
        """
        Constructeur de Worm
        :param camp: Camp du worm (pas nécessairement binaire)
        """
        self.team = camp # L'équipe du worm
        self.x_coord = x
        self.y_coord = y
        self.health = hp
        self.alive = True # Checker si le worm est en vie
        self.is_jumping = False # Checker si le joueur saute
        self.is_on_ground = False
        self.jump_current = 0 # Track la hauteur d'un saut actuel, commence = 0 puis < 0 lorsque hauteur maxi atteint
        self.jump_height = 80 # La hauteur maximale d'un saut
        self.movement_distance = 200 # NOT THE FINAL VALUE SUBJECT TO CHANGE
        self.movement_speed = 40 # SUBJECT TO CHANGE
        self.image = pygame.image.load("assets/worms/worm_sprite.png").convert_alpha()

    def move_worm(self, x_axis, y_axis):
        """
        Permet de déplacer le worm dans les deux directions
        :param x_axis: Type(int) gauche à droite
        :param y_axis: Type(int) haut à bas
        """
        self.x_coord += x_axis
        self.y_coord += y_axis

        # NEW IDEA FOR WORM MOVEMENT:
        """
        Move the x axis however but to make sure that we don't walk through the map,
        we use the get_full_line and use all the coordinates grabbed from it.
        When moving left or right, we constantly check
        """

        distance_travelled = 0

    def get_surrounding_points(self):
        """
        À partir des coordonnées du joueur, détermine le point
        le plus proche à sa gauche et à sa droite
        :return: List
        """






    def jump_worm_check(self):
        """
        Vérifie si le worm peut sauter ou pas. Il faut qu'il soit au sol
        """
        if self.is_on_ground:
            self.is_jumping = True
            self.is_on_ground = False

    def jump_worm(self):
        """
        Fait sauter le worm
        :return:
        """
        if self.is_jumping:
            if self.jump_current >= -self.jump_height: # S'il na pas atteint sa hauteur maximale
                direction = 1 # Le worms monte
                if self.jump_current < 0:
                    direction = -1  # Le worms descend
                self.y_coord -= (self.jump_current ** 2) * 0.5 * direction
                self.jump_current -= 1
            else:
                self.is_jumping = False
                self.jump_current = self.jump_height
                self.is_on_ground = True

    def draw(self, screen):
        screen.blit(self.image,(self.x_coord,self.y_coord))













    def pg_blit(self, surface: pygame.Surface):
        """Pygame Blit : Fonction d'affichage spécifique au worm"""
        pass
