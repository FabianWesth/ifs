
iterations = 20

width = 1024
height = 768

transformations = (
   (.167, lambda x, y,z: (.341*x - .071*y, .071*x + .341*y, 0)),
   (.167, lambda x, y,z: (.038*x - .346*y + .341, .346*x + .038*y + .071, 0)),
   (.166, lambda x, y,z: (.341*x - .071*y + .379, .071*x + .341*y + .418, 0)),
   (.167, lambda x, y,z: (-.234*x + .258*y + .72, -.258*x - .234*y + .489, 0)),
   (.167, lambda x, y,z: (.173*x + .302*y + .486, -.302*x + .173*y + .231, 0)),
   (.166, lambda x, y,z: (.341*x - .071*y + .659, .071*x + .341*y - .071, 0))
)
