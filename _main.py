import math
import sys
sys.path.append('/repo_mcmct')


print("""
 __       __                  __       __           ________ 
/  \     /  |                /  \     /  |         /        |
$$  \   /$$ |  _______       $$  \   /$$ |  _______$$$$$$$$/ 
$$$  \ /$$$ | /       |      $$$  \ /$$$ | /       |  $$ |   
$$$$  /$$$$ |/$$$$$$$/       $$$$  /$$$$ |/$$$$$$$/   $$ |   
$$ $$ $$/$$ |$$ |            $$ $$ $$/$$ |$$ |        $$ |   
$$ |$$$/ $$ |$$ \_____       $$ |$$$/ $$ |$$ \_____   $$ |   
$$ | $/  $$ |$$       |      $$ | $/  $$ |$$       |  $$ |   
$$/      $$/  $$$$$$$/       $$/      $$/  $$$$$$$/   $$/    
                                                             
                                                             
                                                             
""")
1
nullswitch = False
hello = "Willkommen im McMcT Projekt"
funcList = ["Funktionen", "Dreiecks-Geometrie",
            "Vektorberechnung", "Währungsrechner", "Stop"]

print(
    '''
    1 - ''' + funcList[0] + '''
    2 - ''' + funcList[1] + '''
    3 - ''' + funcList[2] + '''
    4 - ''' + funcList[3] + '''
    5 - ''' + funcList[4] + '''
    
    
    '''

)


# Auswahl
while True:
    operation = int(
        input("Bitte wählen Sie eine Funktion(1-5) des McMcT-Taschenrechners aus:  "))

    match operation:

        case 1:
            print("Viel Spass mit " + funcList[0])
            import functions as fun

        case 2:
            print("Viel Spass mit " + funcList[1])
            import triangle as tri

        case 3:
            print("Viel Spass mit " + funcList[2])
            import vector as vec

        case 4:
            print("Viel Spass mit " + funcList[3])
            import currency as cur

        case 5:
            break

        case _:
            print(
                "Sie haben ein falsches Zeichen eingegeben....lernen Sie bitte ordentlich tippen...sorry :)")

if (nullswitch == True):
    print("Der McMcT ist aufgrund dieser inakzeptablen Operation explodiert - Kawuuum!")
else:
    print("Danke für die kompetente Verwendung unseres McMcT :) Beehren Sie uns bald wieder!")

# Berechnung mit ende beenden wollen, oder ob sie mit start eine neue Rechnung starten wollen.
