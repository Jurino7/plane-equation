
class point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

class vector:
    def __init__(self, start: point, end: point) -> None:
        self.start = start
        self.end = end
        self.coords = [end.x - start.x, end.y - start.y, end.z - start.z]

# change points coords and run
A = point(1,1,3)
B = point(2,0.5,0)
C = point(5,0,1)

# vectors
u = vector(A, B).coords
v = vector(A, C).coords

# determinat to find normal to plane
det = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]

# calculate plane equation
d = det[0]*A.x*(-1) + det[1]*A.y*(-1) + det[2]*A.z*(-1)
print("ϱ: ", det[0], "x ", det[1], "y ", det[2], "z ", d)

# find intersection of axis
print(f"Px = [{-d/det[0]}, 0, 0]")
print(f"Py = [0, {-d/det[1]}, 0]")
print(f"Pz = [0, 0, {-d/det[2]}]")

