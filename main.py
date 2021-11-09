# Start
import matplotlib.pyplot as plt

# menu loop
m = 0
while (m == 0):
    m = 1
    # The Main Menu
    print('''
=======================================================
Welcome to the Soccer Player Management and Visualisation System
<A>dd details of a player.
<S>earch details for a player.
<V>isualize player details.
<Q>uit.
=======================================================
''')
    # Taking The input of ID
    inpu = input('Please select an option from the above:')
    # checking if it is an A
    if inpu == "A":
        # Add player loop
        a = 0
        while (a == 0):
            a = 1
            # take input of data
            pid = input('Please enter the player ID:')
            pname = input('Please enter the player name:')
            page = input('Please enter the age:')
            ph = input('Please enter the height:')
            pw = input('Please enter the weight:')
            # checking if they are in correct type of Data
            try:
                pid = int(pid)
                page = int(page)
                ph = int(ph)
                pw = float(pw)
                # reading the database
                lines = [line.rstrip('\n') for line in open("Players.txt")]
                # checking if the ID inputed dose already exist or not
                i = 1
                while len(lines) > i:
                    split = lines[i].split()
                    pid_split = int(split[0])
                    # if it dose exist already break it and go to the loop
                    if pid_split == pid:
                        print(
                            "Sorry the ID you enter already allocated for some other player, please try higher number eg.11001")
                        break
                    else:
                        i += 1
                # checking if data inputed are positive or negetive integer
                if pid > 0:
                    if page > 0:
                        if ph > 0:
                            if pw > 0:
                                if len(lines) == i:
                                    pid = str(pid).zfill(9)  # formating so it matches previous datas
                                    pname = '{:>33}'.format(
                                        pname)  # formating so it matches previous data and alingment
                                    print('''
  Thank You!

  The details of the player you entered are as follows:
  Player ID: ''', pid, '''
  Player name: ''', pname, '''
  Age: ''', page, '''
  Height: ''', ph, '''
  Weight: ''', pw, '''
  The record has been successfully added to the Players.txt file.''')

                                    outfile = open("Players.txt", 'a')
                                    outfile.write(
                                        "\n   {}{}           {}      {}         {}".format(pid, pname, page, ph,
                                                                                           pw))  # formating the input
                                    outfile.close()

                                    # 'Another Add player' loop
                                    AnotherAdd = 0
                                    while (AnotherAdd == 0):
                                        AnotherAdd = 1
                                        apyn = input('Do you want to enter details for another player (Y/N)?')
                                        if apyn == "Y":
                                            a = 0
                                        elif apyn == "N":
                                            m = 0
                                        else:
                                            print("Invalid Entry !")
                                            AnotherAdd = 0
                                else:
                                    a = 0
                            else:
                                print("INVALID!!!  Try again, Please Input an POSITIVE decimal number in Weight")
                                a = 0
                        else:
                            print("INVALID!!! Try again,  Please Input an POSITIVE integer in Hight ")
                            a = 0
                    else:
                        print("INVALID!!!  Try again, Please Input an POSITIVE integer in Age")
                        a = 0
                else:
                    print("INVALID!!!  Try again, Please Input an POSITIVE integer in ID")
                    a = 0

            except ValueError:
                print("INVALID!!!  Please Input an integer in ID,Age, Hight and Weight")
                a = 0
    # checking if it is an S
    elif inpu == "S":
        lines = [line.rstrip('\n') for line in open("Players.txt")]  # reading the database
        s = 0
        while (s == 0):
            s = 1
            wpid = input('''Please enter the player ID you want to search:''')  # take players ID
            try:  # checking if they are in correct type of Data
                z = int(wpid)
                i = 1
                wpid = int(wpid)
                while len(lines) > i:  # separating each ling
                    split = lines[i].split()  # separating each words of that line
                    pid_split = int(split[0])  # take the first word as ID
                    l = int(len(split))
                    # allocating the age hight and weight a arry list number
                    if pid_split == wpid:
                        ws = l - 1
                        hs = l - 2
                        ags = l - 3
                        i = 1
                        ns = " "
                        while (i < ags):
                            ns = ns + " " + split[i]  # taking first middle and last name (if they have)
                            i = i + 1

                        print('''
  Thank You!

  The details of the player you entered are as follows:
  Player ID: ''', split[0], '''
  Player name: ''', ns, '''
  Age: ''', split[ags], '''
  Height: ''', split[hs], '''
  Weight: ''', split[ws], '''
  ''')
                        break
                    else:
                        i += 1
                        if len(lines) == i:
                            print("Invalid Entry ! Number not found")
                            break
                # 'Another search player' loop
                AnotherS = 0
                while (AnotherS == 0):
                    AnotherS = 1
                    aps = input('Do you want to Search details for another player (Y/N)?')
                    if aps == "Y":
                        s = 0
                    elif aps == "N":
                        m = 0
                    else:
                        print("Invalid Entry !")
                        AnotherS = 0

            except ValueError:
                print("INVALID!!!  Please Input an integer")
                s = 0

    # checking if it is an V
    elif inpu == "V":
        v = 0
        while (v == 0):
            v = 1
            print('1. Age    2. Height    3. Weight ')
            vs = input('Please select the attribute you want to visualise(1/2/3):')  # take input
            try:  # checking if they are in correct type of Data
                vs = int(vs)
                if vs == 1:
                    dmax = 0
                    dmin = 500
                    lines = [line.rstrip('\n') for line in open("Players.txt")]  # reading the database
                    i = 1
                    x = []
                    while len(lines) > i:  # separating each ling
                        split = lines[i].split()  # separating each words of that line
                        age_split = int(split[0])  # take the first word as ID
                        l = (len(split))
                        vags = l - 3
                        age_split = int(split[vags])  # allocating the age arry list number
                        if age_split > dmax:  # finding the largest Age
                            dmax = age_split
                        if age_split < dmin:  # finding the lowest Age
                            dmin = age_split
                        x.append(age_split)
                        i = i + 1
                    x

                    bins = []
                    while dmin < (dmax + 1):  # allocating bins according to highest and lowest age
                        bins.append(dmin)
                        dmin = dmin + 1
                    bins

                    plt.hist(x, bins, histtype='bar', rwidth=1, color='g')

                    plt.xlabel('Years')
                    plt.ylabel('Probability ')
                    plt.title('Histogram of Age')

                    plt.show()  # showing the plot


                elif (vs == 2):
                    dmax = 0
                    dmin = 500

                    lines = [line.rstrip('\n') for line in open("Players.txt")]  # reading the database
                    i = 1
                    x = []
                    while len(lines) > i:  # separating each ling
                        split = lines[i].split()  # separating each words of that line
                        height_split = int(split[0])  # take the first word as ID
                        l = (len(split))
                        vh = l - 2
                        height_split = int(split[vh])  # allocating the age arry list number
                        if height_split > dmax:  # finding the largest Age
                            dmax = height_split
                        if height_split < dmin:  # finding the lowest Age
                            dmin = height_split
                        x.append(height_split)
                        i = i + 1
                    x

                    bins = []
                    while dmin < (dmax + 1):  # allocating bins according to highest and lowest age
                        bins.append(dmin)
                        dmin = dmin + 1
                    bins

                    plt.hist(x, bins, histtype='bar', rwidth=1, color='g')

                    plt.xlabel('Years')
                    plt.ylabel('Probability ')
                    plt.title('Histogram of Height')

                    plt.show()  # showing the plot

                elif (vs == 3):

                    dmax = 0
                    dmin = 500

                    lines = [line.rstrip('\n') for line in open("Players.txt")]  # reading the database
                    i = 1
                    x = []
                    while len(lines) > i:  # separating each ling
                        split = lines[i].split()  # separating each words of that line
                        weight_split = int(split[0])  # take the first word as ID
                        l = (len(split))
                        vw = l - 1
                        weight_split = float(split[vw])  # allocating the age arry list number
                        if weight_split > dmax:  # finding the largest Age
                            dmax = weight_split
                        if weight_split < dmin:  # finding the lowest Age
                            dmin = weight_split
                        x.append(weight_split)
                        i = i + 1
                    x

                    bins = []
                    while dmin < (dmax + 1):  # allocating bins according to highest and lowest age
                        bins.append(dmin)
                        dmin = dmin + 1
                    bins

                    plt.hist(x, bins, histtype='bar', rwidth=1, color='g')

                    plt.xlabel('Years')
                    plt.ylabel('Probability ')
                    plt.title('Histogram of Weight')

                    plt.show()  # showing the plot

                else:
                    print("Invalid Entry ! Please enter 1, 2 or 3")
                    v = 0

                # 'Another Plot' loop
                if v != 0:
                    AnotherV = 0
                    while (AnotherV == 0):
                        AnotherV = 1
                        apv = input('Do you want to visualize for another attribute (Y/N)?')
                        if apv == "Y":
                            v = 0
                        elif apv == "N":
                            m = 0
                        else:
                            print("Invalid Entry !")
                            AnotherV = 0

            except ValueError:
                print("INVALID!!!  Please Input an integer")
                v = 0
    # checking if it is an Q
    elif inpu == "Q":
        m = 1  # end the program
    else:
        print("Invalid Entry !")
        m = 0  # going back to the menu
