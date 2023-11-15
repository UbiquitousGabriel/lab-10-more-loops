def move(f, t):
    print("Move disc from {} to {}".format(f, t))

def towerHanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        towerHanoi(n - 1, f, t, h)
        move(f, t)
        towerHanoi(n - 1, h, f, t)

towerHanoi(4, "A", "B", "C")