from build_corpuri_oo import *
from input_Mirona import *

mobila = comanda(nume_client, discount_manopera)
mobila.__setattr__("frezare", frezare_fronturi)

"""
for i in range(len(corpuri)):
        c = corp(corpuri[i][1], corpuri[i][2], corpuri[i][3], corpuri[i][4], th_pal, corpuri[i][5])
        if corpuri[i][0] == "buildBaseCorner":
            c.buildBaseCorner(corpuri[i][3] - gen_d_base, corpuri[i][4] - gen_d_base, corpuri[i][6], th_front)
        elif corpuri[i][0] == "buildBaseBox":
            if corpuri[i][9] == "joly":
                c.buildJolyBox()
            elif corpuri[i][9] == "wine":
                c.buildBaseBox()
                c.addWineShelf(corpuri[i][10][0], corpuri[i][10][1], gen_cant_sep)
            else:
                c.buildBaseBox()
                for j in range(len(corpuri[i][9])):
                    c.addTandemBox(corpuri[i][9][j])
            c.addPol(corpuri[i][6] ,gen_cant_pol)
            c.addFront(corpuri[i][7], gen_gap_front, corpuri[i][8])
        elif corpuri[i][0] == "buildMsVBox":
            c.buildMsVBox()
        elif corpuri[i][0] == "buildSinkBox":
            c.buildSinkBox()
            c.addFront(corpuri[i][7], gen_gap_front, corpuri[i][8])
        elif corpuri[i][0] == "buildTopBox":
            c.buildTopBox()
            c.addPol(corpuri[i][6], gen_cant_pol)
            c.addFront(corpuri[i][7], gen_gap_front, corpuri[i][8])
        elif corpuri[i][0] == "buildTopCorner":
            c.buildTopCorner(corpuri[i][3] - gen_d_top, corpuri[i][4] - gen_d_top, corpuri[i][6], th_front)
        elif corpuri[i][0] == "buildTower":
            c.buildTower(corpuri[i][7][0], corpuri[i][7][1], corpuri[i][7][2], corpuri[i][7][3])
            c.addPol(corpuri[i][6], gen_cant_pol)
            #Se seteaza fronturile pentru turn
            #gap1
            if (corpuri[i][8][0] == 1) and (corpuri[i][8][1] == 0):
                    c.addFrontManual(corpuri[i][7][0] + (2 * th_pal) - 4, gen_w - 4)
            if (corpuri[i][8][0] == 1) and (corpuri[i][8][1] == 1):
                    c.addFrontManual(corpuri[i][7][0] + (1.5 * th_pal) - 3, gen_w - 4)
            #gap2
            if (corpuri[i][8][1] == 1) and (corpuri[i][8][0] == 0) and (corpuri[i][8][2] == 0):
                    c.addFrontManual(corpuri[i][7][1] + (2 * th_pal) - 4, gen_w - 4)
            if (((corpuri[i][8][1] == 1) and (corpuri[i][8][0] == 1) and (corpuri[i][8][2] == 0))
                    or ((corpuri[i][8][1] == 1) and (corpuri[i][8][0] == 0) and (corpuri[i][8][2] == 1))):
                    c.addFrontManual(corpuri[i][7][1] + (1.5 * th_pal) - 3, gen_w - 4)
            if (corpuri[i][8][1] == 1) and (corpuri[i][8][0] == 1) and (corpuri[i][8][2] == 1):
                c.addFrontManual(corpuri[i][7][1] + th_pal - 4, gen_w - 4)

            #gap3
            if (corpuri[i][8][2] == 1) and (corpuri[i][8][1] == 0) and (corpuri[i][8][3] == 0):
                    c.addFrontManual(corpuri[i][7][2] + (2 * th_pal) - 4, gen_w - 4)
            if (((corpuri[i][8][2] == 1) and (corpuri[i][8][1] == 1) and (corpuri[i][8][3] == 0))
                    or ((corpuri[i][8][2] == 1) and (corpuri[i][8][1] == 0) and (corpuri[i][8][3] == 1))):
                    c.addFrontManual(corpuri[i][7][2] + (1.5 * th_pal) - 3, gen_w - 4)
            if (corpuri[i][8][2] == 1) and (corpuri[i][8][1] == 1) and (corpuri[i][8][3] == 1):
                c.addFrontManual(corpuri[i][7][2] + th_pal - 4, gen_w - 4)

            #gap4
            if (corpuri[i][8][3] == 1) and (corpuri[i][8][2] == 0):
                    c.addFrontManual(gen_h_tower - corpuri[i][7][0] - corpuri[i][7][1] - corpuri[i][7][2] - (3 * th_pal) - 4 , gen_w - 4)
            if (corpuri[i][8][3] == 1) and (corpuri[i][8][2] == 1):
                    c.addFrontManual(gen_h_tower - corpuri[i][7][0] - corpuri[i][7][1] - corpuri[i][7][2] - (3.5 * th_pal) - 3, gen_w - 4)
        mobila.append(c)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)


"""
j1 = corp("J1", gen_h_base, 750 - 50, 1088 - 50, 18, gen_cant)
j1.buildBaseCorner(750 - 50 - gen_d_base, 1088 - 50 - gen_d_base, "left", 18, True)
mobila.append(j1)

j2 = corp("J2", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j2.buildBaseBox()
j2.addPol(1, gen_cant_pol)
j2.add_sep_h(j2.width - 2 * j2.pal_width, 0, 100, gen_cant_sep)
j2.addFront([[100, 100]], 2, "drawer")
mobila.append(j2)

j3 = corp("J3", gen_h_base, 450, gen_d_base, 18, gen_cant)
j3.buildBaseBox()
j3.addPol(1, 2)
j3.addFront([[100, 100]], 2, "door")
mobila.append(j3)

j4 = corp("J4", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j4.buildBaseBox()
j4.add_tandem_box("M")
j4.add_tandem_box("D")
j4.add_tandem_box("D")
j4.addFront([[20, 100], [40, 100], [40, 100]], 2, "drawer")
mobila.append(j4)

j5 = corp("J5", gen_h_base, 1000, gen_d_base, 18, gen_cant)
j5.buildSinkBox()
j5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(j5)

j6 = corp("J6", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j6.buildMsVBox()
mobila.append(j6)

j7 = corp("J7", gen_h_base, 300, gen_d_base, 18, gen_cant)
j7.buildJolyBox()
mobila.append(j7)

t1 = corp("T1", gen_h_tower, 600, gen_d_tower, 18, gen_cant)
t1.buildTower([gen_h_base - 2 * t1.pal_width, 590, 380], 40, [1, 0, 0, 1])
# t1.addFront([[100,100]],2,"door")
t1.addPol(1, gen_cant_pol)

mobila.append(t1)

s1 = corp("s1", gen_h_top, 585, gen_d_top, 18, gen_cant)
s1.buildTopBox()
s1.addPol(1, gen_cant_pol)
s1.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s1)

s2 = corp("s2", gen_h_top, 750, 488, 18, gen_cant)
s2.buildTopCorner(450, 188, "left", 18)
mobila.append(s2)

s3 = corp("s3", gen_h_top - 40, gen_w, gen_d_top, 18, gen_cant)
s3.buildTopBox()
s3.addFront([[100, 100]], 2, "door")
mobila.append(s3)

s4 = corp("s4", gen_h_top, 450, gen_d_top, 18, gen_cant)
s4.buildTopBox()
s4.addPol(1, gen_cant_pol)
s4.addFront([[100, 100]], 2, "door")
mobila.append(s4)

s5 = corp("s5", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s5.buildTopBox()
s5.addPol(1, gen_cant_pol)
s5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s5)

s6 = corp("s6", round(gen_h_top / 2), 1000, gen_d_top, 18, gen_cant)
s6.buildTopBox()
s6.addFront([[100, 100]], 2, "door")
mobila.append(s6)

s7 = corp("s7", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s7.buildTopBox()
s7.addPol(1, gen_cant_pol)
s7.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s7)

s8 = corp("s8", gen_h_top, 300, gen_d_top, 18, gen_cant)
s8.buildTopBox()
s8.addPol(1, gen_cant_pol)
s8.addFront([[100, 100]], 2, "door")
mobila.append(s8)

i1 = corp("I1", gen_h_base, 450, 400, 18, gen_cant)
i1.buildBaseBox()
i1.addPol(1, gen_cant_pol)
i1.addFront([[100, 100]], 2, "door")
i1.add_front_manual(gen_h_base, 800 + 18 + 18)
mobila.append(i1)

i2 = corp("I2", gen_h_base, 1000, 400, 18, gen_cant)
i2.buildSinkBox()
i2.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(i2)

i3 = corp("I3", gen_h_base, 450, 400, 18, gen_cant)
i3.buildBaseBox()
i3.addPol(1, gen_cant_pol)
i3.addFront([[100, 100]], 2, "door")
i1.add_front_manual(gen_h_base, 800 + 18 + 18)
mobila.append(i3)

i4 = corp("I4", gen_h_base, 450, 400, 18, gen_cant)
i4.buildBaseBox()
i4.add_wine_shelf(5, "left", gen_cant_sep)
i4.addFront([[100, 66]], 2, "door")
mobila.append(i4)

i5 = corp("I5", gen_h_base, 1000, 400, 18, gen_cant)
i5.buildBaseBox()
i5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(i5)

i6 = corp("I6", gen_h_base, 450, 400, 18, gen_cant)
i6.buildBaseBox()
i6.add_wine_shelf(5, "right", gen_cant_sep)
i6.addFront([[100, 66]], 2, "door")
mobila.append(i6)



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

if gen_h_base + picioare + blat > h_faianta_base:
    print("Verificare inaltime fainata jos: OK", "Suprapunere blat si faianta jos",
          gen_h_base + picioare + blat - h_faianta_base, "mm")
else:
    print("Verificare inaltime fainata jos: ERROR", "Distanta intre blat si faianta:",
          h_faianta_base - gen_h_base + picioare + blat, "mm")

print("Verificare distanta de la blat la corpurile suspendate (recomandare min. 600): ",
      h_bucatarie - gen_h_top - blat - gen_h_base - picioare, "mm")


