# documentation
"""
--Comanda (class)
    corpuri
    --corp (class) [BaseBox, Raft, Bar, JollyBox, TopBox, SinkBox, TowerBox, MsVBox]
        material_list
            --placa (class) [PlacaPal, Front, Pfl, Blat]
            --accesoriu (class)

"""
# documentation
import os
import openpyxl

from architectures.kitchen import *
import shutil


# MATERIAL_PAL = "W962ST2"
# MATERIAL_PFL = "Alb"
# MATERIAL_BLAT = "Blat Stejar Bardolino"
# MATERIAL_FRONT = "A34/R3"


'''
class Placa:
    def __init__(self, label, length, width, thick):
        """
        :param label: eticheta
        :param length: lungimea
        :param width: latimea
        :param thick: grosimea
        """

        self.label = label
        self.length = length
        self.width = width
        self.thick = thick
        self.obs = ""
        self.position = [self.length, self.width, self.thick, 0, 0, 0]  # pozitia placii
                      # (dim_x,       dim_y,      dim_z,    offset_x, offset_y, offset_z)
        self.type = ""  # pal, pfl, front
        self.material = ""
        self.price = 0

    def add_obs(self, text):
        self.obs = self.obs + text

    def set_material(self, material):
        self.material = material

    def rotate(self, axis):
        # axis = "x"/"y"/"z"
        init_x = self.position[0]
        init_y = self.position[1]
        init_z = self.position[2]
        if axis == "x":
            self.position[0] = init_x
            self.position[1] = -init_z
            self.position[2] = init_y
        elif axis == "y":
            self.position[0] = -init_z
            self.position[1] = init_y
            self.position[2] = init_x
        elif axis == "z":
            self.position[0] = init_y
            self.position[1] = -init_x
            self.position[2] = init_z
        else:
            self.position[0] = init_x
            self.position[1] = init_y
            self.position[2] = init_z

    def move(self, axis, offset):
        if axis == "x":
            self.position[3] = self.position[3] + int(offset)
        if axis == "y":
            self.position[4] = self.position[4] + int(offset)
        if axis == "z":
            self.position[5] = self.position[5] + int(offset)

    def draw_placa(self, file_name, ox, oy, oz):
        exportStl(file_name, self.label, self.length, self.width, self.thick, ox, oy, oz)

    def get_m2(self):
        return self.length * self.width / 1000000
class PlacaPal(Placa):

    def __init__(self, label, length, width, thick, cant_L1, cant_L2, cant_l1, cant_l2):
        super().__init__(label, length, width, thick)
        self.cant_list = [cant_L1, cant_L2, cant_l1, cant_l2]
        self.type = "pal"
        self.material = ""
        length_cant04 = 0
        length_cant2 = 0
        for i in range(2):
            if self.cant_list[i] == 0.4:
                length_cant04 = length_cant04 + self.length
            if self.cant_list[i] == 2:
                length_cant2 = length_cant2 + self.length
            if self.cant_list[i + 2] == 0.4:
                length_cant04 = length_cant04 + self.width
            if self.cant_list[i + 2] == 2:
                length_cant2 = length_cant2 + self.width
        self.cant_length = [['0.4', length_cant04], ['2', length_cant2]]

        # with open('price_list.csv') as price_list_file:
        #     price_reader = csv.DictReader(price_list_file, delimiter=',')
        #     found = False
        #     for row in price_reader:
        #         if row["Item"] == self.material:
        #             found = True
        #             self.price = float(row["Price"]) * (self.length * self.width / 1000000)
        #     if found == False:
        #         raise NameError("ERROR: Price for " + self.material + " not found. Setting to 0 RON.")

    def get_m_cant(self, cant_type):
        """
        :param cant_type: "0.4" sau "2"
        :return: length of selected cant
        """
        if cant_type == "0.4":
            return self.cant_length[0][1] / 1000
        elif cant_type == "2":
            return self.cant_length[1][1] / 1000
        else:
            raise Exception("ERROR: Unknown cant type!")
class Front(Placa):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "front"
        self.material = ""
class Pfl(Placa):
    def __init__(self, label, length, width):
        super().__init__(label, length, width, 4)
        self.type = "pfl"
        self.material = ""
        # with open('price_list.csv') as price_list_file:
        #     price_reader = csv.DictReader(price_list_file, delimiter=',')
        #     found = False
        #     for row in price_reader:
        #         if row["Item"] == self.type and row["Material"] == self.material:
        #             found = True
        #             self.price = float(row["Price"]) / (2.8 * 2.07) * (self.length * self.width / 1000000)
        #             # TODO de folosit pretul pe m2 nu pe coala
        #     if not found:
        #         raise NameError("ERROR: Price for " + self.material + " not found. Setting to 0 RON.")
class Blat(Placa):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "blat"
        self.material = ""
        # with open('price_list.csv') as price_list_file:
        #     price_reader = csv.DictReader(price_list_file, delimiter=',')
        #     found = False
        #     for row in price_reader:
        #         if row["Item"] == self.material:
        #             found = True
        #             self.price = float(row["Price"]) * length / 1000
        #     if not found:
        #         raise NameError("ERROR: Price for " + self.material + " not found. Setting to 0 RON.")
'''

'''
class accesoriu:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
        self.type = "accesoriu"
        with open('price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Material"] == self.name:
                    found = True
                    # print(row["Price"])
                    self.price = float(row["Price"])
            if found == False:
                print("ERROR: Price for ", self.name, " not found. Setting to 0 RON.")

    def printAcces(self):
        print("Accesoriu: ", self.name, " Pieces:", self.price, " Price: ", self.price)

    def addPieces(self, number):
        self.pieces = self.pieces + number
'''

'''
class corp:
    def __init__(self, label, height, width, depth, rules):
        
        :param label: eticheta
        :param height: inaltimea
        :param width: latimea
        :param depth: adancimea
        :param rules: lista de reguli
        
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

    def remove(self, item_type, label):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == item_type and self.material_list[i].label == label:
                index = i
        self.material_list.pop(index)

    def addPFL(self):
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
            raise NameError("ERROR: elementul ", lab, " de tip ", typ, " nu a fost gasit")

    def remove_pfl(self):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pfl":
                index = i
        self.material_list.pop(index)

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

    def addSeparator(self, orient, sep_cant):

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

    def addWineShelf(self, goluri, left_right, cant):
        offset_z = round((self.height - ((goluri + 1) * self.thick_pal)) / goluri)
        if left_right == "left":
            self.addSepV(self.height - (2 * self.thick_pal), offset_z, 0, cant)
            for x in range(goluri - 1):
                self.addSepH(offset_z, 0, (offset_z * (x + 1)) + (self.thick_pal * (x)), cant)
        if left_right == "right":
            self.addSepV(self.height - (2 * self.thick_pal), self.width - offset_z - (3 * self.thick_pal), 0, cant)
            for x in range(goluri - 1):
                self.addSepH(offset_z, self.width - offset_z - (2 * self.thick_pal),
                             (offset_z * (x + 1)) + (self.thick_pal * x), cant)
        if offset_z < 90:
            print("ERROR: nu incap sticlele de vin in " + self.label)

    def addSepV(self, height, offset_x, offset_z, sep_cant):
        sep_l = height
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.addPalObject(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.rotate("y")
        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.addAcces("surub", 4)

    def addSepH(self, width, offset_x, offset_z, sep_cant):
        sep_l = width
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.append(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.append(accesoriu("surub", 4))

    def addFrontLateral(self):
        self.front = self.front + [["front", self.label + ".lat", self.height, self.depth]]

    def addFrontManual(self, height, width):
        fr = Front(self.label + ".man", height, width, self.thick_front)
        fr.rotate("x")
        fr.rotate("y")
        fr.move("x", self.front_gap)
        fr.move("z", self.front_gap)
        fr.move("y", -self.thick_front)
        self.append(fr)

    def addTandemBox(self, tip):
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

    def addSertar(self, sert_h, offset):
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

        self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0], self.cant_lab)
        self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0] + gap_list[1] + self.thick_pal, self.cant_lab)
        self.addSepH(self.width - 2 * self.thick_pal, 0, gap_list[0] + gap_list[1] + gap_list[2] + (2 * self.thick_pal),
                     self.cant_lab)
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
            self.addFrontManual(gap_list[0] + (2 * self.thick_pal) - 4, self.width - 4)
        if (front_list[0] == 1) and (front_list[1] == 1):
            self.addFrontManual(gap_list[0] + (1.5 * self.thick_pal) - 3, self.width - 4)
        # gap_list[1]
        if (front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 0):
            self.addFrontManual(gap_list[1] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 0))
                or ((front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 1))):
            self.addFrontManual(gap_list[1] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 1):
            self.addFrontManual(gap_list[1] + self.thick_pal - 4, self.width - 4)

        # gap_list[2]
        if (front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 0):
            self.addFrontManual(gap_list[2] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 0))
                or ((front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 1))):
            self.addFrontManual(gap_list[2] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 1):
            self.addFrontManual(gap_list[2] + self.thick_pal - 4, self.width - 4)

        # gap4
        if (front_list[3] == 1) and (front_list[2] == 0):
            self.addFrontManual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3 * self.thick_pal) - 4,
                                self.width - 4)
        if (front_list[3] == 1) and (front_list[2] == 1):
            self.addFrontManual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3.5 * self.thick_pal) - 3,
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

    def getPFLOO(self):
        return self.pflOO

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
        
        :param type: "0.4" sau "2"
        :return: lungimea cantului selectat din tot corpul
        
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
                exportStl(filename,
                          self.material_list[i].label + str(i),
                          self.material_list[i].position[0],
                          self.material_list[i].position[1],
                          self.material_list[i].position[2],
                          self.material_list[i].position[3] + ox,
                          self.material_list[i].position[4] + oy,
                          self.material_list[i].position[5] + oz)

    # def drawCorp2(self, filename, ox, oy, oz):
    #     for i in range(len(self.arch)):
    #         exportStl(filename,
    #                   self.arch[i][0] + str(i),
    #                   self.arch[i][1],
    #                   self.arch[i][2],
    #                   self.arch[i][3],
    #                   self.arch[i][4] + ox,
    #                   self.arch[i][5] + oy,
    #                   self.arch[i][6] + oz)
'''

'''
class BaseBox(corp):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)
        picioare = math.ceil(self.width / 400) * 2
        self.append(accesoriu("picioare", picioare))
        self.append(accesoriu("clema plinta", picioare / 2))
        self.append(accesoriu("surub 3.5x16", picioare * 4))  # pentru picioare
        self.append(accesoriu("surub blat", 4))
        self.append(accesoriu("surub", 14))
        self.append(accesoriu("plinta", self.width / 1000))
        self.append(accesoriu("sipca apa", self.width / 1000))

        # arhitectura
        # jos
        jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, self.cant_lab, "", self.cant_lab,
                       self.cant_lab)
        self.append(jos)

        # lat rotit pe Y si ridicat pe z cu grosimea lui jos
        lat1 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth, self.thick_pal, self.cant_lab,
                        "", "", "")
        lat1.rotate("y")
        lat1.move("x", lat1.thick)
        lat1.move("z", jos.thick)
        self.append(lat1)

        # lat rotit pe y, translatat pe x cu (jos - grosime), translatat pe z cu grosime jos
        lat2 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth, self.thick_pal, self.cant_lab,
                        "", "", "")
        lat2.rotate("y")
        lat2.move("x", lat2.thick)
        lat2.move("x", jos.length - lat2.thick)
        lat2.move("z", jos.thick)
        self.append(lat2)

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg), si pe x cu grosime lat
        leg1 = PlacaPal(self.label + ".leg1", self.width - (2 * (self.thick_pal + self.cant)), 100, self.thick_pal,
                        self.cant_lab, self.cant_lab, "", "")
        leg1.move("z", lat1.length + jos.thick - leg1.thick)
        leg1.move("x", lat1.thick)
        self.append(leg1)

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg)
        #               pe y cu (latime lat - latime leg)
        #               pe x cu grosime lat
        leg2 = PlacaPal(self.label + ".leg2", self.width - (2 * (self.thick_pal + self.cant)), 100, self.thick_pal,
                        self.cant_lab, self.cant_lab, "", "")
        leg2.move("z", lat1.length + jos.thick - leg1.thick)
        leg2.move("y", lat1.width - leg2.width)
        leg2.move("x", lat1.thick)
        self.append(leg2)

        blatul = Blat(self.label + ".blat", self.width, self.width_blat, self.thick_blat)
        blatul.move("z", self.height)
        blatul.move("y", -rules["gap_fata"])
        self.append(blatul)

        self.addPFL()
class Raft(corp):
    def __init__(self, label, height, width, depth, shelves, rules):
        super().__init__(label, height, width, depth, rules)
        picioare = math.ceil(self.width / 400) * 2
        self.append(accesoriu("picioare", picioare))
        self.append(accesoriu("clema plinta", picioare / 2))
        self.append(accesoriu("surub 3.5x16", picioare * 4))  # pentru picioare
        self.append(accesoriu("surub blat", 4))
        self.append(accesoriu("surub", 14))
        self.append(accesoriu("plinta", self.width / 1000))

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

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("z", lat1.length)
        sus.move("x", lat1.thick)
        self.append(sus)

        self.addPFL()

        self.add_pol(shelves, 2)
class Bar(corp):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)
        self.append(accesoriu("surub", 14))

        # arhitectura
        lat1 = PlacaPal(self.label + ".lat1", self.height - self.thick_blat, self.depth - rules["gap_fata"],
                        self.thick_pal, self.cant_lab, self.cant_lab, self.cant_lab, "")
        lat1.rotate("y")
        lat1.move("x",self.thick_pal)
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat2", self.height - self.thick_blat, self.depth - rules["gap_fata"],
                        self.thick_pal, self.cant_lab, self.cant_lab, self.cant_lab, "")
        lat2.rotate("y")
        lat2.move("x", self.width)
        self.append(lat2)

        spate = PlacaPal(self.label + ".spate", self.height - self.thick_blat, self.width - 2 * self.thick_pal,
                         self.thick_pal, self.cant_lab, "", "", "")
        spate.rotate("x")
        spate.rotate("y")
        spate.rotate("y")
        spate.rotate("y")
        spate.move("z", self.height - self.thick_blat)
        spate.move("y", self.depth - rules["gap_fata"]) #- self.thick_pal
        spate.move("x", self.thick_pal)
        self.append(spate)

        bl = Blat(self.label + ".blat", self.width, self.depth, self.thick_blat)
        bl.move("z", self.height - self.thick_blat)
        bl.move("y", -rules["gap_fata"])
        self.append(bl)

class JollyBox(BaseBox):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)
        self.append(accesoriu("surub 3.5x16", 8))  # prentu glisiere
        self.append(accesoriu("surub 3.5x16", 8))  # pentru front
        if width < 150:
            raise NameError("ERROR: Cos Jolly pentru corpul ", self.label, "inexistent!")
        elif width < 200:
            self.append(accesoriu("Cos Jolly 150", 1))
        elif width < 250:
            self.append(accesoriu("Cos Jolly 200", 1))
        elif width < 300:
            self.append(accesoriu("Cos Jolly 250", 1))
        else:
            self.append(accesoriu("Cos Jolly 300", 1))

        self.addPFL()
        # self.addFront([[100, 100]], "door")
class TopBox(corp):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)

        self.sep_max_depth = self.depth - self.cant
        self.sep_prev = "h"
        self.append(accesoriu("surub", 8))
        self.append(accesoriu("pereche clema prindere perete", 1))
        self.append(accesoriu("sina perete", self.width / 1000))
        self.append(accesoriu("surub diblu perete", round(self.width / 201)))

        # arhitectura
        lat1 = PlacaPal(self.label + ".lat1", self.height, self.depth, self.thick_pal, self.cant_lab, "",
                        self.cant_lab, self.cant_lab)
        lat1.rotate("y")
        lat1.move("x",lat1.thick)
        self.append(lat1)
        # self.palOO.append(lat1)
        jos = PlacaPal(self.label + ".jos", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        jos.move("x", lat1.thick)
        self.append(jos)
        # self.palOO.append(jos)
        lat2 = PlacaPal(self.label + ".lat2", self.height, self.depth, self.thick_pal, self.cant_lab, "",
                        self.cant_lab, self.cant_lab)
        lat2.rotate("y")
        lat2.move("x", jos.length + 2 * lat2.thick)
        self.append(lat2)
        # self.palOO.append(lat2)
        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("z", lat1.length - sus.thick)
        sus.move("x", lat1.thick)
        self.append(sus)

        self.addPFL()
class SinkBox(BaseBox):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)
        self.remove_pfl()
        # for i in self.getPFLOO():
        #    if self.getPFLOO()[i].__getattribute__("label") == self.label + ".pfl":
        #        self.getPFLOO().pop()
        # self.getPFLOO().pop(self.getPFLOO()[0])
        leg_width = 100
        legatura = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), leg_width, self.thick_pal,
                            self.cant_lab, "", "", "")
        legatura.move("x", self.thick_pal)
        legatura.move("z", self.thick_pal)
        legatura.move("y", self.depth - self.thick_pal)
        legatura.rotate("x")
        legatura.move("y", legatura.thick)
        self.append(legatura)

        leg1 = self.get_item_by_type_label("pal", self.label + ".leg1")
        leg1.rotate("x")
        leg1.move("y", leg1.thick)
        leg1.move("z", self.thick_pal - leg1.width)

        leg2 = self.get_item_by_type_label("pal", self.label + ".leg2")
        leg2.rotate("x")
        leg2.move("y", leg2.thick)
        leg2.move("z", self.thick_pal - leg2.width)
        leg2.move("y", leg2.width - self.thick_pal)
class TowerBox(corp):
    def __init__(self, label, height, width, depth, rules, gap_list, gap_heat, front_list):
        """

        :param label:
        :param height:
        :param width:
        :param depth:
        :param rules:
        :param gap_list: intaltimea gap-urilor de jos in sus. Ultimul gap e cat ramane (ex:[gen_h_base - 2 * t1.pal_width,300, gen_h_tower - gen_h_base - 318 - gen_h_top])
        :param gap_heat: distanta in spate cat sunt mai in interior politele fata de lateriale ca sa permita evacuarea cladurii
        :param front_list: care gap-uri au front (ex. [0, 0, 0, 1])
        """
        super().__init__(label, height, width, depth, rules)
        self.depth = self.depth - gap_heat
        jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, self.cant_lab, "", self.cant_lab,
                       self.cant_lab)
        self.append(jos)

        lat1 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth + gap_heat, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat1.rotate("y")
        lat1.move("z", jos.thick)
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth + gap_heat, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat2.rotate("y")
        lat2.move("z", jos.thick)
        lat2.move("x", jos.length - lat2.thick)
        self.append(lat2)

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("x", lat1.thick)
        sus.move("z", lat1.length)
        self.append(sus)

        #adding horizontal separators
        offset = 0
        for gap in range(len(gap_list)):
            offset += gap_list[gap] + self.thick_pal
            self.addSepH(self.width - 2 * self.thick_pal, 0, offset, self.cant_lab)
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

        self.addPFL()

        # Se seteaza fronturile pentru turn
        # gap_list[0]
        if (front_list[0] == 1) and (front_list[1] == 0):
            self.addFrontManual(gap_list[0] + (2 * self.thick_pal) - 4, self.width - 4)
        if (front_list[0] == 1) and (front_list[1] == 1):
            self.addFrontManual(gap_list[0] + (1.5 * self.thick_pal) - 3, self.width - 4)
        # gap_list[1]
        if (front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 0):
            self.addFrontManual(gap_list[1] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 0))
                or ((front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 1))):
            self.addFrontManual(gap_list[1] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 1):
            self.addFrontManual(gap_list[1] + self.thick_pal - 4, self.width - 4)

        # gap_list[2]
        if (front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 0):
            self.addFrontManual(gap_list[2] + (2 * self.thick_pal) - 4, self.width - 4)
        if (((front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 0))
                or ((front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 1))):
            self.addFrontManual(gap_list[2] + (1.5 * self.thick_pal) - 3, self.width - 4)
        if (front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 1):
            self.addFrontManual(gap_list[2] + self.thick_pal - 4, self.width - 4)

        # gap4
        if (front_list[3] == 1) and (front_list[2] == 0):
            self.addFrontManual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3 * self.thick_pal) - 4,
                                self.width - 4)
        if (front_list[3] == 1) and (front_list[2] == 1):
            self.addFrontManual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3.5 * self.thick_pal) - 3,
                                self.width - 4)
class MsVBox(corp):
    def __init__(self, label, height, width, depth, rules):
        """

        :param label:
        :param height:
        :param width:
        :param depth:
        :param rules:

        """
        super().__init__(label, height, width, depth, rules)
        # self.addAcces("blat",self.width/1000)
        self.append(accesoriu("sipca apa", self.width / 1000))
        self.append(accesoriu("plinta", self.width / 1000))
        self.append(accesoriu("surub intre corpuri", 10))
        blatul = Blat(self.label + ".blat", self.width, self.width_blat, self.thick_blat)
        blatul.move("z", self.height)
        blatul.move("y", -rules["gap_fata"])
        self.append(blatul)
        self.add_front([[100, 100]], "door")
'''

class latura:
    def __init__(self, label):
        self.label = label
        self.corpuri = []

    def append(self, corp):
        self.length = self.length + corp.width
        self.corpuri.append(corp)

'''
class Comanda:
    def __init__(self, client, discount, req):

        self.req = req
        self.client = req["client"]
        self.discount = req["discount"]
        self.h_rate = req["h_rate"]
        self.corpuri = []
        self.length = 0
        self.pret_manop = 0
        self.acc = []
        self.m2pal = 0
        self.mat_pal = ""
        self.m2front = 0
        self.frezare = ""
        self.m2pfl = 0
        self.mat_pfl = ""
        self.m_blat = 0
        self.mat_blat = ""
        self.m_cant = [0, 0]
        self.price_pal = 1
        self.price_pfl = 1
        self.price_front = 1
        self.price_blat = 1
        self.price_cant = [0, 0]
        self.price_list = []
        self.cost_pal = 0
        self.cost_pfl = 0
        self.cost_front = 0
        self.cost_blat = 0
        self.cost_cant = [0, 0]
        self.cost_acc = 0
        self.mat_pal = req["material_pal"]
        self.mat_pfl = req["material_pfl"]
        self.mat_blat = req["material_blat"]
        self.mat_front = req["material_front"]


    def append(self, corp):

        self.length = self.length + corp.width
        self.corpuri.append(corp)

    # def addAcces(self, name, buc):
    #     found = False
    #     for i in range(len(self.acc)):
    #         acc_current = self.acc[i]
    #         if (name == acc_current[2]):
    #             acc_current[3] = acc_current[3] + buc
    #             found = True
    #             index_of_acc = -1
    #             for row in self.price_list:
    #                 if acc_current in row:
    #                     index_of_acc = self.price_list.index(row)
    #             acc_current[4] = acc_current[4] + (float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]))
    #     if not found:
    #         self.acc = self.acc + [["accesoriu", "total", name, buc, 0]]

    # for i in range(len(self.acc)):
    #    acc_to_find = self.acc[i][2]
    #    index_of_acc = -1
    #    for row in self.price_list:
    #        if acc_to_find in row:
    #            index_of_acc = self.price_list.index(row)
    #    self.cost_acc = self.cost_acc + (float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]))

    # def setPrice(self, item, price):
    #     if item == "pal":
    #         self.price_pal = price
    #     elif item == "pfl":
    #         self.price_pfl = price
    #     elif item == "front":
    #         self.price_front = price
    #     else:
    #         self.priceList.append(item, price)

    def get_price_for_item(self, type, material):
        with open('elements/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == type and row["Material"] == material:
                    found = True
                    return row["Price"]
            if not found:
                raise NameError("ERROR: Price for " + type + ":" + material + " not found. Setting to 0 RON.")

    def get_min_qty_for_item(self, type, material):
        with open('elements/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == type and row["Material"] == material:
                    found = True
                    return row["Minimum"]
            if not found:
                raise NameError("ERROR: Minimum quantity for " + type + " : " + material + " not found. "
                                                                                           "Considering 1 unit")
                return 1

    def create_folder(self):
        # create folder with customer name if it doesn't exist
        folder_name = "Comanda " + self.client
        isExist = os.path.exists(folder_name)

        if not isExist:
            os.mkdir(folder_name)


    def export_pal_for_proficut(self):
        self.create_folder()
        folder_name = "Comanda " + self.client
        shutil.copyfile("templates/Cote-Proficut-2018.xlsx", "Comanda " + self.client + "/Comanda_Proficut_"+self.client+".xlsx")

        file = openpyxl.load_workbook("Comanda " + self.client + "/Comanda_Proficut_"+self.client+".xlsx")
        sheet = file.get_sheet_by_name("Sheet1")

        sheet['C1'] = self.req["Client Proficut"]
        sheet['D2'] = self.req["Tel Proficut"]
        sheet['D3'] = self.req["Transport"]
        sheet['C4'] = self.req["Adresa"]
        sheet['G4'] = self.req["material_pal"]


        counter = 0
        for corp in self.corpuri:
            for element in corp.material_list:
                if element.type == "pal":
                    sheet['A' + str(10 + counter)] = "1"
                    sheet['B' + str(10 + counter)] = element.length
                    sheet['C' + str(10 + counter)] = element.width
                    sheet['D' + str(10 + counter)] = 0
                    sheet['E' + str(10 + counter)] = element.label
                    sheet['F' + str(10 + counter)] = element.cant_list[0]
                    sheet['G' + str(10 + counter)] = element.cant_list[1]
                    sheet['H' + str(10 + counter)] = element.cant_list[2]
                    sheet['I' + str(10 + counter)] = element.cant_list[3]
                    counter += 1
        file.save("Comanda " + self.client + "/Comanda_Proficut_"+self.client+".xlsx")

    def export_csv(self):
        # create folder with customer name if it doesn't exist
        folder_name = "Comanda " + self.client
        isExist = os.path.exists(folder_name)

        if not isExist:
            os.mkdir(folder_name)

        # output comanda pal
        name = os.path.join(folder_name, "comanda_pal_" + self.client + ".csv")
        corpuri = self.corpuri

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Orientabila", "Eticheta", "L1", "L2", "l1", "l2"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pal":
                        comanda_writer.writerow(
                            [1, element.length, element.width, 0, element.label, element.cant_list[0],
                             element.cant_list[1], element.cant_list[2], element.cant_list[3]])

        # output comanda pfl
        name = os.path.join(folder_name, "comanda_pfl_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Eticheta"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pfl":
                        comanda_writer.writerow([1, element.length, element.width, element.label])

        # output comanda fronturi
        name = os.path.join(folder_name, "comanda_front_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Eticheta", "Lungime", "Latime", "Pret"])
            comanda_writer.writerow([self.__getattribute__("frezare")])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "front":
                        comanda_writer.writerow([element.label, element.length, element.width, element.price])

        # output comanda accesorii
        name = os.path.join(folder_name, "comanda_accesorii_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Nume", "Bucati", "Pret/buc", "Pret total"])
            # pe corpuri

            totals = []  # totals is a list containing total accessories and their amount and price

            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "accesoriu":
                        comanda_writer.writerow(
                            [element.name, element.pieces, element.price, element.pieces * element.price])
                        found_in_totals = False
                        for i in range(len(totals)):
                            if totals[i][0] == element.name:
                                totals[i][1] += element.pieces
                                found_in_totals = True
                        if not found_in_totals:
                            totals.append([element.name, element.pieces, element.price])

            # total
            for i in range(len(totals)):
                # print(totals2[i][0], totals2[i][1], totals2[i][2], totals2[i][1] * totals2[i][2])
                comanda_writer.writerow(["TOTAL " + totals[i][0], totals[i][1], totals[i][2], totals[i][1] *
                                         totals[i][2]])

        # output pentru optimizare pal
        name = os.path.join(folder_name, "PannelsCuttingList_pal_" + self.client + ".csv")
        mobila = self.corpuri
        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Length", "Width", "Qty", "Label", "Enabled"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pal":
                        comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])

        # pentru optimizare PFL
        name = os.path.join(folder_name, "PannelsCuttingList_pfl_" + self.client + ".csv")
        mobila = self.corpuri
        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Length", "Width", "Qty", "Enabled"])
            # pe corpuri
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pfl":
                        comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])

    def get_m2_pal(self):
        m2pal = 0
        for i in range(len(self.corpuri)):
            m2pal = m2pal + self.corpuri[i].get_m2_pal()
        return m2pal

    def get_m2_pfl(self):
        m2pfl = 0
        for i in range(len(self.corpuri)):
            m2pfl = m2pfl + self.corpuri[i].get_m2_pfl()
        return m2pfl

    def get_m2_front(self):
        m2 = 0
        for i in range(len(self.corpuri)):
            m2 = m2 + self.corpuri[i].get_m2_front()
        return m2

    def get_m_cant(self, type):
        
         :param type: "0.4" sau "2"
         :return: lungimea cantului selectat din toata comanda
         

        m = 0
        for i in range(len(self.corpuri)):
            m = m + self.corpuri[i].get_m_cant(type)
        return m

    def get_m_blat(self):
        

        :return: metri de blat din comanda
        

        m = 0
        for i in range(len(self.corpuri)):
            for j in range(len(self.corpuri[i].material_list)):
                if self.corpuri[i].material_list[j].type == "blat":
                    m = m + self.corpuri[i].material_list[j].length / 1000
        return m

    def draw(self, ox, oy, oz):
        folder_name = "Comanda " + self.client
        isExist = os.path.exists(folder_name)

        if not isExist:
            os.mkdir(folder_name)

        name = os.path.join(folder_name, "3D " + self.client)

        ofset = 0
        for i in range(len(self.corpuri)):
            self.corpuri[i].drawCorp(name, ox + ofset, oy, oz)
            ofset = ofset + self.corpuri[i].width + 1

    def get_cost_manopera(self):
        
        - 8h proictare
        - 2h per corp asamblare, pozitionare si montaj fronturi
        - 2h montaj / electrocasnic
        - 0.5h pe metru de blat, montaj blat
        :return: [pret manopera, pret manopera cu discount]


        discount = self.req["discount"]
        h_rate = self.req["h_rate"]
        electrocasnice = self.req["nr_electrocasnice"]
        pret_manop = math.ceil((8 + (len(self.corpuri) * 2) + electrocasnice * 2 + self.get_m_blat() * 0.5)) * h_rate
        pret_manop_discount = pret_manop * (100 - discount) / 100
        return [pret_manop, pret_manop_discount]

    def get_sheets_pal(self):
        m2_pal = self.get_m2_pal() * (1 + PAL_LOSS)
        min = float(self.get_min_qty_for_item("pal", self.req["material_pal"])) * (2800 * 2070 / 1000000)
        sheets = math.ceil(m2_pal / (2800 * 2070 / 1000000))
        if m2_pal < min:
            return min
        else:
            return sheets

    def get_cost_pal(self):
        pal_price = float(self.get_price_for_item("pal", self.mat_pal))
        return self.get_sheets_pal() * pal_price

    def print_status(self):

        cant_price_04 = float(self.get_price_for_item("cant", "0.4"))
        cant_price_2 = float(self.get_price_for_item("cant", "2"))
        pfl_price = float(self.get_price_for_item("pfl", self.mat_pfl))
        front_price = float(self.get_price_for_item("front", self.mat_front))
        blat_price = float(self.get_price_for_item("blat", self.mat_blat))
        for i in range(len(self.corpuri)):
            for j in range(len(self.corpuri[i].material_list)):
                if self.corpuri[i].material_list[j].type == "accesoriu":
                    acc_price = float(self.get_price_for_item(self.corpuri[i].material_list[j].type,
                                                              self.corpuri[i].material_list[j].name))
                    self.cost_acc += acc_price * self.corpuri[i].material_list[j].pieces

        print("*** INFORMATII GENERALE ***")
        print("Numar de corpuri: ", len(self.corpuri))
        print("Lungime totala mobila: ", self.length / 1000, " m")
        print("M2 PAL: ", "{:.2f}".format(self.get_m2_pal()),
              " | Nr. coli PAL: ", self.get_sheets_pal(),
              " | Cost pal:", self.get_cost_pal(),
              " | Material:", self.mat_pal)
        print("M Cant 0.4", math.ceil(self.get_m_cant("0.4")),
              " | Pret ", "{:.2f}".format(math.ceil(self.get_m_cant("0.4")) * cant_price_04))
        print("M Cant 2", math.ceil(self.get_m_cant("2")),
              " | Pret ", "{:.2f}".format(math.ceil(self.get_m_cant("2")) * cant_price_2))

        print("M2 PFL: ", "{:.2f}".format(self.get_m2_pfl()),
              " | Nr. coli PFL: ", math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)),
              " | Pret PFL: ", math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)) * pfl_price)

        print("M2 Front: ", "{:.2f}".format(self.get_m2_front()),
              " | Pret ", "{:.2f}".format(self.get_m2_front() * front_price),
              " | Material: ", "NETT FRONT" , self.mat_front)

        print("M Blat: ", "{:.2f}".format(self.get_m_blat()),
              " | Pret", self.get_m_blat() * blat_price)

        print("Cost total accesorii: ", round(self.cost_acc))

        if self.req["discount"] == 0:
            print("Pret manopera:", self.get_cost_manopera()[0])
        else:
            print("Pret manopera:", self.get_cost_manopera()[0],
                  "| Discount[%]:", self.req["discount"],
                  "| Pret manopera cu discount:", self.get_cost_manopera()[1])

        print("Cost TOTAL: ", round(int(self.cost_acc) +
                                    int(self.get_cost_manopera()[1]) +
                                    int(self.get_cost_pal()) +
                                    int(math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)) * pfl_price) +
                                    int(self.get_m2_front() * int(front_price)) +
                                    int(self.get_m_blat() * blat_price) +
                                    int(math.ceil(self.get_m_cant("0.4")) * cant_price_04) +
                                    int(math.ceil(self.get_m_cant("2")) * cant_price_2)))
'''