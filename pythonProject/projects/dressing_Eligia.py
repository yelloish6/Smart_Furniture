from build_corpuri_oo_refactored import *

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 0,
    "general_width": 600,
    "width_blat": 600,
    "gap_spate": 50,
    "gap_fata": 0,
    "gap_front": 2,
    "cant_general": 0.4,
    "cant_pol": 2,
    "cant_separator": 0.4,
}

req = {
    "client": "Eligia - dressing",
    "h_bucatarie": 2400,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
    "h_faianta_top": 1200,
    "h_faianta_base": 900,
    "depth_base": 600,  # adancime blat jos
    "top_height": 800,
    "top_height_2": 400,
    "top_depth": 350,
    "top_depth_2": 500,
    "blat_height": 900,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "W962ST2",
    "material_front": "A34/R3",
    "material_blat": "Blat Stejar Bardolino",
    "material_pfl": "Alb",
    "h_rate": 100,
    "discount": 100,
    "nr_electrocasnice": 0
}

mobila = Comanda("Eligia - dressing", 0, req)

base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
base_width = 600
base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]

top_height = 2200
top_width = 600
top_depth = 350

top_height_2 = 400
top_width_2 = 600
top_depth_2 = 500

tower_height = req["h_bucatarie"] - rules["height_legs"]
tower_width = 600
tower_depth = req["depth_base"] - rules["gap_fata"]

t1 = TowerBox("T1", tower_height, tower_width, tower_depth, rules, [],0,[0,0,0,0])
t1.add_pol(6, rules["cant_pol"])
t1.addPFL()
t1.add_front([[100, 100]], "door")
mobila.append(t1)

t2 = TowerBox("T2", tower_height, tower_width, tower_depth, rules, [],0,[0,0,0,0])
t2.add_pol(6, rules["cant_pol"])
t2.addPFL()
t2.add_front([[100, 100]], "door")
mobila.append(t2)

t3 = TowerBox("T3", tower_height, tower_width * 2, tower_depth, rules, [500, 1300],0,[0,0,0,0])
t3.add_pol(2, rules["cant_pol"])
t3.add_tandem_box("D")
t3.add_tandem_box("D")
t3.add_front([[10, 100], [10, 100], [80, 100]], "door")
t3.addPFL()
mobila.append(t3)

t4 = TowerBox("T4", tower_height, tower_width * 2, tower_depth, rules, [500, 1300],0,[0,0,0,0])
t4.add_pol(2, rules["cant_pol"])
t4.add_tandem_box("D")
t4.add_tandem_box("D")
t4.addPFL()
t4.add_front([[10, 100], [10, 100], [80, 100]], "door")
mobila.append(t4)

t5 = TowerBox("T5", tower_height, tower_width, tower_depth, rules, [],0,[0,0,0,0])
t5.add_pol(6, rules["cant_pol"])
t5.addPFL()
t5.add_front([[100, 100]], "door")
mobila.append(t5)

t6 = TowerBox("T6", tower_height, tower_width, tower_depth, rules, [],0,[0,0,0,0])
t6.add_pol(6, rules["cant_pol"])
t6.addPFL()
t6.add_front([[100, 100]], "door")
mobila.append(t6)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)