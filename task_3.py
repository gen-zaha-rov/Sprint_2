class PointsForPlace:
    def __init__(self):
        self.points = 0 

    def get_points_for_place(self, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0     
        else:
            self.points = 101 - place 
            return self.points
        
class PointsForMeters:
    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0    
        else: 
            return 0.5 * meters

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)  
        PointsForMeters.__init__(self)  
        self.total = 0
    
    def get_total_points(self, meters, place):
        meters_points = self.get_points_for_meters(meters)
        place_points = self.get_points_for_place(place)
        self.total = meters_points + place_points
        return self.total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))