"""
Gestion de la physique pure
    - Equations physique en jeu
    - PAS DE CONSTANTES (cf. CONSTS.py)
"""
from math import pi, cos, sin, atan

from CONSTS import coordinate, vector
from debug import DEBUG_FLAG


def get_circle(density: int, center: coordinate, radius: float) -> list[coordinate]:
    """
    Renvoie une liste de coordonée en forme de cercle,
    en renvoie selon la densité demandée
    :param density: Nombre de points renvoyé
    :param center: Centre du cercle (coordonnée)
    :param radius: Rayon du cercle
    :return: Liste de coordonnée
    """
    angles = [(2 * k * pi) / density for k in range(density)]

    return list(zip([round(center[0] + int(radius * cos(angle)), 4) for angle in angles],
                    [round(center[1] + int(radius * sin(angle)), 4) for angle in angles]))


def get_result_point_from_vector(vector0: vector) -> coordinate:
    """
    Get the point at the end of the vector
    :param vector0: Vecteur à extraire la position
    :return: Point (arrondi)
    """
    return vector0[0][0] + int(vector0[1] * cos(vector0[2])), vector0[0][1] + int(vector0[1] * sin(vector0[2]))


def get_dist(ptA: coordinate, ptB: coordinate) -> float:
    """
    Calcule la distance entre 2 points
    :param ptA: Point A
    :param ptB: Point B
    :return: Distance
    """
    return ((ptA[0] - ptB[0]) ** 2 + (ptA[1] - ptB[1]) ** 2) ** 0.5


def get_angle(ptA: coordinate, ptB: coordinate) -> float:
    """
    Calcul l'angle entre 2 points
    :param ptA: Point A (Origine de l'angle)
    :param ptB: Point B
    :return: Angle (rad)
    """
    # On place p1 à gauche de p2
    if ptA[0] > ptB[0]: ptA, ptB = ptB, ptA
    if ptA[0] - ptB[0] == 0:
        if ptA[1] > ptB[1]:
            return pi / 2
        else:
            return -pi / 2
    return atan(ptA[1] - ptB[1]) / (ptA[0] - ptB[0])


def get_full_line(ptA: coordinate, ptB: coordinate) -> list[coordinate]:
    """
    Get a full line with all coordinates between ptA and ptB
    :param ptA: Point A
    :param ptB: Point B
    :return: List of all points between
    """
    # Use the bresenham algorithm
    # Reference : https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham
    # Reference : https://babavoss.pythonanywhere.com/python/bresenham-line-drawing-algorithm-implemented-in-py

    # Fit the input into the algorithm:
    if ptA[0] > ptB[0]:
        ptA, ptB = ptB, ptA
    # print(ptA, ptB)

    dx = ptB[0] - ptA[0]
    dy = abs(ptB[1] - ptA[1])
    if dx < dy:
        dy, dx = dx, dy
        invert_x_y = True
        ptA = (ptA[1], ptA[0])
        ptB = (ptB[1], ptB[0])
    else:
        invert_x_y = False

    # Bresenham algorithm

    x, y = ptA
    pente = 2 * dy - dx
    line = [(x, y)]

    for k in range(2, dx + 2):
        if pente > 0:
            y = y + 1 if y < ptB[1] else y - 1
            pente = pente + 2 * (dy - dx)
        else:
            pente = pente + 2 * dy
        x = x + 1 if x < ptB[0] else x - 1
        line.append((x, y))

    # Correct inversion
    if invert_x_y:
        for i in range(len(line)):
            line[i] = (line[i][1], line[i][0])
    return line


def does_intersect(lineA: tuple[coordinate, coordinate], lineB: tuple[coordinate, coordinate]) -> bool:
    """
    Défini si un point et une ligne s'intersectent dans une ligne de 0 rad
    :param lineA: Ligne
    :param lineB: Ligne
    :return: True Si Il y a Croisement
    """
    return len(set(get_full_line(*lineA)) & set(get_full_line(*lineB))) > 0


def is_inner_point(point: coordinate, polygon: list[coordinate]) -> bool:
    """
    Défini si un point est dans un polygone
    :param point: Point à définir
    :param polygon: Tous les points des polygones
    :return: Si le point est dans le polygone
    """
    if DEBUG_FLAG: print(f"\n\t====Analysing new point : {point} ====\n")
    inside = False
    # On prend les points deux à deux
    for i in range(len(polygon)):
        p1, p2 = polygon[i - 1], polygon[i]

        # On place p1 à gauche de p2
        if p1[0] > p2[0]: p2, p1 = p1, p2
        if DEBUG_FLAG: print("P1={}, P2={} ...".format(p1, p2))

        # Test si le point pourrait être dans le champ de la droite deux points (niveau y)
        if min(p1[1], p2[1]) < point[1] <= max(p1[1], p2[1]):
            if DEBUG_FLAG: print("In y range")
            if p2[0] < point[0]:
                if DEBUG_FLAG: print("Out in x range (no intersection)")
                continue
            elif point[0] <= p1[0]:
                if DEBUG_FLAG: print("Out in x range (intersect segment)")
                inside = not inside
            else:
                if DEBUG_FLAG: print("In x range")
                if does_intersect((*point, (p2[0], point[1])), (p1, p2)):
                    if DEBUG_FLAG: print(f"Inverting {inside}->{not inside}")
                    inside = not inside
                    break
        else:
            if DEBUG_FLAG: print("Out y range")
            continue
    if DEBUG_FLAG: print(f"Res={inside}")
    return inside


if __name__ == '__main__':
    pts = [(331, 240), (396, 237)]
    print(get_full_line(*pts))
    pts = [(5, 15), (2, 3)]  # Inversion
    print(get_full_line(*pts))
