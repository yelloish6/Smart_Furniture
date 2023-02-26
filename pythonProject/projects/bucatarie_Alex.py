from elements.comanda import *
from architectures.kitchen import *
from architectures.dressing import *

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 100,
    "general_width": 600,
    "width_blat": 550,
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
    "h_bucatarie": 1850,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 550,
    "top_height": 600,
    "top_height_2": 400,
    "top_depth": 600,
    "top_depth_2": 500,
    "blat_height": 850,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "W962ST2",
    "material_front": "A34/R3 Satin Alb Mat",  #frezare si culoare
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "PFL Alb",
    "h_rate": 120,
    "discount": 100,
    "nr_electrocasnice": 2  # plita, cuptor, chiuveta, microunde, frigider, hota
    # https://www.vidaxl.ro/e/vidaxl-chiuveta-de-bucatarie-lucrata-manual-negru-otel-inoxidabil/8720286179079.html
    # https://www.emag.ro/plita-incorporabila-mpm-45-gmh-16-gaz-3-zone-de-gatit-45-cm-negru-6354274/pd/D4Q7X2MBM/?X-Search-Id=46a48a7bc7da1880df57&X-Product-Id=63513001&X-Search-Page=1&X-Search-Position=8&X-Section=search&X-MB=0&X-Search-Action=view
    # https://www.dedeman.ro/timisoara2/baterie-bucatarie-ferro-fitness-bfs4b-stativa-monocomanda-alama-finisaj-cromat/-negru/p/3031462
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

# j1 = SinkBox("j1", base_height, 1000, base_depth, rules)
# j1.add_front([[100, 50], [100, 50]], "door")
# mobila.append(j1)

t1 = TowerBox("t1", tower_height, 600, 650, rules, [base_height, 300, 300], 0, [0, 0, 0, 0])
t1.add_front([[40, 100], [60, 100]], "door")
t1.add_pol(4, rules["cant_pol"])

t1.move("x", 100)
# mobila.append(t1)

#j2 = BaseCorner("j2", base_height, 950, 943, rules, 450, 503, "right", False)
j2 = BaseCorner("j2", base_height, 943, 950, rules, 503, 450, "left", False)

# adaugam polita manual sa vina pe cealalta parte, daca il facem cu left vine spatele spre chiuveta
pol = PlacaPal(j2.label + "pol", j2.width - (2 * j2.thick_pal), j2.depth - 470 - j2.thick_pal, rules["thick_pal"],
               rules["cant_pol"], "", "", "")
pol.move("x", j2.thick_pal)
pol.move("y", 470 + j2.thick_pal)
pol.move("z", j2.height / 2)
j2.append(pol)

j2.remove_material("pal", "j2.spate")
# # spate 1 440 694
# sp1 = PlacaPal(j2.label + ".sp1", j2.height - j2.thick_pal, 440, j2.thick_pal, "", "", "", "")
# sp1.rotate("y")
# sp1.rotate("z")
# sp1.move("z", j2.thick_pal)
# # sp1.move("x", 950)
# # sp1.move("y", 503)
# j2.append(sp1)
# # spate 2 712 475
sp2 = PlacaPal(j2.label + ".sp2", j2.height - j2.thick_pal, 500, j2.thick_pal, "1", "", "", "")
sp2.rotate("y")
sp2.move("z", j2.thick_pal)
sp2.move("x", j2.thick_pal)
sp2.move("y", 450)
j2.append(sp2)

j2.remove_all_pfl()
# j2.rotate("z")
# j2.rotate("z")
# j2.rotate("z")
j2.move("x", 10)


blat1 = Blat("blat1", 1000, 550, rules["thick_blat"])
blat1.rotate("z")
blat1.rotate("z")
blat1.rotate("z")
blat1.move("x", blat1.width - 70)
blat1.move("z", j2.height)
j2.append(blat1)

blat2 = Blat("blat2", 473, 600, rules["thick_blat"])
blat2.move("x", blat1.width - 70)
blat2.move("z", j2.height)
blat2.move("y", blat1.length - blat2.width)
j2.append(blat2)
j2.move("x", 1000)
mobila.append(j2)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)
mobila.export_pal_for_proficut()
mobila.export_pfl_for_proficut()
mobila.export_front_for_nettfront()
