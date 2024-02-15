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
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("disable-quic")
        #chrome_options.add_experimental_option(
    #"excludeSwitches", ['enable-automation'])
        self.driver=webdriver.Chrome(service=service, options=chrome_options)
        #self.driver = webdriver.Chrome(os.getenv('DRIVER_PATH'), options=chrome_options)
        #self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
    def fTry(self, path, elementType = "xpath", debug = True, stop = 10):
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
                sleep(stop)

    def getMapsFromRank(self, maxMaps = 6):
        numMaps = 6
        maps_list = []
        mapName = []
        playRate = []
        atkWin = []
        defWin = []
        numMatches = []
        for i in range(1, numMaps + 1):
            '''mapName = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            playRate = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]').text
            atkWin = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[3]').text
            defWin = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]').text
            numMatches = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]').text'''
            mapName.append(self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[2]/a[1]/span[1]").text)
            playRate.append(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[3]/span[1]").text).strip('%'))/100.0)
            atkWin.append(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ "+ str(i) + "]/div[4]/p[1]").text).strip('%'))/100.0)
            defWin.append(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[ " + str(i) + "]/div[5]/p[1]").text).strip('%'))/100.)
            numMatches.append(int(float((self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[" + str(i) + "]/div[6]/span[1]").text).replace(',', ''))))
            #maps_list.append([mapName, playRate, atkWin, defWin, numMatches])
        map_data = {
            'Map': mapName,
            'playRate': playRate,
            'atkWin': atkWin,
            'defWin': defWin,
            'numMatches': numMatches
        }
        #maps_df = pd.DataFrame(maps_list, columns=["Map Name", "Play Rate", "Atk Win", "Def Win", "Num Matches"])
        #maps_df = pd.DataFrame(maps_list)
        maps_df = pd.DataFrame(map_data)
        return maps_df

    #def getMaps(self, maxMaps = 6, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"]):
    def getMaps(self, maxMaps = 6, modes = ["Competitive"]):
        maps_list = []

        # Iron 1 - tier #3
        # Immortal - tier #21
        # Radiant - tier #24

        for mode in modes:
            mode = (mode.lower()).replace(' ', '')
            print(f"Completing analysis of maps for mode {mode}...")
            if mode == "competitive":
                for i in range(17, 18):
                    print(f"Completing analysis of tier {i}...")
                    self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={i}')
                    sleep(1)
                    maps_df = self.getMapsFromRank()
                    self.driver.get(f'https://blitz.gg/valorant/stats/maps?sortBy=attackingRoundWinRate&sortDirection=DESC&mode=competitive&rank={0}')
                    maps_df.to_csv(f"map_data/maps_competitive_tier={i}.csv")
            '''else:
                self.driver.get(f'https://blitz.gg/valorant/stats/maps?map=all&act=e3act1&queue={mode}&rank=0')
                sleep(1)
                maps_df = self.getMapsFromRank()
                maps_df.to_csv(f"map_data/maps_{mode}_tier=0.csv")'''

    def getAgentsFromRank(self, maxAgents = 15):
        agents_list = []

        numAgents = 0
        for i in range(maxAgents, 1, -1):
            try:
                filler = self.driver.find_element_by_xpath(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[1]').text
                numAgents = i
                break
            except:
                pass

        for i in range(1, numAgents + 1):
            agentName = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            KD = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]').text
            KDA_text = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[3]').text
            winRate = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]').text
            pickRate = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]').text
            ACS = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[6]').text
            firstBlood = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[7]').text
            numMatches = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[8]').text
            kills = KDA_text[:KDA_text.index('/')-1]
            KDA_text = KDA_text[KDA_text.index('/')+2:]
            deaths = KDA_text[:KDA_text.index('/')-1]
            KDA_text = KDA_text[KDA_text.index('/')+2:]
            assists = KDA_text
            agents_list.append([agentName, KD, kills, deaths, assists, winRate, pickRate, ACS, firstBlood, numMatches])

        agents_df = pd.DataFrame(agents_list, columns=["Agent Name", "KD", "Kills", "Deaths", "Assists",
            "Win Rate", "Pick Rate", "ACS", "First Blood", "Num Matches"])
        return agents_df

    #def getAgents(self, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"], maps = ["All", "Bind", "Split",
            #"Ascent", "Haven", "Icebox", "Breeze"]):
    def getAgents(self, modes = ["Competitive"], maps = ["All", "Bind", "Split",
            "Ascent", "Haven", "Icebox", "Breeze"]):

        for mapName in maps:
            mapName = mapName.lower()
            print(f"Completing analysis of agents for map {mapName}.")
            for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of agents for mode {mode}.")

                if mode == "competitive":
                    for i in range(3, 22):
                        print(f"Completing analysis of tier {i}...")
                        self.driver.get(f'https://blitz.gg/valorant/stats/agents?sortBy=winRate&type=general&sortDirection=DESC&mode=competitive&rank={i}')
                        sleep(1)
                        agents_df = self.getAgentsFromRank()
                        agents_df.to_csv(f"agents_data/{mapName}/agents_competitive_tier={i}.csv")
                else:
                    self.driver.get(f'https://blitz.gg/valorant/stats/agents?map={mapName}&act=e3act1&queue={mode}&tier=0')
                    sleep(1)
                    agents_df = self.getAgentsFromRank()
                    agents_df.to_csv(f"agents_data/{mapName}/agents_{mode}_tier=0.csv")

    def getAbilitiesFromRank(self, maxAgents = 15):
        self.fTry('//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/button').click()
        self.fTry('/html/body/div[2]/div[3]/div/div[2]/div').click()

        abilities_list = []
        numAgents = 0
        for i in range(maxAgents, 1, -1):
            try:
                filler = self.driver.find_element_by_xpath(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[1]').text
                numAgents = i
                break
            except:
                pass

        for i in range(1, numAgents + 1):
            agentName = ab1 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            ab1 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]/div').text
            ab2 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[3]/div').text
            ab3 = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]/div').text
            ult = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]/div').text
            abilities_list.append([agentName, ab1, ab2, ab3, ult])

        abilities_df = pd.DataFrame(abilities_list, columns=["Agent Name", "Ability 1", "Ability 2", "Ability 3", "Ultimate"])
        return abilities_df

    def getAbilities(self, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"], maps = ["All"]):
        for mapName in maps:
            mapName = mapName.lower()
            print(f"Completing analysis of agents' abilities for map {mapName}.")
            for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of agents' abilities for mode {mode}.")

                if mode == "competitive":
                    for i in range(3, 22):
                        print(f"Completing analysis of tier {i}...")
                        self.driver.get(f'https://blitz.gg/valorant/stats/agents?map={mapName}&act=e3act1&queue=competitive&tier={i}')
                        sleep(1)
                        agents_df = self.getAbilitiesFromRank()
                        agents_df.to_csv(f"abilities_data/{mapName}/agents_competitive_tier={i}.csv")
            else:
                self.driver.get(f'https://blitz.gg/valorant/stats/agents?map={mapName}&act=e3act1&queue={mode}&tier=0')
                sleep(1)
                agents_df = self.getAbilitiesFromRank()
                agents_df.to_csv(f"abilities_data/{mapName}/agents_{mode}_tier=0.csv")

    def getWeaponsFromRank(self, maxWeapons = 17):
        numWeapons = 0
        for i in range(maxWeapons, 1, -1):
            try:
                filler = self.driver.find_element_by_xpath(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p').text
                numWeapons = i
                break
            except:
                pass

        weapons_list = []
        for i in range(1, numWeapons + 1):
            weaponName = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/div/p').text
            kills = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[2]').text
            headshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[4]').text
            bodyshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[5]').text
            legshot = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[6]').text
            damage = self.fTry(f'//*[@id="scroll-view-main"]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[{i}]/a/p[7]').text
            weapons_list.append([weaponName, kills, headshot, bodyshot, legshot, damage])

        weapons_df = pd.DataFrame(weapons_list, columns=["Weapon Name", "Kills Per Match", "Headshot", "Bodyshot", "Legshot", "Damage Per Round"])
        return weapons_df

    def getWeapons(self, modes = ["Competitive", "Unrated", "Spike Rush", "Custom"], maps = ["All", "Bind", "Split",
        "Ascent", "Haven", "Icebox", "Breeze"]):

        for mapName in maps:
            mapName = mapName.lower()
            print(f"Completing analysis of weapons for map {mapName}.")
            for mode in modes:
                mode = (mode.lower()).replace(' ', '')
                print(f"Completing analysis of weapons for mode {mode}.")

                if mode == "competitive":
                    for i in range(3, 22):
                        print(f"Completing analysis of tier {i}...")
                        self.driver.get(f'https://blitz.gg/valorant/stats/weapons?map={mapName}&act=e3act1&queue=competitive&tier={i}')
                        sleep(1)
                        agents_df = self.getWeaponsFromRank()
                        agents_df.to_csv(f"weapons_data/{mapName}/agents_competitive_tier={i}.csv")
                else:
                    self.driver.get(f'https://blitz.gg/valorant/stats/weapons?map={mapName}&act=e3act1&queue={mode}&tier=0')
                    sleep(1)
                    agents_df = self.getWeaponsFromRank()
                    agents_df.to_csv(f"weapons_data/{mapName}/agents_{mode}_tier=0.csv")

    def end(self):
        self.driver.quit()

bot = valorantBot()
#sleep(100)
bot.getMaps()
#bot.getAgents(maps=["All"])
#bot.getAbilities(maps=["All"])
#bot.getWeapons(maps=["All"])