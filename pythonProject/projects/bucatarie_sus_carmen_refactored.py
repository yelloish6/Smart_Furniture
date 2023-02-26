#from build_corpuri_oo_refactored import *
from elements.comanda import *
from architectures.kitchen import *

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
    "client": "Carmen - bucatarie sus",
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
    "material_front": "A34/R3 Satin Alb Mat",
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "PFL Alb",
    "h_rate": 120,
    "discount": 100,
    "nr_electrocasnice": 6
}

mobila = Comanda("Carmen Hurdugaciu Refact", 100, req)

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
ms1 = TopBox("MS1", top_height, 500, top_depth, rules)
ms1.add_pol(1, rules["cant_pol"])
ms1.add_front([[100, 100]], "door")
mobila.append(ms1)

ms2 = TopBox("MS2", top_height, 150, top_depth, rules)
ms2.add_pol(3, "2")
ms2.add_front([[100,100]], "door")
mobila.append(ms2)

ms3 = TopBox("MS3", top_height, 1000, top_depth, rules)
ms3.add_pol(1, "2")
ms3.add_front([[100,50],[100,50]], "door")
mobila.append(ms3)

ms4 = TopBox("MS4", top_height, 150, top_depth, rules)
ms4.add_pol(3, "2")
ms4.add_front([[100,100]], "door")
mobila.append(ms4)

ms5 = TopBox("MS5", top_height, 500, top_depth, rules)
ms5.add_pol(1, "2")
ms5.add_front([[100,100]], "door")
mobila.append(ms5)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)
mobila.export_pal_for_proficut()
mobila.export_front_for_nettfront()