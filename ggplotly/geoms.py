class geom:
    def __init__(self):
        self.name = None


class geom_point(geom):
    def __init__(self):
        super(geom_point, self).__init__()
        self.name = "point"



class geom_bar(geom):
    def __init__(self):
        super(geom_bar, self).__init__()
        self.name = "bar"
