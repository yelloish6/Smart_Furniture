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
    "client": "Eligia - bucatarie",
    "h_bucatarie": 2500,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
    "h_faianta_top": 1200,
    "h_faianta_base": 900,
    "depth_base": 600,  # adancime blat jos
    "top_height": 600,
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
    "discount": 100,
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

bar = Bar("Bar", 1200, 2400, 500, rules)
mobila.append(bar)
bar.move("y", -2000)
bar.move("x", 1000)

j1 = SinkBox("J1", base_height, 1200, base_depth, rules)
j1.add_front([[50, 100], [50, 100]], "drawer")
mobila.append(j1)
j1.move("x", -bar.width)


j2 = MsVBox("J2", base_height, 600, base_depth, rules)
mobila.append(j2)
j2.move("x", -bar.width)

j3 = BaseBox("J3", base_height, 600, base_depth, rules)
j3.add_tandem_box("M")
j3.add_tandem_box("D")
j3.add_tandem_box("D")
j3.add_front([[40, 100], [40, 100], [20, 100]], "door")
mobila.append(j3)
j3.move("x", -bar.width)

j4 = BaseBox("J4", base_height, 600, base_depth, rules)
j4.add_front([[100, 100]], "door")
mobila.append(j4)
j4.move("x", -bar.width)

j5 = BaseBox("J5", base_height, 600, base_depth, rules)
j5.add_front([[100, 100]], "drawer")
mobila.append(j5)
j5.move("x", -bar.width)

j6 = BaseBox("j6", base_height, 600, base_depth, rules)
j6.add_pol(1, "0.4")
j6.add_front([[100, 100]], "door")
mobila.append(j6)
j6.rotate("z")
j6.rotate("z")
j6.move("y",-2000+j6.depth)

j7 = BaseBox("j7", base_height, 600, base_depth, rules)
j7.add_tandem_box("M")
j7.add_tandem_box("D")
j7.add_tandem_box("D")
j7.add_front([[40, 100], [40, 100], [20, 100]], "door")
mobila.append(j7)
j7.rotate("z")
j7.rotate("z")
j7.move("y",-2000+j7.depth)


j8 = JollyBox("j8", base_height, 300, base_depth, rules)
j8.add_front([[100, 100]], "door")
mobila.append(j8)

j9 = BaseBox("j9", base_height, 900, base_depth, rules)
j9.add_front([[100, 50], [100, 50]], "drawer")
mobila.append(j9)
#
# # corpurile de sus
#
# for i in range(3):
#     corp = TopBox("S" + str(i), 800, 1200, top_depth, rules)
#     corp.add_front([[100, 50], [100, 50]], "door")
#     mobila.append(corp)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)