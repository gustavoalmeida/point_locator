class PointLocation(object):
    point_on_vertex_ = True

    def point_location(self):
        print self.point_on_vertex

    def point_in_polygon(self, point, polygon, point_on_vertex=True):
        self.point_on_vertex_ = point_on_vertex
        point = self.point_string_to_coordinates(point)
        vertices = []
        for vertex in polygon:
            vertices.append(self.point_string_to_coordinates(vertex))
        if self.point_on_vertex_ == True and self.point_on_vertex(point, vertices) == True:
            return 'vertex'
        intersections = 0

        for i, v in enumerate(vertices):
            vertex1 = vertices[i-1]
            vertex2 = vertices[i]
            if vertex1['y'] == vertex2['y'] and vertex1['y'] == point['y'] \
                and min(vertex1['x'], vertex2['x']) < point['x'] < max(vertex1['x'], vertex2['x']):
                    return 'bundary'
            if min(vertex1['y'], vertex2['y']) < point['y'] <= max(vertex1['y'], vertex2['y']) \
                    and point['x'] <= max(vertex1['x'], vertex2['x']) \
                    and vertex1['y'] != vertex2['y']:
                    xinters = (point['y'] - vertex1['y']) * (vertex2['x'] - vertex1['x'])\
                              / (vertex2['y'] - vertex1['y']) + vertex1['x']
                    if xinters == point['x']:
                        return "boundary"
                    if vertex1['x'] == vertex2['x'] or point['x'] <= xinters:
                        intersections = intersections + 1

        if intersections % 2 != 0:
            return 'inside'
        else:
            return 'outside'

    def point_on_vertex(self, point, vertices):
        for vertex in vertices:
            if point == vertex:
                return True
        return False

    def point_string_to_coordinates(self, point_string):
        coordinates = point_string.split(" ")
        return {
            "x": int(coordinates[0]),
            "y": int(coordinates[1])
            }


pointLocation = PointLocation()
points = ["50 70","70 40","-20 30","100 10","-10 -10","40 -20","110 -20"]
polygon = ["-50 30","50 70","100 50","80 10","110 -10","110 -30",
           "-20 -50","-30 -40","10 -10","-10 10","-30 -20","-50 30"]

for i, point in enumerate(points):
    print "point " , i+1 , " (point): " ,point, " ", pointLocation.point_in_polygon(point, polygon) , "\n"



"""
point  1  (point):  50 70   vertex

point  2  (point):  70 40   inside

point  3  (point):  -20 30   inside

point  4  (point):  100 10   outside

point  5  (point):  -10 -10   outside

point  6  (point):  40 -20   inside

point  7  (point):  110 -20   boundary


"""