
import time
from wiki import wiki 
from datetime import datetime

def dInfo(getData, driverId):
    try:

        specURL = f"/drivers/{driverId}"
        data = getData(specURL)

        data = data["DriverTable"]
        driver = data["Drivers"][0]

        name = driver["givenName"] + " " + driver["familyName"]

        dateBirth = driver["dateOfBirth"]
        dateBirth = datetime.strptime(
            dateBirth,
            "%Y-%m-%d"
        ).strftime("%d %B %Y")

        nationality = driver["nationality"]
        permanent_number = driver["permanentNumber"]

        description = wiki(driver)

        # Display information
        arr = [
            "",
            f"    {name}",
            "",
            f"    Birthday: {dateBirth}",
            f"    Nationality: {nationality}",
            f"    Number: {permanent_number}",
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
        print("   You did not type the driver ID\n   Use the command bellow to see the driver id:\n   driverIds")
        print()