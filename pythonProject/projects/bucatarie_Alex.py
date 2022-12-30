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
    "client": "Alex Trifan",
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

mobila = Comanda("Alex Trifan", req["discount"], req)

base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
base_width = 600
base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]

top_height = req["h_bucatarie"] - req["h_faianta_top"] + 5
top_width = 600
top_depth = 300

tower_height = req["h_bucatarie"] - rules["height_legs"]
tower_width = 600
tower_depth = req["depth_base"] - rules["gap_fata"]

j1 = SinkBox("j1", base_height, 1000, base_depth, rules)
j1.add_front([[100, 50], [100, 50]], "door")
mobila.append(j1)

t1 = TowerBox("t1", tower_height, tower_width, tower_depth, rules, [base_height, 300, 300], 50, [1, 1, 1, 1])
mobila.append(t1)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)
mobila.export_pal_for_proficut()
