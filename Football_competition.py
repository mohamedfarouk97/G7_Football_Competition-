from easygui import *
import random
import sys
beginIMG = "./images/beginIMG.gif"
winnerIMG = "./images/winnerIMG.gif"
groupA = ["Napoli", "Liverpool", "Ajax", "Rangers"]
groupB = ["porto", "Brugge", "Leverkusen", "Atletico"]
groupC = ["B.Munich", "inter", "Barcelona", "Plzen"]
groupD = ["Tottenham", "Frankfurt", "Sporting Lisbon", "Marseille"]
groupE = ["Chelsea", "Milan", "Salzburg", "Dinamo Zagreb"]
groupF = ["Real Madrid", "Leipzig", "Shakhtar", "Celtic"]
groupG = ["Man City", "Dortmund", "Sevilla", "Copenhagen"]
groupH = ["Benfica Lisbon", "PSG", "Juventus", "Maccabi Haifa"]
def QuarterFinals():
    global quarterone, quartertow, quarterthree, quarterfour, quarterfive, quartersix, quarterseven, quartereight
    msg = (
        "Quarter-Finals\n\n\n"
        + str(quarterone)
        + str(" VS ")
        + str(quartertow)
        + str("\n\n")
        + str(quarterthree)
        + str(" VS ")
        + str(quarterfour)
        + str("\n\n")
        + str(quarterfive)
        + str(" VS ")
        + str(quartersix)
        + str("\n\n")
        + str(quarterseven)
        + str(" VS ")
        + str(quartereight)
    )
    choices = ["Semi-finals"]
    reply = buttonbox(msg, choices=choices)
    if reply == "Semi-finals":
        semiFinals()
    else:
        sys.exit(0)
def winners():
    global winner
    winner = winner[0]
    msg = "                           The winner is " + str(winner)
    choices = ["OK"]
    reply = buttonbox(msg, image='./images/begin.jpeg', choices=choices)
    if reply == "OK":
        sys.exit(0)
    else:
        sys.exit(0)
def finals():
    global   win1final, win2final
    msg = "Final\n\n\n" + str(win1final) + str(" VS ") + str(win2final)
    choices = ["Winner"]
    reply = buttonbox(msg, choices=choices)
    if reply == "Winner":
        winners()
    else:
        sys.exit(0)
def semiFinals():
    global  semi1win, semi2win, semi3win, semi4win
    msg = (
        "Semi-Finals\n\n\n"
        + str(semi1win)
        + str(" VS ")
        + str(semi2win)
        + str("\n")
        + str(semi3win)
        + str(" VS ")
        + str(semi4win)
    )
    choices = ["Finals"]
    reply = buttonbox(msg, choices=choices)
    if reply == "Finals":
        finals()
    else:
        sys.exit(0)
pointes=[{'Napoli':15,'Liverpool':15,'Ajax':6,'Rangers':0},
         {'porto':12,'Brugge':11,'Leverkusen':5,'Atletico':5},
         {'B.Munich':18,'inter':10,'Barcelona':7,'Plzen':0},
         {'Tottenham':11,'Frankfurt':10,'Sporting Lisbon':7,'Marseille':6},
         {'Chelsea':13,'Milan':10,'Salzburg':6,'Dinamo Zagreb':4},
         {'Real Madrid':13,'Leipzig':12,'Salzburg':6,'Celtic':2},
         {'Man City':14,'Dortmund':9,'Sevilla':5,'Copenhagen':3},
         {'Benfica Lisbon':14,'PSG':14,'Juventus':3,'Maccabi Haifa':3}]
Winerrone=[]
Winerronetow=[]
def qulfiction(pointes):
    global  Winerrone
    global Winerronetow
    for i in pointes:
        res = {key: val for key, val in sorted(i.items(), key=lambda ele: ele[1], reverse=True)}
        # print(list(res.keys())[0])
        win1 = list(res.keys())[0]
        win2 = list(res.keys())[1]
        Winerrone.append(win1)
        Winerronetow.append(win2)
    return Winerrone, Winerronetow
one,tow=qulfiction(pointes)
#print("group one",one)
def result (team1,team2,score1,score2):
    if score1>score2:
        return team1
    else:
        return team2
def roundOf16():
    global quarterone, quartertow, \
        quarterthree, quarterfour, quarterfive, quartersix, quarterseven, quartereight \
        , semi1win, semi2win, semi3win, semi4win, win1final, win2final, winner
    List2 = ['1:3'
        , '4:0'
        , '2:1'
        , '3:2'
        , '4:0'
        , '5:3'
        , '0:3'
        , '4:1']
    List = ['Liverpool vs porto',
            'Brugge vs Napoli',
            'inter vs Tottenham',
            'Frankfurt vs B.Munich',
            'Milan vs Real Madrid',
            'Chelsea vs Leipzig',
            'ManCity vs PSG',
            'BenficaLisbon vs Dortmund',
            ]
    one, tow = qulfiction(pointes)
    wins=[]
    for i in range(len(List2)):
        res_teamone = (List2[i][0])
        res_teamtow = (List2[i][2])
        team = List[i].split(" ")
        # print(List[i][0],":",List[i][2])
        win = result(team[0], team[2], res_teamone, res_teamtow)
        wins.append(win)
    A1 = one[0]
    A2 = tow[0]
    B1 = one[1]
    B2 = tow[1]
    C1 = one[2]
    C2 = tow[2]
    D1 = one[3]
    D2 = tow[3]
    E1 = one[4]
    E2 = tow[4]
    F1 = one[5]
    F2 = tow[5]
    G1= one[6]
    G2 = tow[6]
    H1= one[7]
    H2= tow[7]
    quarterone = wins[0]
    quartertow = wins[1]
    quarterthree = wins[2]
    quarterfour = wins[3]
    quarterfive = wins[4]
    quartersix = wins[5]
    quarterseven = wins[6]
    quartereight = wins[7]
    List2 = ['1:3',
             '2:1'
        , '3:2'
        , '4:0']
    List = ['porto vs Brugge',
            'inter vs Frankfurt',
            'Milan vs Chelsea',
            'PSG vs BenficaLisbon'
            ]
    winsof_sime = []
    for i in range(len(List2)):
        res_teamone = (List2[i][0])
        res_teamtow = (List2[i][2])
        team = List[i].split(" ")
        win = result(team[0], team[2], res_teamone, res_teamtow)
        winsof_sime.append(win)
    semi1win = winsof_sime[0]
    semi2win = winsof_sime[1]
    semi3win = winsof_sime[2]
    semi4win = winsof_sime[3]
    List2 = ['1:0',
             '5:1']
    List = ['porto vs inter',
            'Milan vs PSG',]
    winsof_for_final = []
    for i in range(len(List2)):
        res_teamone = (List2[i][0])
        res_teamtow = (List2[i][2])
        team = List[i].split(" ")
        # print(List[i][0],":",List[i][2])
        win = result(team[0], team[2], res_teamone, res_teamtow)
        winsof_for_final.append(win)
    final1full = [semi1win, semi2win]
    final2full = [semi3win, semi4win]
    win1final = winsof_for_final[0]
    win2final = winsof_for_final[1]
    List2 = ['0:2']
    List = ['porto vs Milan']
    winner = []
    for i in range(len(List2)):
        res_teamone = (List2[i][0])
        res_teamtow = (List2[i][2])
        team = List[i].split(" ")
        win = result(team[0], team[2], res_teamone, res_teamtow)
        winner.append(win)
    msg = (
        "Round of 16\n\n\n"
        + str("A1 ")
        + str(A1)
        + str(" VS ")
        + str("B2 ")
        + str(B2)
        + str("\n\nB1 ")
        + str(B1)
        + str(" VS ")
        + str("A2 ")
        + str(A2)
        + str("\n\nC1 ")
        + str(C1)
        + str(" VS ")
        + str("D2 ")
        + str(D2)
        + str("\n\nD1 ")
        + str(D1)
        + str(" VS ")
        + str("C2 ")
        + str(C2)
        + str("\n\nE1 ")
        + str(E1)
        + str(" VS ")
        + str("F2 ")
        + str(F2)
        + str("\n\nF1 ")
        + str(F1)
        + str(" VS ")
        + str("C2 ")
        + str(E2)
        + str("\n\nG1 ")
        + str(G1)
        + str(" VS ")
        + str("H2 ")
        + str(H2)
        + str("\n\nH1 ")
        + str(H1)
        + str(" VS ")
        + str("G2 ")
        + str(G2)
    )
    choices = ["Quarter-finals"]
    reply = buttonbox(msg, choices=choices)
    if reply == "Quarter-finals":
        QuarterFinals()
    else:
        sys.exit(0)
def begin():
    msg = (

        "This is all Champions League Groups\n\n\n"
        + str("Group A\n")
        + str(
            (groupA[0])
            + str(", ")
            + str(groupA[1])
            + str(", ")
            + str(groupA[2])
            + str(", ")
            + str(groupA[3])
        )
        + str("\n\nGroup B\n")
        + str(
            (groupB[0])
            + str(", ")
            + str(groupB[1])
            + str(", ")
            + str(groupB[2])
            + str(", ")
            + str(groupB[3])
        )
        + str("\n\nGroup C\n")
        + str(
            (groupC[0])
            + str(", ")
            + str(groupC[1])
            + str(", ")
            + str(groupC[2])
            + str(", ")
            + str(groupC[3])
        )
        + str("\n\nGroup D\n")
        + str(
            (groupD[0])
            + str(", ")
            + str(groupD[1])
            + str(", ")
            + str(groupD[2])
            + str(", ")
            + str(groupD[3])
        )
        + str("\n\nGroup E\n")
        + str(
            (groupE[0])
            + str(", ")
            + str(groupE[1])
            + str(", ")
            + str(groupE[2])
            + str(", ")
            + str(groupE[3])
        )
        + str("\n\nGroup F\n")
        + str(
            (groupF[0])
            + str(", ")
            + str(groupF[1])
            + str(", ")
            + str(groupF[2])
            + str(", ")
            + str(groupF[3])
        )
        + str("\n\nGroup G\n")
        + str(
            (groupG[0])
            + str(", ")
            + str(groupG[1])
            + str(", ")
            + str(groupG[2])
            + str(", ")
            + str(groupG[3])
        )
        + str("\n\nGroup H\n")
        + str(
            (groupH[0])
            + str(", ")
            + str(groupH[1])
            + str(", ")
            + str(groupH[2])
            + str(", ")
            + str(groupH[3])
        )
    )
    choices = ["Champions League"]
    reply = buttonbox(msg, image='./images/begin.jpeg', choices=choices)
    if reply == "Champions League":
        roundOf16()
    elif reply == "./images/begin.jpeg":
        roundOf16()
    else:
        sys.exit(0)
begin()
