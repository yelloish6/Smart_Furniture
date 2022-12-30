
from elements.comanda import *
from architectures.kitchen import *
from architectures.dressing import *

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 100,
    "general_width": 600,
    "width_blat": 600,
    "gap_spate": 50,
    "gap_fata": 50,
    "gap_front": 2,
    "cant_general": 1,
    "cant_pol": 2,
    "cant_separator": 1,
}

req = {
    "client": "Test",
    "Client Proficut": 'Bogdan Urs',  # nume client Proficut
    "Tel Proficut": '0740472185',  # numar telefon
    "Transport": 'Da',  # transport (Da/Nu)
    "Adresa": 'Mosnita Veche, str. Borsa, Nr. 38',
    "h_bucatarie": 2070,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 600,  # adancime blat jos
    "top_height": 600,
    "top_height_2": 400,
    "top_depth": 600,
    "top_depth_2": 500,
    "blat_height": 880,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "W962ST2",
    "material_front": "A34/R3",
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "Alb",
    "h_rate": 120,
    "discount": 100,
    "nr_electrocasnice": 6
}

mobila = Comanda("Noi", req["discount"], req)

base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
base_width = 600
base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]

top_height = req["h_bucatarie"] - req["h_faianta_top"] + 5
top_width = 600
top_depth = 300

tower_height = req["h_bucatarie"] - rules["height_legs"]
tower_width = 600
tower_depth = req["depth_base"] - rules["gap_fata"]

# picioare = 100
# top_height = 600
# gen_w = 600
# top_depth = 300
# gap_spate = 50
# gap_fata = 50
# gen_cant = 0.4
# "2" = 2
# gen_cant_sep = 0.4
# gen_gap_front = 2
# th_pal = 18




# 500, 150, 1000, 150, 500
# ms1 = TopBox("MS1", top_height, 500, top_depth, rules)
# ms1.add_pol(1, rules["cant_pol"])
# ms1.add_front([[100, 100]], "door")
# mobila.append(ms1)
#
# ms_colt = BaseCorner("MS_colt", base_height, 900, 800, rules, 400, 400, "left", True)
# ms_colt.move("y", -400)
# mobila.append(ms_colt)

# ms_colt = TopCorner("MS_colt", top_height, top_width, 500, rules, top_width-top_depth, 500 - top_depth, "right", True)
# ms_colt.move("y", -500 + top_depth)
# mobila.append(ms_colt)

# ms_tower = TowerBox("Tower", 1000, 600, 600, rules, [base_height, 100, 100], 50, [1, 0, 1, 0])
# mobila.append(ms_tower)

# ms2 = TopBox("MS2", top_height, 150, top_depth, rules)
# ms2.add_pol(3, "2")
# ms2.add_front([[100,100]], "door")
# ms2.rotate("z")
# # ms2.rotate("z")
# # ms2.rotate("z")
# ms2.move("x", -top_depth)
# ms2.move("y", - 500 + top_depth)
# mobila.append(ms2)
#
# ms3 = TopBox("MS3", top_height, 1000, top_depth, rules)
# ms3.add_pol(1, "2")
# ms3.add_front([[100,50],[100,50]], "door")
# mobila.append(ms3)
#
# ms4 = TopBox("MS4", top_height, 150, top_depth, rules)
# ms4.add_pol(3, "2")
# ms4.add_front([[100,100]], "door")
# mobila.append(ms4)
#
# ms5 = TopBox("MS5", top_height, 500, top_depth, rules)
# ms5.add_pol(1, "2")
# ms5.add_front([[100,100]], "door")
# mobila.append(ms5)

banca1 = Banca("banca", 518, 800, 500, rules)
mobila.append(banca1)

et1 = Etajera("etajera1", 1554, 404, 400, 7, rules)
et1.add_front([[100, 100]], "door")
et1.move("z", banca1.height + 1)
et1.move("x", - et1.width)
et1.move("y", 100)
mobila.append(et1)

et2 = Etajera("etajera2", 1500, 482, 400, 3, rules)
et2.rotate("y")
et2.move("z", banca1.height + et1.height + 1)
et2.move("x", - et1.width)
et2.move("y", 100)
mobila.append(et2)

c_baie = TopBox("baie", 500, 482, 395, rules)
# c_baie.add_tandem_box("D")
# c_baie.add_tandem_box("D")
c_baie.add_front_lateral_2("left")
c_baie.add_pol(1, rules["cant_pol"])
c_baie.add_front([[100, 51.8],[100, 51.8]], "drawer")
c_baie.remove_all_pfl()
mobila.append(c_baie)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)
mobila.export_pal_for_proficut()