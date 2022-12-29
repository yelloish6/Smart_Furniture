#from build_corpuri_oo import *
from build_corpuri_oo_refactored import *



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
    "cant_general": 0.4,
    "cant_pol": 2,
    "cant_separator": 0.4,
}

req = {
    "client": "Alexandra Marcu",
    "h_bucatarie": 2200,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
    "h_faianta_top": 1600,
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
    "frezare_fronturi": "A34/R3",
    "h_rate": 100,
    "discount": 0,
    "nr_electrocasnice": 5
}

mobila = Comanda("Alexandra Marcu", 0, req)

base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
base_width = 600
base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]

top_height = 800
top_width = 600
top_depth = 350

top_height_2 = 400
top_width_2 = 600
top_depth_2 = 500

tower_height = req["h_bucatarie"] - rules["height_legs"]
tower_width = 600
tower_depth = req["depth_base"] - rules["gap_fata"]

# picioare = 100
# gen_h = 600
# gen_w = 600
# gen_d = 300
# gap_spate = 50
# gap_fata = 50
# gen_cant = 0.4
# gen_cant_pol = 2
# gen_cant_sep = 0.4
# gen_gap_front = 2
# th_pal = 18

# ms1 = BaseBox("MS1", base_height, base_width, base_depth, rules)
# ms1.addFront([100,100],"door")
# mobila.append(ms1)

j1 = SinkBox("J1", base_height, 900, base_depth, rules)
j1.add_front([[100, 50], [100, 50]], "door")
mobila.append(j1)

s1 = TopBox("S1", top_height, 600, top_depth, rules)
s1.add_front([[100, 100]], "door")
mobila.append(s1)

s2 = TopBox("S2", top_height, 600, top_depth, rules)
s2.add_front([[100,100]], "door")
mobila.append(s2)

j5 = BaseBox("J5", base_height, 600, base_depth, rules)
j5.add_tandem_box("D")
j5.add_tandem_box("D")
j5.add_tandem_box("M")
j5.add_front([[40, 100], [40, 100], [20, 100]], "drawer")
mobila.append(j5)

j2 = BaseBox("J2", base_height, 600, base_depth, rules)
j2.add_pol(1, "0.4")
j2.add_front([[100, 100]], "door")
mobila.append(j2)

s3 = TopBox("S3", top_height - 40, 600, top_depth, rules)
s3.add_front([[100,100]], "door")
mobila.append(s3)

t1 = TowerBox("T1", tower_height, 800, tower_depth, rules, [base_height, 300, 300], 50, [1,1,1,1])
mobila.append(t1)

s4 = TopBox("S4", 500, 600, top_depth, rules)
s4.add_front([[100,100]], "door")
mobila.append(s4)

s5 = TopBox("S5", 500, 600, top_depth, rules)
s5.add_front([[100,100]], "door")
mobila.append(s5)

s6 = TopBox("S6", 500, 600, top_depth, rules)
s6.add_front([[100,100]], "door")
mobila.append(s6)

t2 = TowerBox("T2", tower_height, 600, tower_depth, rules, [base_height, 300, 300], 50, [1,1,1,1])
mobila.append(t2)

s7 = TopBox("S7", 500, 600, top_depth, rules)
s7.add_front([[100,100]], "door")
mobila.append(s7)

t3 = TowerBox("T3", tower_height, 1000, tower_depth, rules, [base_height, 300, 300], 50, [1,1,1,1])
mobila.append(t3)

t4 = TowerBox("T4", tower_height, 1000, tower_depth, rules, [base_height, 300, 300], 50, [1,1,1,1])
mobila.append(t4)

t5 = TowerBox("T5", tower_height, 1000, tower_depth, rules, [base_height, 300, 300], 50, [1,1,1,1])
mobila.append(t5)


mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)