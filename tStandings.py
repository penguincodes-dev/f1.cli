


def tStandings(getData, year):
    print()
    specURL = f"f1/{year}/constructorstandings"
    data = getData(specURL)

    arr = [
        "  Pos | Name              | Country    | Points",
        "  ---------------------------------------------"
    ]

    standings = data["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]

    for team in standings:
        position = team["position"]
        name = team["Constructor"]["name"]
        country = team["Constructor"]["nationality"]
        points = team["points"]

        drLine = f"  {position:>3} | {name:<17} | {country:<10} | {points:>6}"
        arr.append(drLine)

    print("\n".join(arr))


    print()