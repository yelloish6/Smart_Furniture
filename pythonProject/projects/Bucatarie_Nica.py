from build_corpuri_oo import *
from input_Nica import *

mobila = comanda(nume_client, discount_manopera)
mobila.__setattr__("frezare", frezare_fronturi)


j1 = corp("J1", gen_h_base, 950 - gap_spate, 988 - gap_spate, 18, gen_cant)
j1.buildBaseCorner(350 + gap_fata, 388 + gap_fata, "right", 18, False)
mobila.append(j1)

j2 = corp("J2", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j2.buildBaseBox()
j2.add_sep_h(j2.width - 2 * j2.pal_width, 0, 100, gen_cant_sep)
j2.addFront([[round(((gen_h_base - h_cuptor)/gen_h_base)*100),100]], gen_gap_front, "drawer")
j2.add_tandem_box("M")
mobila.append(j2)

j3 = corp("J3", gen_h_base, 490, gen_d_base, 18, gen_cant)
j3.buildBaseBox()
#j3.addSeparator("v",gen_cant_sep)
j3.addPol(1,gen_cant_pol)
j3.addFront([[100, 50],[100, 50]], gen_gap_front, "door")
mobila.append(j3)

j4 = corp("J4", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j4.buildMsVBox()
mobila.append(j4)

j5 = corp("J5", gen_h_base, 1242 - gap_spate, gen_d_base, 18, gen_cant)
j5.buildSinkBox()
j5.add_front_manual(gen_h_base - 4, 642 + gap_fata)
mobila.append(j5)

j6 = corp("J6", gen_h_base, gen_w + gap_fata, gen_d_base, 18, gen_cant)
j6.buildJolyBox()
#j6.addPol(1,gen_cant_pol)
j6.add_separator("v", gen_cant_sep)
j6.add_separator("h", gen_cant_sep)
j6.addFront([[100, 100]], gen_gap_front, "door")
mobila.append(j6)

j7 = corp("J7", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j7.buildBaseBox()
j7.add_tandem_box("M")
j7.add_tandem_box("D")
j7.add_tandem_box("D")
j7.addFront([[20, 100], [40, 100], [40, 100]], gen_gap_front, "drawer")
mobila.append(j7)

t1 = corp("T1", gen_h_tower, 600, gen_d_tower, 18, gen_cant)
#t1.buildTower(gen_h_base - 2 * t1.pal_width, 300, gen_h_tower - (gen_h_base - 2 * t1.pal_width) - 300 - gen_h_top, 0)
t1.buildTower([gen_h_base - 2 * t1.pal_width,300, gen_h_tower - gen_h_base - 318 - gen_h_top], 0, [0, 0, 0, 1])
t1.addPol(1, gen_cant_pol)
t1.add_tandem_box("M")
t1.add_tandem_box("D")
t1.add_tandem_box("D")
t1.add_front_manual(146, 596)
t1.add_front_manual(294, 596)
t1.add_front_manual(294, 596)
#t1.addFront([[20, 100], [40, 100], [40, 100]], gen_gap_front, "drawer")
#t1.addFrontManual(gen_h_top - 4, gen_w - 4)
mobila.append(t1)

s1 = corp("S1", h_bucatarie-h_blat, 770, 800, 18, gen_cant)
s1.buildBaseCorner(470, 400, "right", th_front, False)
mobila.append(s1)

s2 = corp("S2", gen_h_top, 188, gen_d_top, 18, gen_cant)
s2.buildTopBox()
s2.addPol(3, gen_cant_pol)
s2.addFront([[100,100]],gen_gap_front, "door")
mobila.append(s2)

s3 = corp("s3", gen_h_top - 40, gen_w, gen_d_top, 18, gen_cant)
s3.buildTopBox()
s3.add_sep_h(s3.width - 2 * s3.pal_width, 0, 710, gen_cant_sep)
s3.addPol(1,gen_cant_pol)
s3.addFront([[30, 100], [70, 100]], 2, "door")
mobila.append(s3)

s4 = corp("s4", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s4.buildTopBox()
s4.add_sep_h(s4.width - 2 * s4.pal_width, 0, 750, gen_cant_sep)
s4.addPol(2, gen_cant_pol)
s4.addFront([[30, 100],[70, 100]], 2, "door")
mobila.append(s4)

s5 = corp("s5", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s5.buildTopBox()
s5.add_sep_h(s5.width - 2 * s5.pal_width, 0, 750, gen_cant_sep)
s5.addPol(2, gen_cant_pol)
s5.addFront([[30, 100],[70, 100]], 2, "door")
mobila.append(s5)

s6 = corp("s6", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s6.buildTopBox()
s6.add_sep_h(s6.width - 2 * s6.pal_width, 0, 750, gen_cant_sep)
s6.addPol(2, gen_cant_pol)
s6.addFront([[30, 100],[70, 100]], 2, "door")
mobila.append(s6)

s7 = corp("s7", gen_h_top, 530 - 6, 600, th_pal, gen_cant)
s7.buildTopCorner(230 - 6, 300, "right", th_front)
mobila.append(s7)

s8 = corp("s8", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s8.buildTopBox()
s8.addPol(2, gen_cant_pol)
s8.addFront([[100,50],[100,50]],gen_gap_front, "door")
mobila.append(s8)

s9 = corp("s9", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s9.buildTopBox()
s9.addPol(2, gen_cant_pol)
s9.addFront([[100,50],[100,50]],gen_gap_front, "door")
mobila.append(s9)

s10 = corp("s10", 480, 750, gen_d_tower, 18, gen_cant)
s10.buildTopBox()
s10.addPol(1, gen_cant_pol)
s10.addFront([[100,100]],gen_gap_front, "door")
mobila.append(s10)

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