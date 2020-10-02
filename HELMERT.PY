import math

def isRange(val, min, max): 
    return (val < max and val >= min)

class Quadrant:
    dx = 0
    dy = 0
    dz = 0
    u = 0
    rx = 0
    ry = 0
    rz = 0
    def __init__(self, dx, dy, dz, u, rx, ry, rz): 
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.u = u
        self.rx = rx
        self.ry = ry
        self.rz = rz
        

c1 = Quadrant(-806.4130, 263.5000, -622.6710, -0.00002081616, -0.00006018583, -0.00001450001, -0.00018924550)
c2 = Quadrant(100.7830, 348.5650, 252.9780, -0.00001356561, -0.00004471839, 0.00001175093, -0.00004027967)
c3 = Quadrant(336.0260, 348.6560, 252.9780, -0.00000577191, -0.00008358813, -0.00003057474, 0.00000757303)
c4 = Quadrant(963.2730, 486.3860, 190.9970, -0.00001389914, -0.00007992171, -0.00008090696, 0.00010516990)
c5 = Quadrant(-90.2900, 247.5590, 21.9890, 0.00000218166, 0.00004216369, -0.00002030416, -0.00006209623)
c6 = Quadrant(-0.5620, 244.2990, -456.9380, 0.00000374656, 0.00003329153, -0.00004001009, -0.00004507206)
c7 = Quadrant(-305.3560, 222.0040, -30.0230, 0.00000632575, -0.00004698084, 0.00000500312, -0.00009578655)
c8 = Quadrant(221.8990, 274.1360, -397.5540, -0.00000219994, 0.00001361573, -0.00000217443, -0.00001362410)

a = 6378388.000
e2 = 0.00672267002233


def getQuadrant(phi_, lambda_):
    
    c1 = isRange(phi_, 10, 13) and isRange(lambda_, 71, 73)
    c2 = isRange(phi_, 9.4, 11) and isRange(lambda_, 73, 76)
    c3 = isRange(phi_, 8, 9.4) and isRange(lambda_, 74.4, 77.6)
    c4 = isRange(phi_, 5, 9.4) and isRange(lambda_, 72, 74.4)
    c5 = isRange(phi_, 5, 8) and isRange(lambda_, 74.4, 78)
    c6 = isRange(phi_, 3, 5) and isRange(lambda_, 74.4, 78)
    c7 = isRange(phi_, -1, 3) and isRange(lambda_, 74, 79)
    c8 = isRange(phi_, -4.5, 3) and isRange(lambda_, 66.5, 74) or isRange(phi_, 3, 5) and isRange(lambda_, 66.5, 74) or isRange(phi_, 5, 7.3) and isRange(lambda_, 66.5, 72)
    
    if(c1): return 'I'
    if(c2): return 'II'
    if(c3): return 'III'
    if(c4): return 'IV'
    if(c5): return 'V'
    if(c6): return 'VI'
    if(c7): return 'VII'
    if(c8): return 'VIII'


def calculate(phi_, lambda_, h):
    c = getQuadrant(phi_,lambda_)
    print(c)

    math.cos(math.radians(phi_))
