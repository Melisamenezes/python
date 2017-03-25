#CENTROID OF A TRIANGLE
print('Assume the three sides(coordinates) of a triangle to be A(ax,ay), B(bx,by) & C(cx,cy)')
ax = int(input('ax : '))
ay = int(input('ay : '))
print('The coordinates of side A is ' , (ax,ay))
bx = int(input('bx : '))
by = int(input('by: '))
print('The coordinates of side B is ' , (bx,by))
cx = int(input('cx : '))
cy = int(input('cy : '))
print('The coordinates of side C is' , (cx,cy))
print('Let the centroid be having vertices and coordinates as O(ox,oy)')
ox = (ax + bx + cx) / 3
oy = (ay + by + cy) / 3
print('The centroid of triangle is ' , (ox,oy))