
import time
from datetime import datetime
from .wiki import wiki

def tInfo(getData, teamId):
    try:

        specURL = f"/constructors/{teamId}"
        data = getData(specURL)

        data = data["ConstructorTable"]
        team = data["Constructors"][0]

        name = team["name"]
        nationality = team["nationality"]

        description = wiki(team)
 
        arr = [
                        "",
                        f"    {name}",
                        "",
                        f"    Nationality: {nationality}",
                        "",
                        "    Description:",
                        "",
                    ]

        for line in description.splitlines():
            arr.append(f"    {line}")

        arr.append("")

        print("\n".join(arr))
 
    except IndexError:
        print()
        print("   You did not type the team ID")
        print("   Use the command below to see the team IDs:")
        print("   teamIds")
        print()