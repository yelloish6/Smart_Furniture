from elements.corp import *


class Banca(corp):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)

        gap_fata = 50
        gap_spate = 0
        gap_lat = 50
        height_baza = 100

        lat1 = PlacaPal(self.label + ".lat1", height - self.thick_pal, depth - gap_fata, self.thick_pal, "1", "", "", "")
        lat1.rotate("y")
        lat1.move("x", gap_lat)
        lat1.move("y", gap_fata)
        #lat1.rotate("z")
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat2", height - self.thick_pal, depth - gap_fata, self.thick_pal, "1", "", "", "")
        lat2.rotate("y")
        #lat2.rotate("z")
        lat2.move("x", self.width - gap_lat - self.thick_pal)
        lat2.move("y", gap_fata)
        self.append(lat2)

        jos = PlacaPal(self.label + ".jos", width - 2 * (gap_lat + self.thick_pal), depth - gap_fata, self.thick_pal, "1", "", "", "")
        jos.move("z", height_baza - self.thick_pal)
        jos.move("x", gap_lat)
        jos.move("y", gap_fata)
        #jos.rotate("z")
        self.append(jos)



        pol1 = PlacaPal(self.label + ".pol1", int((width - (3 * self.thick_pal) - (2 * gap_lat)) / 2), depth - gap_fata, self.thick_pal,
                       "1", "", "", "")
        pol1.move("z", int(height * 2/3))
        pol1.move("x", gap_lat)
        pol1.move("y", gap_fata)
        self.append(pol1)

        sep_v = PlacaPal(self.label + ".sep_v", height - height_baza - self.thick_pal, depth - gap_fata, self.thick_pal,
                       "1", "", "", "")
        sep_v.move("z", height_baza)
        sep_v.move("x", gap_lat + self.thick_pal + pol1.length)
        sep_v.move("y", gap_fata)
        sep_v.rotate("y")
        self.append(sep_v)

        pol2 = PlacaPal(self.label + ".pol2", int((width - (3 * self.thick_pal) - (2 * gap_lat)) / 2), depth - gap_fata, self.thick_pal,
                       "1", "", "", "")
        pol2.move("z", int(height * 2/3))
        pol2.move("x", gap_lat + self.thick_pal + pol1.length)
        pol2.move("y", gap_fata)
        self.append(pol2)

        plinta1 = PlacaPal(self.label + ".plinta1", depth - gap_fata, height_baza, self.thick_pal,
                       "2", "2", "", "")
        plinta1.rotate("x")
        plinta1.rotate("z")
        plinta1.rotate("z")
        plinta1.rotate("z")
        plinta1.move("y", gap_fata)
        plinta1.move("x", gap_lat - 2 * self.thick_pal)
        self.append(plinta1)

        plinta2 = PlacaPal(self.label + ".plinta2", depth - gap_fata, height_baza, self.thick_pal,
                       "2", "2", "", "")
        plinta2.rotate("x")
        plinta2.rotate("z")
        plinta2.rotate("z")
        plinta2.rotate("z")
        plinta2.move("y", gap_fata)
        plinta2.move("x", width - gap_lat - self.thick_pal)
        self.append(plinta2)

        plinta3 = PlacaPal(self.label + ".plinta3", width - 2 * gap_lat + 2 * self.thick_pal, height_baza, self.thick_pal,
                       "2", "2", "2", "2")
        plinta3.rotate("x")
        plinta3.move("y", gap_fata)
        plinta3.move("x", gap_lat - 2 * self.thick_pal)
        self.append(plinta3)

        self.add_pfl()