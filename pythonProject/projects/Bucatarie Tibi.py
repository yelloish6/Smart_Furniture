from build_corpuri_oo import *

nume_client = "Tibi Vrabie"
discount_manopera = 0

# definitii bucatarie
#	2490 inaltime totala pana in tavan
#	faianta tavan 700?
#	faianta de jos 1650

h_bucatarie = 2230 + 150  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
h_faianta_top = 150+720+680
h_faianta_base = 150+720
d_base = 600  # adancime blat jos

# definitii mobila

#Grosimi
th_pal = 18
th_front = 18
w_blat = 38

frezare_fronturi = "Nedecis"
materail_pal = "W908ST2 - pal alb perlat"

picioare = 150
gen_w = 600
gap_spate = 50
gap_fata = 50
gen_cant = 0.4
gen_cant_pol = 2
gen_cant_sep = 0.4
gen_gap_front = 2

# top
gen_h_top = 720
gen_d_top = 300  # 300 plus 4 ca sa incapa intaritura in spatele hotei plus suruburile

# base
h_blat = 150+720
gen_h_base = h_blat - w_blat - picioare
gen_d_base = d_base - gap_spate - gap_fata

# tower
gen_h_tower = h_bucatarie - picioare
gen_d_tower = gen_d_base + 50

# electrocasnice
h_cuptor = 595 #59.5 cm

mobila = comanda(nume_client, discount_manopera)
mobila.__setattr__("frezare", frezare_fronturi)

t1 = corp("T1", gen_h_tower, 568, gen_d_tower, 18, gen_cant)
t1.buildTower(690, 602, 720, 40)
t1.addFront([[100,100]],gen_gap_front, "door")
mobila.append(t1)

t2 = corp("T2", gen_h_tower, 317, gen_d_tower, 18, gen_cant)
t2.buildTower(690, 602, 720, 40)
t2.addFront([[100,100]],gen_gap_front, "door")
mobila.append(t2)

j1 = corp("J1", gen_h_base, 818, gen_d_base, th_pal, gen_cant)
j1.buildSinkBox()
j1.addFront([[100,50],[100,50]],gen_gap_front, "door")
mobila.append(j1)

j2 = corp("J2", gen_h_base, 450, gen_d_base, th_pal, gen_cant)
j2.buildMsVBox()
t2.addFront([[100,100]],gen_gap_front, "door")
mobila.append(j2)

j3 = corp("J3", gen_h_base, 450, gen_d_base, th_pal, gen_cant)
j3.buildBaseBox()
j3.add_tandem_box("M")
j3.add_tandem_box("M")
j3.add_tandem_box("D")
t2.addFront([[30,100],[30,100],[60,100]],gen_gap_front, "drawer")
mobila.append(j3)

j4 = corp("J4", gen_h_base, 600, gen_d_base, th_pal, gen_cant)
j4.buildBaseBox()
j4.add_separator("h", gen_cant_sep)
j4.add_tandem_box("M")
mobila.append(j4)

t3 = corp("T3", gen_h_tower, 423, gen_d_tower, 18, gen_cant)
t3.buildTower(690, 602, 720, 40)
t3.addFront([[100,100]],gen_gap_front, "door")
mobila.append(t3)

s1 = corp("S1", gen_h_top, 800, gen_d_top, th_pal, gen_cant)
s1.buildTopBox()
s1.addPol(1,gen_cant_pol)
s1.addFront([[50,100],[50,100]],gen_gap_front, "door")
mobila.append(s1)

s2 = corp("S2", gen_h_top, 900, gen_d_top, th_pal, gen_cant)
s2.buildTopBox()
s2.addPol(1,gen_cant_pol)
s2.addFront([[50,100],[50,100]],gen_gap_front, "door")
mobila.append(s2)

s3 = corp("S3", gen_h_top, 600, gen_d_top, th_pal, gen_cant)
s3.buildTopBox()
s2.addPol(1,gen_cant_pol)
s3.addFront([[50,100],[50,100]],gen_gap_front, "door")
mobila.append(s3)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)

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
