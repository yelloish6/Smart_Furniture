from build_corpuri_oo import *
from input_Marius import *

mobila = comanda(nume_client, discount_manopera)
mobila.__setattr__("frezare", frezare_fronturi)

mobila2 = comanda("Marius Lazarescu sus", discount_manopera)

j1 = corp("J1", gen_h_base, 300, gen_d_base, 18, gen_cant)
j1.buildJolyBox()
mobila.append(j1)

j2 = corp("J2", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j2.buildBaseBox()
j2.remPFLObject("J2.pfl")
j2.add_sep_h(j2.width - 2 * j2.pal_width, 0, 100, gen_cant_sep)
j2.addFront([[round(((gen_h_base - h_cuptor)/gen_h_base)*100),100]], gen_gap_front, "drawer")
j2.add_tandem_box("M")
mobila.append(j2)

j3 = corp("J3", gen_h_base, 1000 - gap_spate, 950 - gap_spate, 18, gen_cant)
j3.buildBaseCorner(400 + gap_fata, 350 + gap_fata, "right", 18, True)
mobila.append(j3)

j4 = corp("J4", gen_h_base, 1150, gen_d_base, 18, gen_cant)
j4.buildSinkBox()
j4.addFront([[100,50],[100,50]],gen_gap_front,"door")
mobila.append(j4)

j5 = corp("J5", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j5.buildMsVBox()
latMsV = placa_pal("J5.latMsV", gen_h_base + picioare, d_base - gap_fata, th_pal, 1, "", 1, "")
latMsV.rotate("y")
latMsV.move("x", j5.width - th_pal)
j5.addPalObject(latMsV)
mobila.append(j5)

j6 = corp("J6", gen_h_base, 150, gen_d_base, 18, gen_cant)
j6.buildJolyBox()
mobila.append(j6)

j7 = corp("J7", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j7.buildBaseBox()
j7.add_tandem_box("M")
j7.add_tandem_box("D")
j7.add_tandem_box("D")
j7.addFront([[20, 100], [40, 100], [40, 100]], gen_gap_front, "drawer")
mobila.append(j7)

j8 = corp("J8", gen_h_base, 500, gen_d_base, 18, gen_cant)
j8.buildBaseBox()
j8.addPol(1, gen_cant_pol)
j8.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(j8)

j9 = corp("J9", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j9.buildBaseBox()
j9.add_tandem_box("M")
j9.add_tandem_box("D")
j9.add_tandem_box("D")
j9.addFront([[20, 100], [40, 100], [40, 100]], gen_gap_front, "drawer")
mobila.append(j9)

j10 = corp("J10", gen_h_base + picioare, 150, gen_d_base, 18, gen_cant)

#adaugat manual placi
j10lat = placa_pal("J10.lat", j10.height, j10.depth, th_pal, 1, "", 1, "")
j10lat.rotate("y")
j10lat.move("x", j10.width - th_pal)
j10.addPalObject(j10lat)

j10spate = placa_pal("J10.spate", j10.height, j10.width - th_pal, th_pal, 1, "", 1, "")
j10spate.rotate("x")
j10spate.move("y", j10.depth - th_pal)
j10spate.rotate("y")
j10.addPalObject(j10spate)


#j10.buildBaseBox()
j10.addPol(4, gen_cant_pol)
mobila.append(j10)

#TODO corp din stejar bardolino cu pfl stejar bardolino sau cu spate de pal
s1 = corp("S1", gen_h_top, 300, gen_d_top, 18, gen_cant)
s1.buildTopBox()
s1.remPFLObject("S1.pfl")
s1spate = placa_pal("S1.spate", s1.height-(2*th_pal), s1.width-(2*th_pal),th_pal,"","","","")
s1spate.rotate("x")
s1spate.rotate("y")
s1spate.move("y", s1.depth - th_pal)
s1spate.move("z", th_pal)
s1spate.move("x", th_pal)
s1.addPalObject(s1spate)
s1.addPol(2, gen_cant_pol)
s1.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(s1)

s2 = corp("S2", gen_h_top-40, gen_w, gen_d_top, 18, gen_cant)
s2.buildTopBox()
s2.remPFLObject("S2.pfl")
s2.addPol(1, gen_cant_pol)
s2.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(s2)

s3 = corp("S3", gen_h_top, 400, gen_d_top, 18, gen_cant)
s3.buildTopBox()
s3.addPol(1, gen_cant_pol)
s3.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(s3)

s4 = corp("S4", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s4.buildTopBox()
s4.addPol(1, gen_cant_pol)
s4.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(s4)

s5 = corp("S5", gen_h_top, 900, gen_d_top, 18, gen_cant)
s5.buildTopBox()
s5.remPFLObject("S5.pfl")
s5spate = placa_pal("S5.spate", s5.height - 2 * th_pal, s5.width - 2 * th_pal, th_pal, "", "", "", "")
s5spate.rotate("x")
s5spate.rotate("y")
s5spate.move("y", s1.depth - th_pal)
s5spate.move("z", th_pal)
s5spate.move("x", th_pal)
s5.addPalObject(s5spate)
s5.addPol(1, gen_cant_pol)
s5.addFront([[100, 50], [100, 50]], gen_gap_front, "door")
mobila.append(s5)

#TODO de inlocuit cu rafturi simple pe perete
#s6 = corp("S6", gen_h_top, 900, gen_d_top, 18, gen_cant)
#s6.buildTopBox()
#s6.addPol(1, gen_cant_pol)
#s6.addFront([[100, 100]], gen_gap_front, "door")
#mobila.append(s6)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)

# mobila2.print_status()
# mobila2.export_csv()
# mobila2.draw(0, 0, 0)


# verificari
if h_bucatarie - gen_h_top < h_faianta_top:
    print("Verificare inaltime fainata sus: OK", "Suprapunere corp suspendat faianta: ",
          -h_bucatarie + gen_h_top + h_faianta_top, "mm")
else:
    print("Verificare inaltime fainata sus: ERROR", "Distanta corp suspendat faianta: ",
          h_bucatarie - gen_h_top - h_faianta_top, "mm")

if gen_h_base + picioare + w_blat > h_faianta_base:
    print("Verificare inaltime fainata jos: OK", "Suprapunere blat si faianta jos",
          gen_h_base + picioare + w_blat - h_faianta_base, "mm")
else:
    print("Verificare inaltime fainata jos: ERROR", "Distanta intre blat si faianta:",
          h_faianta_base - gen_h_base - picioare - w_blat, "mm")

print("Verificare distanta de la blat la corpurile suspendate (recomandare min. 600): ",
      h_bucatarie - gen_h_top - w_blat - gen_h_base - picioare, "mm")