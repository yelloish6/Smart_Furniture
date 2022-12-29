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
    "client": "Irina Francu",
    "h_bucatarie": 2700,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
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
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "Alb",
    "h_rate": 120,
    "discount": 0,
    "nr_electrocasnice": 6
}

mobila = Comanda("Irina Francu", 0, req)

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

bar = Bar("Bar", 1150, 1400, 450, rules)
mobila.append(bar)

j1 = BaseBox("J1", base_height, 800, base_depth, rules)
j1.add_tandem_box("D")
j1.add_tandem_box("D")
j1.add_front([[50, 100], [50, 100]], "drawer")
mobila.append(j1)

j2 = BaseBox("J2", base_height, 900, base_depth, rules)
j2.add_pol(1, "0.4")
j2.add_front([[100, 50], [100, 50]], "door")
mobila.append(j2)

j3 = JollyBox("J3", base_height, 350, base_depth, rules)
j3.add_front([[100, 100]], "door")
mobila.append(j3)

j4 = BaseBox("J4", base_height, 600, base_depth, rules)
j4.add_front([[100, 100]], "door")
mobila.append(j4)

j5 = BaseBox("J5", base_height, 900, base_depth, rules)
j5.add_tandem_box("D")
j5.add_tandem_box("D")
j5.add_front([[50, 100], [50, 100]], "drawer")
mobila.append(j5)

j6 = BaseBox("J6", base_height, 900, base_depth, rules)
j6.add_pol(1, rules["cant_pol"])
j6.add_front([[100, 100]], "door")
mobila.append(j6)

j7 = SinkBox("J7", base_height, 850, base_depth, rules)
j7.add_front([[100, 50], [100, 50]], "door")
mobila.append(j7)

j8 = BaseBox("J8", base_height, 900, base_depth, rules)
j8.add_pol(1, rules["cant_pol"])
j8.add_front([[100, 50], [100, 50]], "door")
mobila.append(j8)

j9 = BaseBox("J9", base_height, 600, base_depth, rules)
j9.add_front([[100, 100]], "door")
mobila.append(j9)

# corpurile de sus sus
ss_widths =  [700, 600, 900, 600, 600, 450, 600]
ss_heights = [400, 400, 400, 400, 400, 400, 400]
for i in range(4):
    corp = TopBox("ss" + str(i), ss_heights[i], ss_widths[i], top_depth_2, rules)
    corp.add_front([[100, 100]], "door")
    mobila.append(corp)

sj_widths =  [350, 350, 600,      450, 450, 600, 600, 450, 600]
sj_heights = [800, 800, 800 - 40, 800, 800, 800, 800, 800, 800]
for i in range(len(sj_widths)):
    corp = TopBox("sj" + str(i), sj_heights[i], sj_widths[i], top_depth, rules)
    corp.add_pol(1, rules["cant_pol"])
    corp.add_front([[100, 50], [100, 50]], "door")
    mobila.append(corp)

tower_widths = [600, 600, 600, 500, 500]
for i in range(len(tower_widths)):
    corp = TowerBox("tower" + str(i), tower_height, tower_widths[i], tower_depth, rules,
                    [base_height, 1800 - base_height, 400], 50, [1,1,1,1])
    corp.add_pol(3, rules["cant_pol"])
    corp.add_tandem_box("D")
    mobila.append(corp)

raft = Raft("Raft", tower_height, req["top_depth_2"], 250, 5, rules)
mobila.append(raft)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)