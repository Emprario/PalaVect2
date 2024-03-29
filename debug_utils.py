"""
Outil de debug divers
"""

def test_get_full_line():

    from utils import get_full_line

    assert get_full_line((10, 30), (-20, 69)) == [(-20, 69), (-19, 68), (-18, 67), (-18, 66), (-17, 65), (-16, 64),
                                              (-15, 63), (-15, 62), (-14, 61), (-13, 60), (-12, 59), (-12, 58),
                                              (-11, 57), (-10, 56), (-9, 55), (-8, 54), (-8, 53), (-7, 52), (-6, 51),
                                              (-5, 50), (-5, 49), (-4, 48), (-3, 47), (-2, 46), (-2, 45), (-1, 44),
                                              (0, 43), (1, 42), (2, 41), (2, 40), (3, 39), (4, 38), (5, 37), (5, 36),
                                              (6, 35), (7, 34), (8, 33), (8, 32), (9, 31), (10, 30)]


def have_duplicated_obj_in_list(master: list[list]) -> bool:
    """Returns true if there are duplicated objects"""
    lisflat = [obj for lsobj in master for obj in lsobj]
    setflat = set(lisflat)
    return len(setflat) != len(lisflat)
