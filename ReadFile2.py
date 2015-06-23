__author__ = 'Siuxoes'

import os, configparser

def carpetaRealeaseBuscar():
    carpetaReleases = carpetaLol+"\RADS\solutions\lol_game_client_sln\\releases"
    for file in os.listdir(carpetaReleases):
        return carpetaReleases + "\\" + file

letraDisco = os.getenv("SystemDrive")
carpetaLol = letraDisco+"\Riot Games\League of Legends"
carpetaRelease = carpetaRealeaseBuscar()
carpetaHUD = carpetaRelease + "\deploy\DATA\menu\hud"

def buscarArchiovHud():
    for file in os.listdir(carpetaHUD):
        if file.endswith(".ini"):
            return file

archiovHud = carpetaHUD+"\\"+buscarArchiovHud()


def buscarValorActualMiniMapScale():
    config = configparser.ConfigParser()
    config.read(archiovHud)
    minimapScale = config['Globals']['MinimapScale']
    print(minimapScale)
    return minimapScale


def setValorMiniMapScale(valor):
    config = configparser.ConfigParser()
    config.read(archiovHud)
    config.set('Globals', 'MinimapScale', '1.400')
    with open(archiovHud, 'w') as configfile:
        config.write(configfile)

if os.path.exists(carpetaLol):
    print("League of legends seems to be installed")
else:
    print ("League of Legends seems to not be installed")

print(carpetaHUD)
print(os.path.exists(carpetaHUD))
print(buscarArchiovHud())
print(archiovHud)
setValorMiniMapScale('1.300')