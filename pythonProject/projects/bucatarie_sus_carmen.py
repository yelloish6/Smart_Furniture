from build_corpuri_oo import *

mobila = comanda("Carmen Hurdugaciu", 100)

# rules = {
#     "thick_pal": 18,
#     "thick_front": 18,
#     "thick_blat": 38,
#     "height_legs": 100,
#     "general_width": 600,
#     "width_blat": 600,
#     "gap_spate": 50,
#     "gap_fata": 50,
#     "gap_front": 2,
#     "cant_general": 0.4,
#     "cant_pol": 2,
#     "cant_separator": 0.4,
# }
#
# req = {
#     "h_bucatarie": 2070,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
#     "h_faianta_top": 1470,
#     "h_faianta_base": 900,
#     "depth_base": 600,  # adancime blat jos
#     "top_height": 600,
#     "top_depth": 600,
#     "blat_height": 880,
#     "cuptor_height": 595,
#     "MsV_height_min": 815,
#     "MsV_height_max": 875,
#     "material_pal": "W908ST2 - pal alb perlat jos| Stejar Bardolino sus",
#     "frezare_fronturi": "A75/P AquaBlue sus, simplu Alb jos"
# }
#
# base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
# base_width = 600
# base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]
#
# top_height = req["h_bucatarie"] - req["h_faianta_top"] + 5
# top_width = 600
# top_depth = 300
#
# tower_height = req["h_bucatarie"] - rules["height_legs"]
# tower_width = 600
# tower_depth = req["depth_base"] - rules["gap_fata"]

picioare = 100
gen_h = 600
gen_w = 600
gen_d = 300
gap_spate = 50
gap_fata = 50
gen_cant = 0.4
gen_cant_pol = 2
gen_cant_sep = 0.4
gen_gap_front = 2
th_pal = 18

# ms1 = BaseBox("MS1", base_height, base_width, base_depth, rules)
# ms1.addFront([100,100],"door")
# mobila.append(ms1)


# 500, 150, 1000, 150, 500
ms1 = corp("MS1", gen_h, 500, gen_d, th_pal, gen_cant)
ms1.buildTopBox()
ms1.addPol(1, gen_cant_pol)
ms1.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms1)

ms2 = corp("MS2", gen_h, 150, gen_d, th_pal, gen_cant)
ms2.buildTopBox()
ms2.addPol(3, gen_cant_pol)
ms2.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms2)

ms3 = corp("MS3", gen_h, 1000, gen_d, th_pal, gen_cant)
ms3.buildTopBox()
ms3.addPol(1, gen_cant_pol)
ms3.addFront([[100,50],[100,50]], gen_gap_front, "door")
mobila.append(ms3)

ms4 = corp("MS4", gen_h, 150, gen_d, th_pal, gen_cant)
ms4.buildTopBox()
ms4.addPol(3, gen_cant_pol)
ms4.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms4)

ms5 = corp("MS5", gen_h, 500, gen_d, th_pal, gen_cant)
ms5.buildTopBox()
ms5.addPol(1, gen_cant_pol)
ms5.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms5)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)