
def dStandings(getData, year):
    print()
    specURL = f"f1/{year}/driverstandings"
    data = getData(specURL)

    arr = [
        "  Pos | Name                     | Team              | Points",
        "  -----------------------------------------------------------"
    ]

    standings = data["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    for driver in standings:
        position = driver["position"]
        name = driver["Driver"]["givenName"] + " " + driver["Driver"]["familyName"]
        team = driver["Constructors"][0]["name"]
        points = driver["points"]

        drLine = f"  {position:>3} | {name:<24} | {team:<17} | {points:>6}"
        arr.append(drLine)

    print("\n".join(arr))
    print()
