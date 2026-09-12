

def driverIds(getData, year):

    specURL = f"f1/{year}/drivers"
    data = getData(specURL)

    data = data["DriverTable"]["Drivers"]

    arr = [
        """
    Name                      | Id
    ---------------------------------------"""
    ]

    for driver in data:
        if driver.get("url"): # will return none if the key parameter is not available
            name = driver["givenName"] + " " + driver["familyName"]
            driver_id = driver["driverId"]

            drLine = f"    {name:<25} | {driver_id:<10}"

            arr.append(drLine)  
        else:
            continue;
    arr.append("    Max Verstappen            | max_verstappen")
    
    print("\n".join(arr))
    print()