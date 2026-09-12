import requests
import os
from datetime import datetime

from .dStandings import dStandings
from .tStandings import tStandings
from .tChart import tChart
from .dChart import dChart
from .lastRace import lastRace
from .nextRace import nextRace
from .driverIds import driverIds
from .teamIds import teamIds
from .dInfo import dInfo
from .tInfo import tInfo
from .helpFunc import helpFunc

def getData(specURL):
    try:
        baseURL = "https://api.jolpi.ca/ergast/f1"
        targetURL = baseURL + str(specURL)

        response = requests.get(targetURL)
        response.raise_for_status()

        data = response.json()
        return data["MRData"]

    except Exception as e:
        print(f"An error occurred: {e}")

def print_banner():
    print("""
         ______________  ___
        /  ___________/ /  /
       /  / _________  /  /
      /  / /  ______/ /  /
     /__/ /__/       /__/

    F1 command-line interface
    
    help - to reveal the commands""")
    print()

def main():
    year = datetime.now().year

    print_banner()

    try:
        while True:
            user_input = input("f1 > ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]

            match command:
                case "dStandings":
                    dStandings(getData, year)

                case "tStandings":
                    tStandings(getData, year)

                case "tChart":
                    tChart(getData, year)

                case "dChart":
                    dChart(getData, year)

                case "lastRace":
                    lastRace(getData)

                case "nextRace":
                    nextRace(getData)

                case "driverIds":
                    driverIds(getData, year)

                case "teamIds":
                    teamIds(getData, year)

                case "dInfo":
                    if len(parts) < 2:
                        print("Usage: dInfo <driver>")
                        continue

                    dInfo(getData, parts[1])

                case "tInfo":
                    if len(parts) < 2:
                        print("Usage: tInfo <team>")
                        continue

                    tInfo(getData, parts[1])

                case "help":
                    helpFunc()

                case "exit":
                    print("Exiting the program")
                    break

                case "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                    print_banner()

                case _:
                    print("Unknown command")
                    print("Type 'help' to see all commands")

    except KeyboardInterrupt:
        print("\nExiting the program")
