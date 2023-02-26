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
    "gap_spate": 0,
    "gap_fata": 50,
    "gap_front": 2,
    "cant_general": 1,
    "cant_pol": 2,
    "cant_separator": 1,
}

req = {
    "client": "Valea Mare",
    "Client Proficut": 'Bogdan Urs',  # nume client Proficut
    "Tel Proficut": '0740472185',  # numar telefon
    "Transport": 'Da',  # transport (Da/Nu)
    "Adresa": 'Mosnita Veche, str. Borsa, Nr. 38',
    "h_bucatarie": 0,
    "h_faianta_top": 0,
    "h_faianta_base": 0,
    "depth_base": 600,
    "top_height": 0,
    "top_height_2": 0,
    "top_depth": 0,
    "top_depth_2": 0,
    "blat_height": 850 - 105, # inaltimea fata inaltimea chiuvetei
    "cuptor_height": 0,
    "MsV_height_min": 0,
    "MsV_height_max": 0,
    "material_pal": "H1146ST10",
    "material_front": "A34/R3 Satin Alb Mat",  #frezare si culoare
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "PFL Alb",
    "h_rate": 120,
    "discount": 100,
    "nr_electrocasnice": 1  # plita, cuptor, chiuveta, microunde, frigider, hota

}

mobila = Comanda("Valea Mare Baie", req["discount"], req)

base_height = req["blat_height"] - rules["height_legs"] - rules["thick_blat"]
base_width = 600
base_depth = req["depth_base"] - rules["gap_fata"] - rules["gap_spate"]

top_height = req["h_bucatarie"] - req["h_faianta_top"] + 5
top_width = 600
top_depth = 300

tower_height = req["h_bucatarie"] - rules["height_legs"]
tower_width = 600
tower_depth = req["depth_base"] - rules["gap_fata"]

j1 = BaseBox("j1", base_height, base_width, base_depth, rules)
j1.add_wine_shelf(4, "right", rules["cant_pol"])
j1.add_pol(1,rules["cant_pol"])
j1.add_front([[50, 74], [50, 74]], "door")
j1.remove_all_pfl()

# blat = Blat("blat", j1.width, rules["width_blat"], rules["thick_blat"])
# blat.move("z",j1.height)
# j1.append(blat)

list_pal = list(filter(lambda material: material.__getattribute__("type") == "pal", j1.material_list))

for i in range(len(list_pal)):
    element = list_pal[i]
    if "sep" in element.__getattribute__("label"):
        len_sep = element.__getattribute__("length")
    print(element.__getattribute__("label"), element.__getattribute__("length"))
for i in range(len(list_pal)):
    element = list_pal[i]
    if "pol" in element.__getattribute__("label"):
        element.length = element.length - len_sep - j1.thick_pal
    print(element.__getattribute__("label"), element.__getattribute__("length"))
mobila.append(j1)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)
mobila.export_pal_for_proficut()
mobila.export_pfl_for_proficut()
mobila.export_front_for_nettfront()
