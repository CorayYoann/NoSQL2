import csv


csvfileread=open('station/rows.csv', "rt")
csvfilewrite=open('sub_entrance.csv', "w")
spamreader = csv.reader(csvfileread, delimiter=',', quotechar='|')
spamwriter = csv.writer(csvfilewrite, delimiter=',', quotechar='|')
l=0
for row in spamreader:
    if (l !=0) :
        coord = row[3].split('POINT (')[1].split(')')[0].split(' ')
        longit=coord[0]
        lattit=coord[1]
        nb_correspond=len(row[4].split("-"))
        ligne=[row[2],longit,lattit,nb_correspond,0]
        print (ligne)
        spamwriter.writerow(ligne)
    else :
        l = 1
        var = ['Street', 'Longitude', 'Lattitude', 'Nb_corr','Score']
        spamwriter.writerow(var)


# Mise en forme fichier sur pistes cyclables
csvfileread=open(dir+'bike_roads/rows.csv', "rt")
csvfilewrite=open(dir+'bike_roads.csv', "w")
spamreader = csv.reader(csvfileread, delimiter=',', quotechar='|')
spamwriter = csv.writer(csvfilewrite, delimiter=',', quotechar='|')
l=0
for row in spamreader:
    if (l !=0) :
        qualite = row[-2]
        if(qualite == ""):
            qualite = row[-1]
        if (qualite == "Greenway" or qualite == "Protected Path"):
            coord1 = row[2].split('LINESTRING (')[1].split(',')[0].split(' ')
            longit1=float(coord1[0])
            lattit1=float(coord1[1])
            coord2 = row[3].split(')')[0].split(' ')
            longit2=float(coord2[1])
            lattit2=float(coord2[2])
            longit=(longit1+longit2)/2
            lattit=(lattit1+lattit2)/2
            ligne=[longit,lattit,qualite]
            print (ligne)
            spamwriter.writerow(ligne)
    else :
        l = 1
        var = ['Longitude', 'Lattitude', 'Qualite']
        spamwriter.writerow(var)
