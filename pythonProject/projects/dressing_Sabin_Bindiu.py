from elements.comanda import *
from elements.corp import *
from architectures.dressing import *

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 100,
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
    "client": "Sabin Bindiu - dressing",
    "h_bucatarie": 2200,  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
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

mobila = Comanda("Sabin Bindiu - dressing", 0, req)

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

t1 = CorpDressing("T1", tower_height, tower_width, tower_depth, rules, [], [0, 0, 0, 0])
t1.add_pol(6, rules["cant_pol"])
t1.add_pfl()
mobila.append(t1)

t2 = CorpDressing("T2", tower_height, tower_width, tower_depth, rules, [], [0, 0, 0, 0])
t2.add_pol(6, rules["cant_pol"])
t2.add_pfl()
mobila.append(t2)

t3 = CorpDressing("T3", tower_height, tower_width * 2, tower_depth, rules, [500, 1300], [0, 0, 0, 0])
t3.add_pol(2, rules["cant_pol"])
#t3.addTandemBox("D")
#t3.addTandemBox("D")
t3.add_pfl()
mobila.append(t3)

t4 = CorpDressing("T4", tower_height, tower_width * 2, tower_depth, rules, [500, 1300], [0, 0, 0, 0])
t4.add_pol(2, rules["cant_pol"])
#t4.addTandemBox("D")
#t4.addTandemBox("D")
t4.add_pfl()
mobila.append(t4)

# t5 = TopBox("T5", 800, 600, 300, rules)
# t5.add_pfl()
# mobila.append(t5)
#
# t6 = TopBox("T6", 800, 600, 300, rules)
# t6.add_pol(3, rules["cant_pol"])
# t6.add_pfl()
# mobila.append(t6)
#
# t7 = TopBox("T7", 800, 900, 300, rules)
# t7.add_pfl()
# mobila.append(t7)
#
# t8 = TopBox("T8", 2200 - 900, 300, 300, rules)
# t8.add_pfl()
# t8.add_pol(4, rules["cant_pol"])
# mobila.append(t8)
#
# t9 = TopBox("T9", 2200, 600, 300, rules)
# t9.add_pfl()
# t9.add_pol(2, rules["cant_pol"])
# t9.addTandemBox("D")
# t9.addTandemBox("D")
# t9.addTandemBox("D")
# t9.addTandemBox("D")
# mobila.append(t9)
#
# t10 = TopBox("T10", 2200, 600, 300, rules)
# t10.add_pfl()
# t10.add_pol(2, rules["cant_pol"])
# t10.addTandemBox("D")
# t10.addTandemBox("D")
# t10.addTandemBox("D")
# t10.addTandemBox("D")
# mobila.append(t10)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)