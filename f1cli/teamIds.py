

def teamIds(getData, year):
    specURL = f"f1/{year}/constructors/"
    
    data = getData(specURL)
    
    data = data["ConstructorTable"]["Constructors"]

    arr = [
        """
    Name                      | Id
    ---------------------------------------"""
    ]

    for team in data:
        name = team["name"]
        team_id = team["constructorId"]

        tmLine = f"    {name:<25} | {team_id:<10}"
        arr.append(tmLine)

    print("\n".join(arr))
    print()