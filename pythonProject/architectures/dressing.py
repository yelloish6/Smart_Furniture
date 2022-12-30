from elements.corp import *


class Banca(corp):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)

        gap_fata = 50
        gap_spate = 0
        gap_lat = 50
        height_baza = 100

        lat1 = PlacaPal(self.label + ".lat1", height - self.thick_pal, depth, self.thick_pal, "1", "", "1", "")
        lat1.rotate("y")
        lat1.move("x", self.thick_pal)
        #lat1.move("y", self.thick_pal)
        #lat1.rotate("z")
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat2", height - self.thick_pal, depth, self.thick_pal, "1", "", "1", "")
        lat2.rotate("y")
        #lat2.rotate("z")
        lat2.move("x", self.width)
        #lat2.move("y", gap_fata)
        self.append(lat2)

        jos = PlacaPal(self.label + ".jos", width - (2 * self.thick_pal), depth, self.thick_pal, "", "", "", "")
        jos.move("z", height_baza - self.thick_pal)
        jos.move("x", self.thick_pal)
        #jos.move("y", gap_fata)
        #jos.rotate("z")
        self.append(jos)

        pol1 = PlacaPal(self.label + ".pol1", int((width - (3 * self.thick_pal)) / 2), depth, self.thick_pal,
                       "2", "", "", "")
        pol1.move("z", int(height * 2/3))
        pol1.move("x", self.thick_pal)
        #pol1.move("y", gap_fata)
        self.append(pol1)

        sep_v = PlacaPal(self.label + ".sep_v", height - height_baza - self.thick_pal, depth - self.cant,
                         self.thick_pal, "2", "", "", "")
        sep_v.move("z", height_baza)
        sep_v.move("x", 2 * self.thick_pal + pol1.length)
        #sep_v.move("y", gap_fata)
        sep_v.rotate("y")
        self.append(sep_v)

        pol2 = PlacaPal(self.label + ".pol2", int((width - (3 * self.thick_pal)) / 2), depth - self.cant,
                        self.thick_pal, "2", "", "", "")
        pol2.move("z", int(height * 2/3))
        pol2.move("x", 2 * self.thick_pal + pol1.length)
        #pol2.move("y", gap_fata)
        self.append(pol2)

        plinta1 = PlacaPal(self.label + ".plinta1", depth, height_baza, self.thick_pal, "2", "2", "", "")
        plinta1.rotate("x")
        plinta1.rotate("z")
        plinta1.rotate("z")
        plinta1.rotate("z")
        #plinta1.move("y", gap_fata)
        plinta1.move("x", - self.thick_pal)
        self.append(plinta1)

        plinta2 = PlacaPal(self.label + ".plinta2", depth, height_baza, self.thick_pal, "2", "2", "", "")
        plinta2.rotate("x")
        plinta2.rotate("z")
        plinta2.rotate("z")
        plinta2.rotate("z")
        #plinta2.move("y", gap_fata)
        plinta2.move("x", width)
        self.append(plinta2)

        plinta3 = PlacaPal(self.label + ".plinta3", width + 2 * self.thick_pal, height_baza, self.thick_pal, "2", "2",
                           "2", "2")
        plinta3.rotate("x")
        #plinta3.move("y", gap_fata)
        plinta3.move("x", - self.thick_pal)
        self.append(plinta3)

        blat = PlacaPal(self.label + ".blat", width + 2 * gap_lat, depth + gap_fata, self.thick_pal, "2", "2", "2", "2")
        blat.move("z", height - self.thick_pal)
        blat.move("x", - gap_lat)
        blat.move("y", - gap_fata)
        self.append(blat)

        self.add_pfl()

        self.append(accesoriu("eurosurub 7x50", 10))
        self.append(accesoriu("surub 3.5x30", 14))
        self.append(accesoriu("demontabil cama", 6))
        self.append(accesoriu("L", 2))


class Etajera(corp):
    def __init__(self, label, height, width, depth, shelves, rules):
        super().__init__(label, height, width, depth, rules)

        lat1 = PlacaPal(self.label + ".lat", self.height, self.depth, self.thick_pal, self.cant_lab, "", "", "")
        lat1.rotate("y")
        lat1.move("x", self.thick_pal)
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat", self.height, self.depth, self.thick_pal, self.cant_lab, "", "", "")
        lat2.rotate("y")
        lat2.move("x", width)
        self.append(lat2)

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth,
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("z", height - self.thick_pal)
        sus.move("x", self.thick_pal)
        self.append(sus)

        jos = PlacaPal(self.label + ".jos", self.width - (2 * self.thick_pal), self.depth,
                       self.thick_pal, self.cant_lab, "", "", "")
        jos.move("x", self.thick_pal)
        self.append(jos)

        self.add_pfl()

        self.append(accesoriu("eurosurub 7x50", 8))

        self.add_pol(shelves, 2)


class CorpDressing(corp):
    def __init__(self, label, height, width, depth, rules, gap_list, front_list):
        """

        :param label:
        :param height:
        :param width:
        :param depth:
        :param rules:
        :param gap_list: intaltimea gap-urilor de jos in sus. Ultimul gap e cat ramane (ex:[gen_h_base - 2 * t1.pal_width,300, gen_h_tower - gen_h_base - 318 - gen_h_top])
        :param front_list: care gap-uri au front (ex. [0, 0, 0, 1])
        """
        super().__init__(label, height, width, depth, rules)

        jos = PlacaPal(self.label + ".jos", self.width - (2 * self.thick_pal), self.depth, self.thick_pal, self.cant_lab, "",
                       self.cant_lab, self.cant_lab)
        jos.move("x", self.thick_pal)
        jos.move("z", rules["height_legs"])
        self.append(jos)

        lat1 = PlacaPal(self.label + ".lat", self.height, self.depth, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat1.rotate("y")
        lat1.move("x", self.thick_pal)
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat", self.height, self.depth, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat2.rotate("y")
        lat2.move("x", self.width)
        self.append(lat2)

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - self.cant,
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("x", lat1.thick)
        sus.move("z", lat1.length - self.thick_pal)
        self.append(sus)

        plinta = PlacaPal(self.label + ".plinta", self.width - (2 * self.thick_pal), rules["height_legs"],
                          self.thick_pal, self.cant_lab, "", "", "")
        plinta.rotate("x")
        plinta.move("x", self.thick_pal)
        plinta.move("y", self.thick_pal)
        self.append(plinta)

        # adding horizontal separators
        offset = 0
        for gap in range(len(gap_list)):
            offset += gap_list[gap] + self.thick_pal
            self.add_sep_h(self.width - 2 * self.thick_pal, 0, offset, self.cant_lab)
        # self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0], self.cant_lab)
        # self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0] + gap_list[1] + self.thick_pal, self.cant_lab)
        # self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0] + gap_list[1] + gap_list[2] + (2 * self.thick_pal),
        #              self.cant_lab)

        self.append(accesoriu("surub", 8))
        self.append(accesoriu("plinta", self.width / 1000))
        picioare = math.ceil(self.width / 400) * 2
        self.append(accesoriu("picioare", picioare))
        self.append(accesoriu("clema plinta", picioare / 2))
        self.append(accesoriu("surub 3.5x16", picioare * 4))  # pentru picioare

        self.add_pfl()

        # Se seteaza fronturile pentru turn
        # gap_list[0]
        if (front_list[0] == 1) and (front_list[1] == 0):
            self.add_front_manual(gap_list[0] + (2 * self.thick_pal) - 4, self.width - 4)
        if (front_list[0] == 1) and (front_list[1] == 1):
            self.add_front_manual(gap_list[0] + (1.5 * self.thick_pal) - 3, self.width - 4)
        # gap_list[1]
        if (front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 0):
            self.add_front_manual(gap_list[1] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 0))
                or ((front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 1))):
            self.add_front_manual(gap_list[1] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 1):
            self.add_front_manual(gap_list[1] + self.thick_pal - 4, self.width - 4)

        # gap_list[2]
        if (front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 0):
            self.add_front_manual(gap_list[2] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 0))
                or ((front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 1))):
            self.add_front_manual(gap_list[2] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 1):
            self.add_front_manual(gap_list[2] + self.thick_pal - 4, self.width - 4)

        # gap4
        if (front_list[3] == 1) and (front_list[2] == 0):
            self.add_front_manual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3 * self.thick_pal) - 4,
                                  self.width - 4)
        if (front_list[3] == 1) and (front_list[2] == 1):
            self.add_front_manual(
                self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3.5 * self.thick_pal) - 3,
                self.width - 4)
