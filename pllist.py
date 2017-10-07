import plistlib

def findDuplicates(fileName):
    print('Wyszukiwanie zduplikowanych utworów w %s...' % fileName)
    #load playsit
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    trackNames = {}

    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']

            if name in trackNames:
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                trackNames[name] = (duration, 1)
        except:
            pass



    dups = []
    for k, v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1], k))
            
    if len(dups) > 0: 
        print("Znaleziono duplikatów %d. Nazwy utworów zostaly zapisane w pliku dup.txt" %len(dups))
    else: 
        print("Nie znaleziono zduplikowanych utworów!")
    
    f = open("dups.txt", "w")
    for val in dups:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()

pldir = input("Wprowadz adres pliku: ")

findDuplicates(pldir)