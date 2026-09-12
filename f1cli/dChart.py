def dChart(getData, year):

    print()

    specURL = f"f1/{year}/driverstandings"

    data = getData(specURL)

    arr = [
        "   Pos| Name              | Chart                                                     | Points",
        "   ----------------------------------------------------------------------------------------------",
    ]

    standings = data["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    maxPoints = float(standings[0]["points"])
    maxPoints += 20

    pointsPerCharacter = round(maxPoints / 50)

    for driver in standings:

        position = driver["position"]

        firstName = driver["Driver"]["givenName"]
        lastName = driver["Driver"]["familyName"]
        name = f"{firstName} {lastName}"

        points = int(driver["points"])

        chart = int(round(points / pointsPerCharacter)) * "#" if points > 0 else " "

        if pointsPerCharacter > points and points > 0:
            chart = "#"

        drLine = f"  {position:>3} | {name:<24} | {chart:<50} | {points:>6}"

        arr.append(drLine)

    print("\n".join(arr))

    print()