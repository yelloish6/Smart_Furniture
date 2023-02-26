from elements.corp import *


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

        self.add_pfl()

class BaseCorner(corp):
    def __init__(self, label, height, width, depth, rules, cut_width, cut_depth, l_r, with_polita):
        """
        o---------width----------|   o------width-----------
        |                        |   |                     |
        |     l_r="left"         |   |    l_r="right"      |
        |                        |   |                     |
        depth                    |   |                     depth
        |        ----cut_width----   --- cut_width--       |
        |        |                                 |       |
        |        cut_depth                  cut_depth      |
        |        |                                 |       |
        ----------                                 ---------

        include PFL si fronturi
        :param label:
        :param height:
        :param width:
        :param depth:
        :param rules:
        :param cut_width:
        :param cut_depth:
        :param l_r:
        :param with_polita:
        :return:
        """

        # depth = depth - rules["gap_spate"]
        # width = width - rules["gap_spate"]
        # cut_depth = cut_depth + rules["gap_fata"]
        # cut_width = cut_width + rules["gap_fata"]

        super().__init__(label, height, width, depth, rules)

        if l_r == "left":
            jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, "", "", "", "")
            jos.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width) + ":" + str(self.depth - cut_depth) + ":" + str(cut_width) + "(cant " + str(
                self.cant_lab) + "):" + str(cut_depth) +
                        "(cant " + str(self.cant_lab) + "):" + str(self.width - cut_width) + ":" + str(self.depth))
            # jos.move("y", - depth)
            self.append(jos)

            lat1 = PlacaPal(self.label + ".lat1", self.height - self.thick_pal, self.depth - cut_depth, self.thick_pal,
                            self.cant_lab, "", "", "")
            lat1.rotate("x")
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("z", self.thick_pal)
            lat1.move("x", jos.length)
            lat1.move("y", cut_depth)
            self.append(lat1)

            lat2 = PlacaPal(self.label + ".lat2", self.height - self.thick_pal, self.width - cut_width, self.thick_pal,
                            self.cant_lab, "", "", "")
            lat2.rotate("x")
            lat2.rotate("y")
            #lat2.rotate("z")
            lat2.move("x", lat2.width)
            lat2.move("z", self.thick_pal)
            lat2.move("y", self.thick_pal)
            self.append(lat2)

            spate = PlacaPal(self.label + ".spate", self.depth - self.thick_pal, self.height - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            # spate.rotate("x")
            # spate.move("z", self.thick_pal)
            # spate.move("y", depth)
            # spate.move("x", self.thick_pal)
            spate.rotate("x")
            spate.rotate("z")
            spate.move("z", self.thick_pal)
            spate.move("y", self.thick_pal + spate.length)
            spate.move("x", self.thick_pal)
            self.append(spate)

            leg1 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "", "", "")
            leg1.rotate("x")
            leg1.rotate("x")
            leg1.rotate("x")
            leg1.move("z", self.height)
            leg1.move("x", self.thick_pal)
            leg1.move("y", cut_depth)
            self.append(leg1)

            leg2 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "", "", "")
            leg2.rotate("x")
            leg2.move("z", self.height - leg2.width)
            leg2.move("y", self.depth)
            leg2.move("x", self.thick_pal)
            self.append(leg2)

            leg3 = PlacaPal(self.label + ".leg", cut_depth - self.thick_pal, 100, self.thick_pal, self.cant_lab, "",
                            "",
                            "")
            leg3.rotate("x")
            leg3.rotate("z")
            leg3.rotate("z")
            leg3.rotate("z")
            leg3.move("z", self.height - leg3.width)
            leg3.move("x", self.width - cut_width - self.thick_pal)
            leg3.move("y", self.thick_pal)
            #leg3.move("y", jos.length)
            self.append(leg3)

            if with_polita:
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

                pol.move("x", self.thick_pal)
                pol.move("y", self.thick_pal)
                pol.move("z", int((self.height - self.thick_pal) / 2))
                #pol.move("y", -cut_depth)
                self.append(pol)

            front1 = Front(self.label + "_1", self.height - 2 * rules["gap_front"], cut_depth - 3 - rules["thick_front"], rules["thick_front"])
            front1.rotate("y")
            front1.move("x", width - cut_width + rules["thick_front"])
            front1.move("z", rules["gap_front"])
            front1.move("y", rules["gap_front"])
            self.append(front1)

            front2 = Front(self.label + "_2", self.height - 2 * rules["gap_front"], cut_width - 3 - rules["thick_front"], rules["thick_front"])
            front2.rotate("y")
            front2.rotate("z")
            front2.move("x", width - cut_width + rules["thick_front"])
            front2.move("y", cut_depth - rules["thick_front"])
            front2.move("z", rules["gap_front"])
            self.append(front2)

            # blat2 = Blat(self.label + ".blat2", cut_depth - rules["gap_fata"], rules["width_blat"], rules["thick_blat"])
            # blat2.move("z", self.height + 10)
            # blat2.move("y", cut_depth - rules["gap_fata"])
            # blat2.move("x", - rules["gap_spate"])
            # blat2.rotate("z")
            # self.append(blat2)

        elif l_r == "right":
            jos = PlacaPal(self.label + ".jos", self.width, self.depth, self.thick_pal, "", "", "", "")
            jos.add_obs(
                str("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                    str(self.width) + ":" + str(self.depth) + ":" + str(self.width - cut_width) + ":" + str(
                    cut_depth) + "(cant " + str(self.cant_lab) + "):" +
                    str(cut_width) + "(cant " + str(self.cant_lab) + "):" + str(self.depth - cut_depth)))
            #jos.move("y", -cut_depth)
            self.append(jos)

            lat1 = PlacaPal(self.label + ".lat1", self.height - self.thick_pal, self.depth - cut_depth, self.thick_pal,
                            self.cant_lab, "", "", "")
            lat1.rotate("x")
            lat1.rotate("y")
            lat1.rotate("z")
            lat1.move("z", self.thick_pal)
            lat1.move("x", self.thick_pal)
            lat1.move("y", cut_depth)
            self.append(lat1)

            lat2 = PlacaPal(self.label + ".lat2", self.height - self.thick_pal, self.width - cut_width, self.thick_pal,
                            self.cant_lab, "", "", "")
            lat2.rotate("x")
            lat2.rotate("y")
            lat2.move("z", self.thick_pal)
            lat2.move("x", self.width)
            lat2.move("y", self.thick_pal)
            self.append(lat2)

            spate = PlacaPal(self.label + ".spate", self.depth - self.thick_pal, self.height - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            spate.rotate("x")
            spate.rotate("z")
            spate.move("z", self.thick_pal)
            spate.move("y", self.depth)
            #spate.move("y", -cut_depth)
            spate.move("x", self.width)
            self.append(spate)

            leg1 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "", "", "")
            leg1.move("z", self.height - self.thick_pal)
            leg1.move("x", self.thick_pal)
            leg1.move("y", self.depth - leg1.width)
            #leg1.move("y", -cut_depth)
            self.append(leg1)

            leg2 = PlacaPal(self.label + ".leg", self.width - (2 * self.thick_pal), 100, self.thick_pal, self.cant_lab,
                            "",
                            "", "")
            leg2.rotate("x")
            leg2.move("z", self.height - leg2.width)
            leg2.move("y", cut_depth)
            leg2.move("x", self.thick_pal)
            leg2.move("y", self.thick_pal)
            self.append(leg2)

            leg3 = PlacaPal(self.label + ".leg", cut_depth - self.thick_pal, 100, self.thick_pal, self.cant_lab, "",
                            "", "")
            leg3.rotate("x")
            leg3.rotate("z")
            leg3.move("z", self.height - leg3.width)
            leg3.move("x", cut_width)
            leg3.move("x", self.thick_pal)
            leg3.move("y", cut_depth)
            self.append(leg3)

            if with_polita:
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

                pol.move("x", self.thick_pal)
                pol.move("y", self.thick_pal)
                pol.move("z", int((self.height - self.thick_pal) / 2))
                #pol.move("y", -cut_depth)
                self.append(pol)

            front1 = Front(self.label + "_1", self.height - 2 * rules["gap_front"], cut_depth - 3 -
                           rules["thick_front"], rules["thick_front"])
            front1.rotate("y")
            front1.move("x", cut_width)
            front1.move("z", rules["gap_front"])
            front1.move("y", rules["gap_front"])
            self.append(front1)

            front2 = Front(self.label + "_2", self.height - 2 * rules["gap_front"], cut_width - 3 -
                           rules["thick_front"], rules["thick_front"])
            front2.rotate("y")
            front2.rotate("z")
            front2.move("x", rules["gap_front"])
            front2.move("y", cut_depth - rules["thick_front"])
            front2.move("z", rules["gap_front"])
            self.append(front2)

            # blat2 = Blat(self.label + ".blat2", cut_depth, rules["width_blat"], rules["thick_blat"])
            # blat2.move("z", self.height)
            # blat2.move("x", cut_width)
            # blat2.move("y", cut_depth)
            # blat2.rotate("z")
            # self.append(blat2)

        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.add_pfl()
#        self.get_item_by_type_label("pfl", self.label + ".pfl").move("y", - cut_depth)
        #self.getPFLOO()[0].getPlacaOO()

        self.append(accesoriu("balama usa franta", 2))
        self.append(accesoriu("balama 170 deg", 2))
        self.append(accesoriu("surub 3.5x16", 4 * 4))  # pentru balamale
        self.append(accesoriu("picioare", 6))
        self.append(accesoriu("clema plinta", 3))
        self.append(accesoriu("surub 3.5x16", 3 * 4))  # pentru picioare
        self.append(accesoriu("surub blat", 4))
        self.append(accesoriu("L", 2))
        self.append(accesoriu("surub", 19))
        self.append(accesoriu("plinta", (cut_width + cut_depth) / 1000))
        self.append(accesoriu("sipca apa", (self.width + self.depth) / 1000))

        # blat1 = Blat(self.label + ".blat1", self.width + rules["gap_spate"], rules["width_blat"], rules["thick_blat"])
        # blat1.move("z", self.height)
        # blat1.move("y", cut_depth - rules["gap_fata"])
        # blat1.move("x", - rules["gap_spate"])
        # blat1.move("z", 10)
        # self.append(blat1)


class TopCorner(corp):
    def __init__(self, label, height, width, depth, rules, cut_width, cut_depth, l_r, with_polita):
        """
        o---------width----------|   o------width-----------
       |                        |   |                     |
       |     l_r="left"         |   |    l_r="right"      |
       |                        |   |                     |
       depth                    |   |                     depth
       |        ----cut_width----   --- cut_width--       |
       |        |                                 |       |
       |        cut_depth                  cut_depth      |
       |        |                                 |       |
       ----------                                 ---------
        include PFL si fronturi
        :param label:
        :param height:
        :param width:
        :param depth:
        :param rules:
        :param cut_width:
        :param cut_depth:
        :param l_r:
        :param with_polita:
        """
        super().__init__(label, height, width, depth, rules)
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
            jos.move("y", self.thick_pal)
            jos.move("x", self.thick_pal)
            #jos.move("y", -cut_depth)
            self.append(jos)
            
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
            sus.move("y", self.thick_pal)
            sus.move("x", self.thick_pal)
            sus.move("z", self.height - self.thick_pal)
            #sus.move("y", -cut_depth)
            self.append(sus)
            
            pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal), self.depth - (1 * self.thick_pal),
                           self.thick_pal, "", "", "", "")

            pol.add_obs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - (2 * self.thick_pal)) + ":" +
                        str(self.depth - cut_depth - 20) + ":" +
                        str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.width - cut_width - self.thick_pal - 20) + ":" +
                        str(self.depth - self.thick_pal))
            pol.move("x", self.thick_pal)
            pol.move("y", self.thick_pal)
            pol.move("z", int((self.height - self.thick_pal) / 2))
            #pol.move("y", -cut_depth)
            self.append(pol)
            
            spate = PlacaPal(self.label + ".spate", self.height, self.depth - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            spate.rotate("y")
            spate.move("y", self.thick_pal)
            spate.move("x", self.thick_pal)
            #spate.move("y", -cut_depth)
            self.append(spate)
            
            lat1 = PlacaPal(self.label + ".lat1", self.height, self.width - cut_width, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            lat1.rotate("y")
            lat1.rotate("z")
            #lat1.move("y", -cut_depth)
            self.append(lat1)

            lat2 = PlacaPal(self.label + ".lat2", self.height, self.depth - cut_depth, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            lat2.rotate("y")
            lat2.move("x", self.width)
            lat2.move("y", self.depth - lat2.width)
            #lat2.move("y", -cut_depth)
            self.append(lat2)
            
            front1 = Front(self.label + "_1", self.height - 2 * rules["gap_front"], cut_depth - 3 - rules["thick_front"], rules["thick_front"])
            front1.rotate("y")
            front1.move("x", width - cut_width + rules["thick_front"])
            front1.move("z", rules["gap_front"])
            front1.move("y", rules["gap_front"])
            self.append(front1)

            front2 = Front(self.label + "_2", self.height - 2 * rules["gap_front"], cut_width - 3 - rules["thick_front"], rules["thick_front"])
            front2.rotate("y")
            front2.rotate("z")
            front2.move("x", width - cut_width + rules["thick_front"])
            front2.move("y", cut_depth - rules["thick_front"])
            front2.move("z", rules["gap_front"])
            self.append(front2)
            
            # self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            # self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]


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
            jos.move("y", self.thick_pal)
            #jos.move("y", -cut_depth)
            jos.move("x", self.thick_pal)
            self.append(jos)
            
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

            sus.move("y", self.thick_pal)
            sus.move("z", self.height - self.thick_pal)
            #sus.move("y", -cut_depth)
            sus.move("x", self.thick_pal)
            self.append(sus)
            
            pol = PlacaPal(self.label + ".pol", self.width - (2 * self.thick_pal), self.depth - (1 * self.thick_pal),
                           self.thick_pal, "", "", "", "")
            pol.add_obs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                        str(self.width - (2 * self.thick_pal)) + ":" +
                        str(self.depth - self.thick_pal) + ":" +
                        str(self.width - cut_width - self.thick_pal - 20) + ":" +
                        str(cut_depth - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(cut_width - self.thick_pal + 20) + "(cant " + str(self.cant_lab) + "):" +
                        str(self.depth - cut_depth - 20) + ":")
            pol.move("x", self.thick_pal)
            pol.move("y", self.thick_pal)
            pol.move("z", int((self.height - self.thick_pal) / 2))
            #pol.move("y", -cut_depth)
            self.append(pol)

            spate = PlacaPal(self.label + ".spate", self.height, self.depth - self.thick_pal,
                             self.thick_pal, "", "", "", "")
            spate.rotate("y")
            spate.move("y", self.thick_pal)
            spate.move("x", self.width)
            # spate.move("z", self.thick_pal)
            #spate.move("y", -cut_depth)
            self.append(spate)
            
            lat1 = PlacaPal(self.label + ".lat1", self.height, self.width - cut_width, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            lat1.rotate("y")
            lat1.rotate("z")
            #lat1.move("y", -cut_depth)
            lat1.move("x", cut_width)
            self.append(lat1)

            lat2 = PlacaPal(self.label + ".lat2", self.height, self.depth - cut_depth, self.thick_pal, self.cant_lab,
                            "",
                            self.cant_lab, self.cant_lab)
            lat2.rotate("y")
            lat2.move("x", self.thick_pal)
            lat2.move("y", self.depth - lat2.width)
            # lat2.move("y", -cut_depth)
            self.append(lat2)
            
            front1 = Front(self.label + "_1", self.height - 2 * rules["gap_front"], cut_depth - 3 - rules["thick_front"], rules["thick_front"])
            front1.rotate("y")
            front1.move("x", cut_width)
            front1.move("z", rules["gap_front"])
            front1.move("y", rules["gap_front"])
            self.append(front1)

            front2 = Front(self.label + "_2", self.height - 2 * rules["gap_front"], cut_width - 3 - rules["thick_front"], rules["thick_front"])
            front2.rotate("y")
            front2.rotate("z")
            front2.move("x", rules["gap_front"])
            front2.move("y", cut_depth - rules["thick_front"])
            front2.move("z", rules["gap_front"])
            self.append(front2)

            # self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
            # self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]


        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.add_pfl()

        self.append(accesoriu("balama usa franta", 2))
        self.append(accesoriu("balama 170 deg", 2))
        self.append(accesoriu("surub 3.5x16", 4 * 4)) # pentru balamale
        self.append(accesoriu("surub", 20))
        self.append(accesoriu("pereche clema prindere perete", 1))
        self.append(accesoriu("sina perete", self.width / 1000))
        self.append(accesoriu("surub diblu perete", round(self.width / 201)))


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

        self.add_pfl()

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

        self.add_pfl()
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

        self.add_pfl()


class SinkBox(BaseBox):
    def __init__(self, label, height, width, depth, rules):
        super().__init__(label, height, width, depth, rules)
        self.remove_all_pfl()
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
        lat1.move("x", self.thick_pal)
        self.append(lat1)

        lat2 = PlacaPal(self.label + ".lat", self.height - self.thick_pal, self.depth + gap_heat, self.thick_pal,
                        self.cant_lab, "", self.cant_lab, "")
        lat2.rotate("y")
        lat2.move("z", jos.thick)
        lat2.move("x", jos.length)
        self.append(lat2)

        sus = PlacaPal(self.label + ".sus", self.width - (2 * self.thick_pal), self.depth - (self.cant),
                       self.thick_pal, self.cant_lab, "", "", "")
        sus.move("x", lat1.thick)
        sus.move("z", lat1.length)
        self.append(sus)

        #adding horizontal separators
        offset = 0
        for gap in range(len(gap_list)):
            offset += gap_list[gap] # + self.thick_pal
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

        # if front_list[0] == 1:
        #     if front_list[1] == 0:
        #         self.add_front_manual(gap_list[0] + (2 * self.thick_pal) - 4, self.width - 4, 0, 0)
        #         if front_list[2] == 0:
        #
        #         elif front_list[2] == 1:
        #     elif front_list[1] == 1:
        #         self.add_front_manual(gap_list[0] + (1.5 * self.thick_pal) - 3, self.width - 4, 0, 0)

        # Se seteaza fronturile pentru turn
        # gap_list[0]
        if (front_list[0] == 1) and (front_list[1] == 0):
            # front jos fara ala de sus
            self.add_front_manual(gap_list[0] + (2 * self.thick_pal) - 4, self.width - 4, 0, 0)
        if (front_list[0] == 1) and (front_list[1] == 1):
            # front jos si ala de sus
            self.add_front_manual(gap_list[0] + (1.5 * self.thick_pal) - 3, self.width - 4, 0, 0)
        # gap_list[1]
        if (front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 0):
            self.add_front_manual(gap_list[1] + (2 * self.thick_pal) - 4, self.width - 4, 0, gap_list[0])
        if (((front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 0))
                or ((front_list[1] == 1) and (front_list[0] == 0) and (front_list[2] == 1))):
            self.add_front_manual(gap_list[1] + (1.5 * self.thick_pal) - 3, self.width - 4, 0, gap_list[0] + (self.thick_pal / 2))
        if (front_list[1] == 1) and (front_list[0] == 1) and (front_list[2] == 1):
            self.add_front_manual(gap_list[1] + self.thick_pal - 4, self.width - 4, 0, gap_list[0] + (self.thick_pal / 2))

        # gap_list[2]
        if (front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 0):
            self.add_front_manual(gap_list[2] + (2 * self.thick_pal) - 4, self.width - 4, 0, gap_list[0] + gap_list[1] + 2)
        if (((front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 0))
                or ((front_list[2] == 1) and (front_list[1] == 0) and (front_list[3] == 1))):
            self.add_front_manual(gap_list[2] + (1.5 * self.thick_pal) - 3, self.width - 4, 0, gap_list[0] + gap_list[1] + 2)
        if (front_list[2] == 1) and (front_list[1] == 1) and (front_list[3] == 1):
            self.add_front_manual(gap_list[2] + self.thick_pal - 4, self.width - 4, 0, gap_list[0] + gap_list[1] + 2)

        # gap4
        if (front_list[3] == 1) and (front_list[2] == 0):
            self.add_front_manual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3 * self.thick_pal) - 4,
                                  self.width - 4, 0, gap_list[0] + gap_list[1] + gap_list[2] + 4)
        if (front_list[3] == 1) and (front_list[2] == 1):
            self.add_front_manual(self.height - gap_list[0] - gap_list[1] - gap_list[2] - (3.5 * self.thick_pal) - 3,
                                  self.width - 4, 0, gap_list[0] + gap_list[1] + gap_list[2] + 4)


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

