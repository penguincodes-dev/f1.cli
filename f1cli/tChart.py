    
    
    

def tChart(getData, year):
    print()

    specURL = f"f1/{year}/constructorstandings"
    data = getData(specURL)

    #chart has 35 spaces 
    arr = [
        "   Pos| Name              | Chart                                                       | Points",
        "   ----------------------------------------------------------------------------------------------",
    ]

    standings = data["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]

    maxPoints = float(standings[0]["points"])
    maxPoints += 20;
    pointsPerCharacter = round(maxPoints / 60);
    

    for team in standings:
        position = team["position"]
        name = team["Constructor"]["name"]
        points = int(team["points"])

        chart = int(round(points / pointsPerCharacter)) * "#" if points > 0 else " " 
        if pointsPerCharacter > points and points > 0:
            chart = "#"

        drLine = f"  {position:>3} | {name:<17} | {chart:<60} | {points:>6}"
        arr.append(drLine)

    print("\n".join(arr))

    print()