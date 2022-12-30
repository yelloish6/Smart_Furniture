from elements.placa import *
from elements.accesoriu import *
from elements.export_stl import *
import math
import csv


class corp:
    def __init__(self, label, height, width, depth, rules):
        """
        collection of boards forming one cabinet
        all items collected in "self.material_list[]"
        :param label: eticheta
        :param height: inaltimea
        :param width: latimea
        :param depth: adancimea
        :param rules: lista de reguli
        """
        self.label = label
        self.height = height
        self.width = width
        self.depth = depth
        self.thick_pal = rules["thick_pal"]
        self.thick_front = rules["thick_front"]
        self.thick_blat = rules["thick_blat"]
        self.width_blat = rules["width_blat"]
        self.cant_lab = rules["cant_general"]
        self.cant = round(rules["cant_general"])
        self.front_gap = float(rules["gap_front"])
        self.material_list = []
        # self.pal = []
        # self.palOO = []
        # self.pfl = []
        # self.pflOO = []
        # self.front = []
        # self.frontOO = []
        # self.blat = 0
        # self.acc = []
        self.sep_space_h = self.height - (2 * self.thick_pal)
        self.sep_space_w = self.width - (2 * self.thick_pal)
        self.sep_max_depth = depth - self.cant
        # self.sep_prev = ""
        # self.arch = []  # matricea de arhitectura care contine elementele corpului orientate si cu offset
        self.position = [0, 0, 0, 0, 0, 0]  # TODO de folosit pozitia corpului
        self.cant_length = [['0.4', 0], ['2', 0]]

    def append(self, obj):
        self.material_list.append(obj)

    def remove_material(self, item_type, label):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == item_type and self.material_list[i].label == label:
                index = i
        self.material_list.pop(index)

    def remove_all_pfl(self):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pfl":
                index = i
        self.material_list.pop(index)

    def add_pfl(self):
        placa = Pfl(self.label + ".pfl", self.width - 4, self.height - 4)
        placa.rotate("x")
        placa.move("y", self.depth + 1 + 4)
        placa.move("x", 2)
        placa.move("z", 2)
        self.append(placa)
        self.append(accesoriu("surub PFL", 2 * round(self.height / 150) + 2 * round(self.width / 150)))

    def get_item_by_type_label(self, typ, lab):
        """

        :param typ: type of item to be returned
        :param lab: label of item to be returned
        :return: index of item found in material_list vector
        """
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == typ and self.material_list[i].label == lab:
                index = i
        if 'index' in locals():
            return self.material_list.__getitem__(index)
        else:
            raise NameError("ERROR: element ", lab, " of type ", typ, " not found.")

    def add_front(self, split_list, tip):
        """

        :param split_list: [[front1_%height,front1_%width][front2_%height,front2_%width]]
        :param tip: "door" "drawer" "cover"
        :return: none
        """

        h_tot = self.height - self.front_gap
        h_count = 0
        w_count = 0
        w_tot = self.width - self.front_gap
        origin = [self.front_gap, self.front_gap]
        for i in range(len(split_list)):
            split = split_list[i]
            h = int((h_tot * split[0] / 100) - self.front_gap)
            w = int((w_tot * split[1] / 100) - self.front_gap)
            usa = Front(self.label + "_" + str(i + 1), h, w, self.thick_front)
            usa.rotate("x")
            usa.move("x", origin[0])
            usa.move("z", origin[1])
            usa.rotate("y")
            usa.move("x",usa.width)
            if w_count != 100:
                origin[0] += usa.width + int(self.front_gap / 2)
                w_count += split[1]
                if w_count == 100:
                    origin[0] = self.front_gap
                    w_count = 0
                    if h_count != 100:
                        origin[1] += usa.length + int(self.front_gap / 2)
                        h_count += split[0]

            self.append(usa)
            if tip == "door":
                if (h * w) > 280000:
                    self.append(accesoriu("balama aplicata", 3))
                    self.append(accesoriu("amortizor", 2))
                    self.append(accesoriu("surub 3.5x16", 12))
                else:
                    self.append(accesoriu("balama aplicata", 2))
                    self.append(accesoriu("amortizor", 1))
                    self.append(accesoriu("surub 3.5x16", 8))
                self.append(accesoriu("maner", 1))
            elif tip == "cover":
                self.append(accesoriu("surub intre corpuri", math.ceil(h * w / 40000)))
            elif tip == "drawer":
                self.append(accesoriu("maner", 1))

    # def addLeg(self, leg_width, placa_cant):
    #     """
    #     Adauga o placa orizontala in interiorul corpului, de o latime specificata si cant pe lungimi (TRUE/FLASE)
    #     :param leg_width:
    #     :param placa_cant:
    #     :return:
    #     """
    #     if placa_cant:
    #         placa = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), leg_width, self.thick_pal,
    #                          self.cant_lab, self.cant_lab, "", "")
    #     else:
    #         placa = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), leg_width, self.thick_pal, "", "",
    #                          "", "")
    #     self.addPalObject(placa)
    #     self.addAcces("surub", 4)

    def add_pol(self, nr, cant):
        """
        adauga polite intr-un corp
        :param nr: numarul politelor de adaugat in corp
        :param cant: tipul de cant 0,4 sau 2 (ca si numar)
        :return: none
        """
        # TODO: adancimea trebe scazuta cu grosimea cantului si inca nu merge corect
        pol_lung = self.width - (2 * self.thick_pal)
        pol_lat = (self.depth - 20)
        for i in range(nr):
            pol = PlacaPal(self.label + ".pol", pol_lung, pol_lat, self.thick_pal, cant, "", "", "")
            pol.move("x", self.thick_pal)
            pol.move("z", round(self.height / (nr + 1)) * (i + 1))
            pol.move("y", 20)
            self.append(pol)
            self.append(accesoriu("bolt polita", 4))
            self.append(accesoriu("surub PFL", 2))

    def add_separator(self, orient, sep_cant):

        sep_cant_thk = round(sep_cant)
        if orient == "h":
            sep_l = self.sep_space_w
            sep_w = self.sep_max_depth
            sep = PlacaPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            # self.addPalObject(sep)
            # self.addPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")

            self.sep_space_h = round((self.sep_space_h - self.thick_pal) / 2)
            if self.sep_prev == "v" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "h"
            self.addAcces("surub", 4)
            sep.move("x", self.thick_pal)
            sep.move("z", round(self.sep_space_h))
        if orient == "v":
            sep_l = self.sep_space_h
            sep_w = self.sep_max_depth
            sep = PlacaPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            self.addPalObject(sep)

            self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)
            # self.addPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            if self.sep_prev == "h" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "v"

            sep.rotate("y")
            sep.move("x", self.thick_pal + round(self.sep_space_w))
            sep.move("z", self.thick_pal)
            self.addAcces("surub", 4)

    def add_wine_shelf(self, goluri, left_right, cant):
        offset_z = round((self.height - ((goluri + 1) * self.thick_pal)) / goluri)
        if left_right == "left":
            self.add_sep_v(self.height - (2 * self.thick_pal), offset_z, 0, cant)
            for x in range(goluri - 1):
                self.add_sep_h(offset_z, 0, (offset_z * (x + 1)) + (self.thick_pal * (x)), cant)
        if left_right == "right":
            self.add_sep_v(self.height - (2 * self.thick_pal), self.width - offset_z - (3 * self.thick_pal), 0, cant)
            for x in range(goluri - 1):
                self.add_sep_h(offset_z, self.width - offset_z - (2 * self.thick_pal),
                               (offset_z * (x + 1)) + (self.thick_pal * x), cant)
        if offset_z < 90:
            print("ERROR: nu incap sticlele de vin in " + self.label)

    def add_sep_v(self, height, offset_x, offset_z, sep_cant):
        """

        :param height:
        :param offset_x:
        :param offset_z:
        :param sep_cant:
        :return:
        """
        sep_l = height
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.append(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.rotate("y")
        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.append(accesoriu("surub", 4))

    def add_sep_h(self, width, offset_x, offset_z, sep_cant):
        sep_l = width
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.append(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.append(accesoriu("surub", 4))

    def add_front_lateral_2(self, left_right):
        front = Front(self.label + ".fr_lat", self.height, self.depth, self.thick_front)
        if left_right == "left":
            front.rotate("y")
        elif left_right == "right":
            front.rotate("y")
            front.move("x", self.width)
        self.append(front)

    def add_front_lateral(self):
        self.front = self.front + [["front", self.label + ".lat", self.height, self.depth]]

    def add_front_manual(self, height, width, offset_x, offset_z):
        fr = Front(self.label + ".man", height, width, self.thick_front)
        fr.rotate("x")
        fr.rotate("y")
        fr.move("x", fr.width)
        fr.move("x", self.front_gap)
        fr.move("z", self.front_gap)
        fr.move("x", offset_x)
        fr.move("z", offset_z)
        # fr.move("y", - self.thick_front)
        self.append(fr)

    def add_tandem_box(self, tip):
        fund_label = self.label + ".ser.jos"
        spate_label = self.label + ".ser.sp"
        fund_lung = int(self.width - (2 * self.thick_pal) - (37.5 * 2))
        spate_lung = self.width - 2 * 18 - 87
        fund_lat = self.depth - 20
        if tip == "M":
            spate_lat = 68
        elif tip == "D":
            spate_lat = 183
        fund = PlacaPal(fund_label, fund_lung, fund_lat, 16, "", "", "", "")
        fund.move("x", self.thick_pal + 13)
        fund.move("z", self.thick_pal + 3)
        self.append(fund)

        spate = PlacaPal(spate_label, spate_lung, spate_lat, 16, self.cant_lab, "", "", "")
        spate.rotate("x")
        spate.move("x", self.thick_pal + 20)
        spate.move("y", fund.width)
        self.append(spate)
        self.append(accesoriu("tandembox " + tip, 1))
        self.append(accesoriu("surub 3.5x16", 18))

    def add_sertar(self, sert_h, offset):
        # sertar de tacamuri de 100, sertare adanci de 200

        gap_glisiera = 13
        height_offset = offset
        sert_thick_pal = self.thick_pal
        sert_lat = self.width - (2 * self.thick_pal) - (2 * gap_glisiera)
        sert_depth = self.depth - gap_glisiera

        long1 = PlacaPal(self.label + ".ser.long", sert_depth, sert_h, sert_thick_pal, self.cant_lab, "", "", "")
        long1.rotate("x")
        long1.rotate("z")
        long1.move("x", self.thick_pal + gap_glisiera)
        long1.move("z", height_offset)
        self.addPalObject(long1)

        lat1 = PlacaPal(self.label + ".ser.lat", sert_lat - (2 * sert_thick_pal), sert_h, sert_thick_pal,
                        self.cant_lab, "", "", "")
        lat1.rotate("x")
        lat1.move("x", self.thick_pal + sert_thick_pal + gap_glisiera + 1)
        lat1.move("z", height_offset)
        self.addPalObject(lat1)

        lat2 = PlacaPal(self.label + ".ser.lat", sert_lat - (2 * sert_thick_pal), sert_h, sert_thick_pal,
                        self.cant_lab, "", "", "")
        lat2.rotate("x")
        lat2.move("x", self.thick_pal + sert_thick_pal + gap_glisiera + 1)
        lat2.move("y", long1.length - lat2.thick)
        lat2.move("z", height_offset)
        self.addPalObject(lat2)

        long2 = PlacaPal(self.label + ".ser.long", sert_depth, sert_h, sert_thick_pal, self.cant_lab, "", "", "")
        long2.rotate("x")
        long2.rotate("z")
        long2.move("x", self.thick_pal + lat1.thick + gap_glisiera + lat2.length + 2)
        long2.move("z", height_offset)
        self.addPalObject(long2)

        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.thick_pal), sert_h,self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.thick_pal), sert_h,self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.thick_pal, self.cant_lab, "", "", "")
        self.pfl = self.pfl + [["pfl", self.label + ".ser.pfl", sert_lat - 4, sert_depth - 4]]
        self.addAcces("pereche glisiera " + str(self.depth) + " mm", 1)
        self.addAcces("surub 3.5x16", 12)
        self.addAcces("surub", 8)
        self.addAcces("surub PFL", 2 * round(sert_lat / 100) + 2 * round(sert_depth / 100))

    ################
    # BUILD CORPURI#
    ################
    '''
    def buildBaseBox(self):

        picioare = math.ceil(self.width / 400) * 2
        self.append(accesoriu("picioare", picioare))
        self.append(accesoriu("clema plinta", picioare / 2))
        self.append(accesoriu("surub 3.5x16", picioare * 4))  # pentru picioare
        self.append(accesoriu("surub blat", 4))
        self.append(accesoriu("surub", 14))
        self.append(accesoriu("plinta", self.width / 1000))
        self.append(accesoriu("sipca apa", self.width / 1000))
        self.append(Blat(self.label + ".blat", self.width, self.width_blat, self.thick_blat))

        # arhitectura
        # jos
        jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, self.cant_lab, "", self.cant_lab,
                       self.cant_lab)
        self.append(jos)

        # lat rotit pe Y si ridicat pe z cu grosimea lui jos
        lat1 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth, self.thick_pal, self.cant_lab,
                        "", "", "")
        lat1.rotate("y")
        lat1.move("z", jos.thick)
        self.append(lat1)

        # lat rotit pe y, translatat pe x cu (jos - grosime), translatat pe z cu grosime jos
        lat2 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth, self.thick_pal, self.cant_lab,
                        "", "", "")
        lat2.rotate("y")
        lat2.move("x", jos.length - lat2.thick)
        lat2.move("z", jos.thick)
        self.append(lat2)

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg), si pe x cu grosime lat
        leg1 = PlacaPal(self.label + ".leg", self.width - (2 * (self.thick_pal + self.cant)), 100, self.thick_pal,
                        self.cant_lab, self.cant_lab, "", "")
        leg1.move("z", lat1.length + jos.thick - leg1.thick)
        leg1.move("x", lat1.thick)
        self.append(leg1)

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg)
        #               pe y cu (latime lat - latime leg)
        #               pe x cu grosime lat
        leg2 = PlacaPal(self.label + ".leg", self.width - (2 * (self.thick_pal + self.cant)), 100, self.thick_pal,
                        self.cant_lab, self.cant_lab, "", "")
        leg2.move("z", lat1.length + jos.thick - leg1.thick)
        leg2.move("y", lat1.width - leg2.width)
        leg2.move("x", lat1.thick)
        self.append(leg2)

        self.addPFL()

    def buildBaseCorner(self, cut_width, cut_depth, l_r, front_thick, withPolita):
        #    o---------width----------|   o------width-----------
        #    |                        |   |                     |
        #    |     l_r="left"         |   |    l_r="right"      |
        #    |                        |   |                     |
        #    depth                    |   |                     depth
        #    |        ----cut_width----   --- cut_width--       |
        #    |        |                                 |       |
        #    |        cut_depth                  cut_depth      |
        #    |        |                                 |       |
        #    ----------                                 ---------
        # include PFL si fronturi

        if l_r == "left":
            jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, "", "", "", "")
            jos.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width) + ":" + str(self.depth - cut_depth) + ":" + str(cut_width) + "(cant " + str(
                self.cant_lab) + "):" + str(cut_depth) +
                        "(cant " + str(self.cant_lab) + "):" + str(self.width - cut_width) + ":" + str(self.depth))
            self.addPalObject(jos)
            jos.move("y", -cut_depth)

            lat1 = PlacaPal(self.label + ".lat1", self.height - self.thick_pal, self.depth - cut_depth, self.thick_pal,
                            self.cant_lab, "", "", "")
            self.addPalObject(lat1)
            lat1.rotate("x")
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("z", self.thick_pal)
            lat1.move("x", jos.length - self.thick_pal)
            lat1.move("y", cut_depth)
            lat1.move("y", -cut_depth)

            lat2 = PlacaPal(self.label + ".lat2", self.height - self.thick_pal, self.width - cut_width, self.thick_pal,
                            self.cant_lab, "", "", "")
            self.addPalObject(lat2)

            lat2.rotate("x")
            lat2.rotate("y")
            lat2.move("z", self.thick_pal)
            lat2.move("y", -cut_depth)

            spate = PlacaPal(self.label + ".spate", self.depth - self.thick_pal, self.height - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            self.addPalObject(spate)
            spate.rotate("x")
            spate.rotate("z")
            spate.move("z", self.thick_pal)
            spate.move("y", self.thick_pal)
            spate.move("y", -cut_depth)

            leg1 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "",
                            "", "")
            self.addPalObject(leg1)
            leg1.move("z", self.height - self.thick_pal)
            leg1.move("x", self.thick_pal)
            leg1.move("y", self.depth - leg1.width)
            leg1.move("y", -cut_depth)

            leg2 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "",
                            "", "")
            self.addPalObject(leg2)
            leg2.rotate("x")
            leg2.move("z", self.height - leg2.width)
            leg2.move("y", cut_depth)
            leg2.move("x", self.thick_pal)
            leg2.move("y", -cut_depth)

            leg3 = PlacaPal(self.label + ".leg", cut_depth - self.thick_pal, 100, self.thick_pal, self.cant_lab, "",
                            "",
                            "")
            self.addPalObject(leg3)
            leg3.rotate("x")
            leg3.rotate("z")
            leg3.move("z", self.height - leg3.width)
            leg3.move("x", self.width - cut_width - self.thick_pal)
            leg3.move("y", self.thick_pal)
            leg3.move("y", -cut_depth)

            if withPolita:
                pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal),
                               self.depth - (1 * self.thick_pal),
                               self.thick_pal, "", "", "", "")

                pol.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                            str(self.width - (2 * self.thick_pal)) + ":" +
                            str(self.depth - cut_depth - 20) + ":" +
                            str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                            str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                            str(self.width - cut_width - self.thick_pal - 20) + ":" +
                            str(self.depth - self.thick_pal))

                self.addPalObject(pol)
                pol.move("x", self.thick_pal)
                pol.move("y", self.thick_pal)
                pol.move("z", int((self.height - self.thick_pal) / 2))
                pol.move("y", -cut_depth)

            self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]

        elif l_r == "right":
            jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, "", "", "", "")
            jos.add_obs(
                str("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                    str(self.width) + ":" + str(self.depth) + ":" + str(self.width - cut_width) + ":" + str(
                    cut_depth) + "(cant " + str(self.cant_lab) + "):" +
                    str(cut_width) + "(cant " + str(self.cant_lab) + "):" + str(self.depth - cut_depth)))
            self.addPalObject(jos)
            jos.move("y", -cut_depth)

            lat1 = PlacaPal(self.label + ".lat1", self.height - self.thick_pal, self.depth - cut_depth, self.thick_pal,
                            self.cant_lab, "", "", "")
            self.addPalObject(lat1)
            lat1.rotate("x")
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("z", self.thick_pal)

            lat2 = PlacaPal(self.label + ".lat2", self.height - self.thick_pal, self.width - cut_width, self.thick_pal,
                            self.cant_lab, "", "", "")
            self.addPalObject(lat2)

            lat2.rotate("x")
            lat2.rotate("y")
            lat2.move("z", self.thick_pal)
            lat2.move("y", -cut_depth)
            lat2.move("x", cut_width)

            spate = PlacaPal(self.label + ".spate", self.depth - self.thick_pal, self.height - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            self.addPalObject(spate)
            spate.rotate("x")
            spate.rotate("z")
            spate.move("z", self.thick_pal)
            spate.move("y", self.thick_pal)
            spate.move("y", -cut_depth)
            spate.move("x", self.width - self.thick_pal)

            leg1 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "",
                            "", "")
            self.addPalObject(leg1)
            leg1.move("z", self.height - self.thick_pal)
            leg1.move("x", self.thick_pal)
            leg1.move("y", self.depth - leg1.width)
            leg1.move("y", -cut_depth)

            leg2 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "",
                            "", "")
            self.addPalObject(leg2)
            leg2.rotate("x")
            leg2.move("z", self.height - leg2.width)
            leg2.move("y", cut_depth)
            leg2.move("x", self.thick_pal)
            leg2.move("y", -cut_depth)

            leg3 = PlacaPal(self.label + ".leg", cut_depth - self.thick_pal, 100, self.thick_pal, self.cant_lab, "",
                            "",
                            "")
            self.addPalObject(leg3)
            leg3.rotate("x")
            leg3.rotate("z")
            leg3.move("z", self.height - leg3.width)
            leg3.move("x", cut_width)
            leg3.move("y", self.thick_pal)
            leg3.move("y", -cut_depth)

            if withPolita:
                pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal),
                               self.depth - (1 * self.thick_pal),
                               self.thick_pal, "", "", "", "")

                pol.add_obs(
                    "decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                    str(self.width - (2 * self.thick_pal)) + ":" +
                    str(self.depth - self.thick_pal) + ":" +
                    str(self.width - cut_width - self.thick_pal - 20) + ":" +
                    str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                    str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                    str(self.depth - cut_depth - 20) + ":")

                self.addPalObject(pol)
                pol.move("x", self.thick_pal)
                pol.move("y", self.thick_pal)
                pol.move("z", int((self.height - self.thick_pal) / 2))
                pol.move("y", -cut_depth)

            self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]

        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPFLObject()
        self.getPFLOO()[0].getPlacaOO().move("y", - cut_depth)

        self.addAcces("balama usa franta", 2)
        self.addAcces("balama 170 deg", 2)
        self.addAcces("surub 3.5x16", 4 * 4)  # pentru balamale
        self.addAcces("picioare", 6)
        self.addAcces("clema plinta", 3)
        self.addAcces("surub 3.5x16", 3 * 4)  # pentru picioare
        self.addAcces("surub blat", 4)
        self.addAcces("L", 2)
        self.addAcces("surub", 19)
        self.addAcces("plinta", (cut_width + cut_depth) / 1000)
        self.addAcces("sipca apa", (self.width + self.depth) / 1000)
        self.addBlat((self.width + self.depth) / 1000)
    '''
    def buildTopCorner(self, cut_width, cut_depth, l_r, front_thick):

        #    o---------width----------|   o------width-----------
        #    |                        |   |                     |
        #    |     l_r="left"         |   |    l_r="right"      |
        #    |                        |   |                     |
        #    depth                    |   |                     depth
        #    |        ----cut_width----   --- cut_width--       |
        #    |        |                                 |       |
        #    |        cut_depth                  cut_depth      |
        #    |        |                                 |       |
        #    ----------                                 ---------
        # include PFL si fronturi
        if l_r == "left":
            # placa de jos
            jos = PlacaPal(self.label + ".jos", self.width - (2 * self.thick_pal), self.depth - self.thick_pal,
                           self.thick_pal,
                           "", "", "", "")
            jos.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - self.thick_pal) + ":" +
                        str(self.depth - cut_depth) + ":" +
                        str(cut_width - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_depth - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.width - cut_width) + ":" +
                        str(self.depth - self.thick_pal))
            self.addPalObject(jos)
            jos.move("y", self.thick_pal)
            jos.move("x", self.thick_pal)
            jos.move("y", -cut_depth)
            # placa de sus
            sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - self.thick_pal,
                           self.thick_pal,
                           "", "", "", "")
            sus.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - self.thick_pal) + ":" +
                        str(self.depth - cut_depth) + ":" +
                        str(cut_width - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_depth - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.width - cut_width) + ":" +
                        str(self.depth - self.thick_pal))
            self.addPalObject(sus)
            sus.move("y", self.thick_pal)
            sus.move("x", self.thick_pal)
            sus.move("z", self.height - self.thick_pal)
            sus.move("y", -cut_depth)

            pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal), self.depth - (1 * self.thick_pal),
                           self.thick_pal, "", "", "", "")

            pol.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - (2 * self.thick_pal)) + ":" +
                        str(self.depth - cut_depth - 20) + ":" +
                        str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.width - cut_width - self.thick_pal - 20) + ":" +
                        str(self.depth - self.thick_pal))
            self.addPalObject(pol)
            pol.move("x", self.thick_pal)
            pol.move("y", self.thick_pal)
            pol.move("z", int((self.height - self.thick_pal) / 2))
            pol.move("y", -cut_depth)

            spate = PlacaPal(self.label + ".spate", self.height, self.depth - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            self.addPalObject(spate)
            spate.rotate("y")
            spate.move("y", self.thick_pal)
            # spate.move("z", self.thick_pal)
            spate.move("y", -cut_depth)

            lat1 = PlacaPal(self.label + ".lat1", self.height, self.width - cut_width, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            self.addPalObject(lat1)
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("y", -cut_depth)

            lat2 = PlacaPal(self.label + ".lat2", self.height, self.depth - cut_depth, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            self.addPalObject(lat2)
            lat2.rotate("y")
            lat2.move("x", self.width - self.thick_pal)
            lat2.move("y", self.depth - lat2.width)
            lat2.move("y", -cut_depth)

            self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]


        elif l_r == "right":
            # placa de jos
            jos = PlacaPal(self.label + ".jos", self.width - (2 * self.thick_pal), self.depth - self.thick_pal,
                           self.thick_pal,
                           "", "", "", "")
            jos.add_obs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - self.thick_pal) + ":" +
                        str(self.depth - self.thick_pal) + ":" +
                        str(self.width - cut_width) + ":" +
                        str(cut_depth - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_width - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.depth - cut_depth) + ":")
            self.addPalObject(jos)
            jos.move("y", self.thick_pal)
            jos.move("y", -cut_depth)
            jos.move("x", self.thick_pal)

            # placa de sus
            sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - self.thick_pal,
                           self.thick_pal,
                           "", "", "", "")
            sus.add_obs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - self.thick_pal) + ":" +
                        str(self.depth - self.thick_pal) + ":" +
                        str(self.width - cut_width) + ":" +
                        str(cut_depth - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_width - self.thick_pal) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.depth - cut_depth) + ":")

            self.addPalObject(sus)
            sus.move("y", self.thick_pal)
            sus.move("z", self.height - self.thick_pal)
            sus.move("y", -cut_depth)
            sus.move("x", self.thick_pal)

            pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal), self.depth - (1 * self.thick_pal),
                           self.thick_pal, "", "", "", "")
            pol.add_obs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - (2 * self.thick_pal)) + ":" +
                        str(self.depth - self.thick_pal) + ":" +
                        str(self.width - cut_width - self.thick_pal - 20) + ":" +
                        str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.depth - cut_depth - 20) + ":")
            self.addPalObject(pol)
            pol.move("x", self.thick_pal)
            pol.move("y", self.thick_pal)
            pol.move("z", int((self.height - self.thick_pal) / 2))
            pol.move("y", -cut_depth)

            spate = PlacaPal(self.label + ".spate", self.height, self.depth - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            self.addPalObject(spate)
            spate.rotate("y")
            spate.move("y", self.thick_pal)
            spate.move("x", self.width - self.thick_pal)
            # spate.move("z", self.thick_pal)
            spate.move("y", -cut_depth)

            lat1 = PlacaPal(self.label + ".lat1", self.height, self.width - cut_width, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            self.addPalObject(lat1)
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("y", -cut_depth)
            lat1.move("x", cut_width)

            lat2 = PlacaPal(self.label + ".lat2", self.height, self.depth - cut_depth, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            self.addPalObject(lat2)
            lat2.rotate("y")
            # lat2.move("x", self.width - self.thick_pal)
            # lat2.move("y", self.depth - lat2.width)
            # lat2.move("y", -cut_depth)

            self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]


        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPFLObject()

        self.addAcces("balama usa franta", 2)
        self.addAcces("balama 170 deg", 2)
        self.addAcces("surub 3.5x16", 4 * 4)  # pentru balamale
        self.addAcces("surub", 20)
        self.addAcces("pereche clema prindere perete", 1)
        self.addAcces("sina perete", self.width / 1000)
        self.addAcces("surub diblu perete", round(self.width / 201))

    def buildJolyBox(self):
        self.buildBaseBox()
        self.addAcces("Joly" + str(self.width) + str(self.depth), 1)
        self.addAcces("surub 3.5x16", 8)  # prentu glisiere
        self.addAcces("surub 3.5x16", 8)  # pentru front
        self.addPFLObject()
        self.add_front([[100, 100]], 2, "door")

    def buildMsVBox(self):
        # self.addAcces("blat",self.width/1000)
        self.addAcces("sipca apa", self.width / 1000)
        self.addAcces("plinta", self.width / 1000)
        self.addAcces("surub intre corpuri", 10)
        self.addBlat(self.width / 1000)
        self.add_front([[100, 100]], 2, "door")

    def buildTower(self, gap_list, gap_heat, front_list):
        self.depth = self.depth - gap_heat
        jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, self.cant_lab, "", self.cant_lab,
                       self.cant_lab)
        self.addPalObject(jos)

        lat1 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth + gap_heat, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat1.rotate("y")
        lat1.move("z", jos.thick)
        self.addPalObject(lat1)

        lat2 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth + gap_heat, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat2.rotate("y")
        lat2.move("z", jos.thick)
        lat2.move("x", jos.length - lat2.thick)
        self.addPalObject(lat2)

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("x", lat1.thick)
        sus.move("z", lat1.length)
        self.addPalObject(sus)

        self.add_sep_h(self.width - 2 * self.thick_pal, 0, gap_list[0], self.cant_lab)
        self.add_sep_h(self.width - 2 * self.thick_pal, 0, gap_list[0] + gap_list[1] + self.thick_pal, self.cant_lab)
        self.add_sep_h(self.width - 2 * self.thick_pal, 0,
                       gap_list[0] + gap_list[1] + gap_list[2] + (2 * self.thick_pal), self.cant_lab)
        # self.addSeparator("h",self.cant_lab)
        # self.addSeparator("h",self.cant_lab)
        self.addAcces("surub", 8)
        self.addAcces("plinta", self.width / 1000)
        picioare = math.ceil(self.width / 400) * 2
        self.addAcces("picioare", picioare)
        self.addAcces("clema plinta", picioare / 2)
        self.addAcces("surub 3.5x16", picioare * 4)  # pentru picioare

        self.addPFLObject()

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
            self.add_front_manual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3.5 * self.thick_pal) - 3,
                                  self.width - 4)

    ############
    ## UTILS ###
    ############

    def getLabel(self):
        print(self.label)

    def printPal(self):
        corp = self.pal
        for i in range(len(corp)):
            print(corp[i])

    def printCorp(self):
        corp = self.pal + self.pfl + self.front + self.acc
        for i in range(len(corp)):
            print(corp[i])

    def printAcc(self):
        acc = self.acc
        for i in range(len(acc)):
            print(acc[i])

    def getPal(self):
        return self.pal

    def getCorp(self):
        return self.pal + self.pfl + self.front + self.acc

    def getPFL(self):
        return self.pfl

    # def getPFLOO(self):
    #     return self.pflOO

    def getFront(self):
        return self.front

    def getAcces(self):
        return self.acc

    def get_m2_pal(self):

        m2pal = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pal":
                m2pal = m2pal + self.material_list[i].get_m2()
        return m2pal

    def get_m2_pfl(self):

        m2pfl = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pfl":
                m2pfl = m2pfl + self.material_list[i].get_m2()
        return m2pfl

    def get_m2_front(self):

        m2 = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "front":
                m2 = m2 + self.material_list[i].get_m2()
        return m2

    def get_m_cant(self, type):
        '''
        :param type: "0.4" sau "2"
        :return: lungimea cantului selectat din tot corpul
        '''
        m = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pal":
                m = m + self.material_list[i].get_m_cant(type)
        return m

    ############
    ## EXPORT ##
    ############

    def exportCSV(self, mobila):
        with open('comanda_pal.csv', mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(mobila)):
                p = mobila[i].getPal()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getPFL()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getFront()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getAcces()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])

    def rotate(self, axis):
        for i in range(len(self.material_list)):
            if isinstance(self.material_list[i], Placa):
                self.material_list[i].rotate(axis)
                initial_position = self.material_list[i].__getattribute__("position")
                final_position = initial_position
                offset_x = initial_position[3]
                offset_y = initial_position[4]
                offset_z = initial_position[5]
                if axis == "x":
                    final_position[3] = offset_x
                    final_position[4] = -offset_z
                    final_position[5] = offset_y
                elif axis == "y":
                    final_position[3] = -offset_z
                    final_position[4] = offset_y
                    final_position[5] = offset_x
                elif axis == "z":
                    final_position[3] = offset_y
                    final_position[4] = -offset_x
                    final_position[5] = offset_z
                self.material_list[i].position = final_position

    def move(self, axis, offset):
        for i in range(len(self.material_list)):
            if isinstance(self.material_list[i], Placa):
                self.material_list[i].move(axis,offset)

    def drawCorp(self, filename, ox, oy, oz):
        for i in range(len(self.material_list)):
            if isinstance(self.material_list[i], Placa):
                export_stl(filename,
                          self.material_list[i].label + str(i),
                          self.material_list[i].position[0],
                          self.material_list[i].position[1],
                          self.material_list[i].position[2],
                          self.material_list[i].position[3] + ox,
                          self.material_list[i].position[4] + oy,
                          self.material_list[i].position[5] + oz)


