

import time
from datetime import datetime

def lastRace (getData):
    specURL = f"f1/current/last/results/"
    data = getData(specURL)
    data = data["RaceTable"]
    race_round = data["round"]
    data = data["Races"][0]

    race_name = data["raceName"]
    circuit_name = data["Circuit"]["circuitName"]
    race_country = data["Circuit"]["Location"]["country"]
    
    race_date = data["date"]
    date = race_date.replace("-", " ")
    date = date.split()
    
    race_date = f"{date[2]} {datetime.strptime(date[1], '%m').strftime('%B')} {date[0]}"

    arr = [

    ]

    main_content = f"""
    {race_name}
    {race_date} R{race_round}
    {circuit_name}. {race_country}\n
    Pos| Name                      | Time          | Points 
    -------------------------------------------------------"""
    arr.append(main_content)
    
    results = data["Results"]

    max_laps = results[0]["laps"]

    for driver in results:
        position = driver["position"]
        points = driver["points"] if float(driver["points"]) > 0 else 0 
        name = driver["Driver"]["givenName"] + " " + driver["Driver"]["familyName"]
        time = ""
        if driver["laps"] == max_laps:
            time = driver["Time"]["time"]
        else:
            if driver["status"] == "Finished" or driver["status"] == "Lapped":
                if (int(driver["laps"]) + 1) == max_laps:
                    time = f"+{int(max_laps) - int(driver["laps"])} lap"
                else:
                    time = f"+{int(max_laps) - int(driver["laps"])} laps"
            else:
                time = "DNF"

        drLine = f"   {position:>3} | {name:<25} | {time:>13} | {points:>3}"

        arr.append(drLine);
    
    print("\n".join(arr))
    print()
