import plistlib

def findCommonTracks(fileNames):
    """
    Wyszukiwanie wspólnych utworów w danych plikach list odtwarzania 
    i zapisywanie ich w pliku common.txt.
    """    
    # lista zbiorów nazw utworów
    trackNameSets = []
    for fileName in fileNames:
        # tworzenie nowego zbioru
        trackNames = set()
        # wczytywanie listy odtwarzania
        plist = plistlib.readPlist(fileName)
        # pobieranie utworów
        tracks = plist['Tracks']
        # iterowanie przez utwory
        for trackId, track in tracks.items():
            try:
                # dodawanie nazwy do zbioru
                trackNames.add(track['Name'])
            except:
                # ignorowanie
                pass
        # dodawanie do listy
        trackNameSets.append(trackNames)    
    # pobieranie zbioru wspólnych utworów
    commonTracks = set.intersection(*trackNameSets)
    # zapisywanie w pliku
    if len(commonTracks) > 0:
        f = open("common.txt", 'wb')
        for val in commonTracks:
            s = "%s\n" % val
            f.write(s.encode("UTF-8"))
        f.close()
        print("Znaleziono wspólnych utworów %d. "
              "Nazwy utworów zostaly zapisane w pliku common.txt." % len(commonTracks))
    else:
        print("Nie ma żadnych wspólnych utworów!")





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

# pldir = input("Wprowadz adres pliku: ")
# findDuplicates(pldir)


lists = ['test-data/pl1.xml', 'test-data/pl2.xml']

findCommonTracks(lists)