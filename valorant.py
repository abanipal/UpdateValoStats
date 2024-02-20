from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import numpy as np
import time
import os
#from dotenv import load_dotenv
import pandas as pd

#load_dotenv()
g = ""
class valorantBot():
    def __init__(self):
        service = Service(executable_path='chromedriver.exe')
        #service = Service(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox')
        '''chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("disable-quic")
        chrome_options.add_argument("log-level=3")'''
        chrome_options.add_extension('bgnkhhnnamicmpeenaelnjfhikgbkllg.crx')
        #chrome_options.add_experimental_option(
    #"excludeSwitches", ['enable-automation'])
        self.driver=webdriver.Chrome(service=service, options=chrome_options)
        #self.driver = webdriver.Chrome(os.getenv('DRIVER_PATH'), options=chrome_options)
        #self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
    '''def fTry(self, path, elementType = "xpath", debug = True, stop = 10):
        # Force try function

        c = 1
        sleep(stop)
        while True:
            try:
                if elementType.lower() == "xpath":
                    pathOutput = self.driver.find_element_by_xpath(path)
                elif elementType.lower() == "class":
                    pathOutput = self.driver.find_element_by_class_name(path)
                else:
                    raise Exception("elementType variable must be defined differently.")
                return pathOutput
            except Exception as e:
                if debug:
                    print(f"Waiting... {c}; Error: {e}")
                c += 1
                sleep(stop)'''
    def fTry(self, path):
        print("IN ftry")
        # Force try function
        stop = 2
        c = 1
        #sleep(stop)
        while True:
            try:
                pathout= self.driver.find_element(By.XPATH, path)
                return pathout
            except Exception as e:
                print(f"Waiting... {c}; Error: {e}")
                c += 1
                sleep(stop)
    def getMapsFromRank(self, maxMaps = 6):
        numMaps = 6
        maps_list = []
        for i in range(1, numMaps + 1):
            '''mapName=(self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[2]/a[1]/span[1]").text)
            playRate=(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[3]/span[1]").text).strip('%'))/100.0)
            atkWin=(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ "+ str(i) + "]/div[4]/p[1]").text).strip('%'))/100.0)
            defWin=(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ " + str(i) + "]/div[5]/p[1]").text).strip('%'))/100.)
            numMatches=(int(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[6]/span[1]").text).replace(',', ''))))'''
            mapName=(self.fTry( "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[2]/a[1]/span[1]").text)
            playRate=(float((self.fTry( "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[3]/span[1]").text).strip('%'))/100.0)
            atkWin=(float((self.fTry( "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ "+ str(i) + "]/div[4]/p[1]").text).strip('%'))/100.0)
            defWin=(float((self.fTry("/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ " + str(i) + "]/div[5]/p[1]").text).strip('%'))/100.)
            numMatches=(int(float((self.fTry( "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[6]/span[1]").text).replace(',', ''))))
            maps_list.append([mapName, playRate, atkWin, defWin, numMatches])
        maps_df = pd.DataFrame(maps_list, columns=["Map Name", "Play Rate", "Atk Win", "Def Win", "Num Matches"])
        #maps_df = pd.DataFrame(maps_list)
        #maps_df = pd.DataFrame(map_data)
        return maps_df

    #def getMaps(self, maxMaps = 6, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"]):
    def getMaps(self, maxMaps = 6, modes = ["Competitive"]):
        maps_list = []

        # Iron 1 - tier #3
        # Immortal - tier #21
        # Radiant - tier #24
        tabSwitch = False
        for mode in modes:
            mode = (mode.lower()).replace(' ', '')
            print(f"Completing analysis of maps for mode {mode}...")
            if mode == "competitive":
                for i in range(3, 28):
                    print(f"Completing analysis of tier {i}...")
                    self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={i}')
                    idk = self.driver.window_handles
                    self.driver.switch_to.window(idk[0])
                    if tabSwitch == False:
                        sleep(10)
                        tabSwitch = True
                    else:
                        sleep(2)
                    maps_df = self.getMapsFromRank()
                    #self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={0}')
                    maps_df.to_csv(f"map_data/maps_competitive_tier={i}.csv")
            '''else:
                self.driver.get(f'https://blitz.gg/valorant/stats/maps?map=all&act=e3act1&queue={mode}&rank=0')
                sleep(1)
                maps_df = self.getMapsFromRank()
                maps_df.to_csv(f"map_data/maps_{mode}_tier=0.csv")'''

    def getAgentsFromRank(self):
        agents_list = []
        #sleep(2)
        maxAgents = 23
        numAgents = 0
        for i in range(1, maxAgents + 1):
            try:
                filler = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
                numAgents = i
                continue
            except:
                break
        for i in range(1, numAgents + 1):
           # print(i)
            '''agentName = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
            KD = self.driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[3]/span").text
            kills = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[1]").text
            deaths = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[3]").text
            assists = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[5]").text
            winRate = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[5]/p").text
            pickRate = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[6]/span").text
            ACS = self.driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[7]/p").text
            #firstBlood = self.driver.find_element(By.XPATH, "").text'''
            agentName = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
            KD = self.fTry("/html/body/main/div/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[3]/span").text
            kills = self.fTry( "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[1]").text
            deaths = self.fTry( "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[3]").text
            assists = self.fTry( "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span[5]").text
            winRate = self.fTry( "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[5]/p").text
            pickRate = self.fTry( "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[6]/span").text
            ACS = self.fTry( "/html/body/main/div/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[7]/p").text
            #firstBlood = self.driver.find_element(By.XPATH, "").text
            numMatches = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[8]/span").text
            #agents_list.append([agentName, KD, kills, deaths, assists, winRate, pickRate, ACS, firstBlood, numMatches])
            agents_list.append([agentName, KD, kills, deaths, assists, winRate, pickRate, ACS, numMatches])

        #agents_df = pd.DataFrame(agents_list, columns=["Agent Name", "KD", "Kills", "Deaths", "Assists",
          #  "Win Rate", "Pick Rate", "ACS", "First Blood", "Num Matches"])
        agents_df = pd.DataFrame(agents_list, columns=["Agent Name", "KD", "Kills", "Deaths", "Assists",
            "Win Rate", "Pick Rate", "ACS", "Num Matches"])
        return agents_df

    #def getAgents(self, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"], maps = ["All", "Bind", "Split",
            #"Ascent", "Haven", "Icebox", "Breeze"]):
    def getAgents(self, modes = ["Competitive"], maps = [ "Breeze", "Bind", "Lotus", "Sunset"]):
        #maps = ["All", "Split", "Ascent", "Icebox", "Breeze", "Bind", "Lotus", "Sunset"]
        tabSwitch = False
        for mapName in maps:
           
            mapName = mapName.lower()
            print(f"Completing analysis of agents for map {mapName}.")
            ''' for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of agents for mode {mode}.")

                if mode == "competitive":'''
            for i in range(3, 28):
                print(f"Completing analysis of tier {i}...")
                #self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={0}')
                self.driver.get(f'https://blitz.gg/valorant/stats/agents?sortBy=winRate&type=general&sortDirection=DESC&mode=competitive&rank={i}&map={mapName}')
                idk = self.driver.window_handles
                self.driver.switch_to.window(idk[0])
                if tabSwitch == False:
                    sleep(10)
                    tabSwitch = True
                else:
                    sleep(2)
                agents_df = self.getAgentsFromRank()
                #self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={0}')
                agents_df.to_csv(f"agents_data/{mapName}/agents_competitive_tier={i}.csv")
                '''else:
                    self.driver.get(f'https://blitz.gg/valorant/stats/agents?map={mapName}&act=e3act1&queue={mode}&tier=0')
                    sleep(1)
                    agents_df = self.getAgentsFromRank()
                    agents_df.to_csv(f"agents_data/{mapName}/agents_{mode}_tier=0.csv")'''

    def getAbilitiesFromRank(self, maxAgents = 23):
        #self.fTry('//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/button').click()
        #self.fTry('/html/body/div[2]/div[3]/div/div[2]/div').click()

        abilities_list = []
        numAgents = 0
        for i in range(1, maxAgents + 1):
            try:
                filler = self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span').text
                numAgents = i
                continue
            except:
                break

        for i in range(1, numAgents + 1):
           print(i)
           ''' agentName = ab1 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            ab1 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]/div').text
            ab2 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[3]/div').text
            ab3 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]/div').text
            ult = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]/div').text
            abilities_list.append([agentName, ab1, ab2, ab3, ult])'''
           agentName = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
           ab1 = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[3]/div/span").text
           ab2 = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[4]/div/span").text
           ab3 = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[5]/div/span").text
           ult = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[6]/div/span").text
           abilities_list.append([agentName, ab1, ab2, ab3, ult])

        abilities_df = pd.DataFrame(abilities_list, columns=["Agent Name", "Ability 1", "Ability 2", "Ability 3", "Ultimate"])
        return abilities_df

    def getAbilities(self, modes = ["Competitive"], maps = ["All", "Split", "Ascent", "Icebox", "Breeze", "Bind", "Lotus", "Sunset"]):
        #maps = ["All", "Split", "Ascent", "Icebox", "Breeze", "Bind", "Lotus", "Sunset"]
        tabSwitch = False
        for mapName in maps:
            mapName = mapName.lower()
            print(f"Completing analysis of agents' abilities for map {mapName}.")
            for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of agents' abilities for mode {mode}.")
#https://blitz.gg/valorant/stats/agents?map=Lotus&act=e3act1&queue=competitive&rank=16
                for i in range(3, 28):
                    loop = True
                    print(f"Completing analysis of tier {i}...")
                    #while(loop == True):
                        #try:
                    self.driver.get(f'https://blitz.gg/valorant/stats/agents?sortBy=winRate&type=abilities&sortDirection=DESC&mode=competitive&rank={i}&map={mapName}')
                    idk = self.driver.window_handles
                    self.driver.switch_to.window(idk[0])
                           # loop = False
                        #except:
                           # loop = True
                    if tabSwitch == False:
                        sleep(10)
                        tabSwitch = True
                    else:
                        sleep(2)
                    agents_df = self.getAbilitiesFromRank()
                    agents_df.to_csv(f"abilities_data/{mapName}/agents_competitive_tier={i}.csv")
            '''else:
                self.driver.get(f'https://blitz.gg/valorant/stats/agents?map={mapName}&act=e3act1&queue={mode}&tier=0')
                sleep(1)
                agents_df = self.getAbilitiesFromRank()
                agents_df.to_csv(f"abilities_data/{mapName}/agents_{mode}_tier=0.csv")'''

    def getWeaponsFromRank(self, maxWeapons = 18):
        numWeapons = 0
        for i in range(1, maxWeapons+1):
            try:
                filler = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
                numWeapons = i
                continue
            except:
                break

        weapons_list = []
        for i in range(1, numWeapons + 1):
            print(i)
            '''weaponName = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            kills = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]').text
            headshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]').text
            bodyshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]').text
            legshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[6]').text
            damage = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[7]').text'''
            weaponName = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[2]/a/span").text
            kills = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[3]/span").text
            headshot = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[5]/span").text
            bodyshot = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[6]/span").text
            legshot = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[7]/span").text
            damage = self.fTry("/html/body/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/div[" + str(i) + "]/div[8]/p").text
            weapons_list.append([weaponName, kills, headshot, bodyshot, legshot, damage])

        weapons_df = pd.DataFrame(weapons_list, columns=["Weapon Name", "Kills Per Match", "Headshot", "Bodyshot", "Legshot", "Damage Per Round"])
        return weapons_df

    def getWeapons(self, modes = ["Competitive"], maps = ["All", "Split", "Ascent", "Icebox", "Breeze", "Bind", "Lotus", "Sunset"]):
        tabSwitch = False
        for mapName in maps:
            mapName = mapName.lower()
            print(f"Completing analysis of weapons for map {mapName}.")
            for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of weapons for mode {mode}.")

                if mode == "competitive":
                    for i in range(3, 28):
                        print(f"Completing analysis of tier {i}...")
                        self.driver.get(f'https://blitz.gg/valorant/stats/weapons?sortBy=avgDamage&type=all&sortDirection=DESC&mode=competitive&rank={i}&map={mapName}')
                        idk = self.driver.window_handles
                        self.driver.switch_to.window(idk[0])
                        if tabSwitch == False:
                            sleep(10)
                            tabSwitch = True
                        else:
                            sleep(2)
                        agents_df = self.getWeaponsFromRank()
                        agents_df.to_csv(f"weapons_data/{mapName}/agents_competitive_tier={i}.csv")
    def end(self):
        self.driver.quit()

bot = valorantBot()
#sleep(100)
#bot.getMaps()
bot.getAgents()
#bot.getAbilities()
#bot.getWeapons()