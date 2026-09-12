

import time
from datetime import datetime
from datetime import datetime

def nextRace(getData):
    specURL = f"/current/next/"
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
    {circuit_name}. {race_country}\n"""

    arr.append(main_content)

    sessions = []

    if "FirstPractice" in data:
        sessions.append(("FP1", data["FirstPractice"]))

    if "SecondPractice" in data:
        sessions.append(("FP2", data["SecondPractice"]))

    if "ThirdPractice" in data:
        sessions.append(("FP3", data["ThirdPractice"]))

    if "SprintQualifying" in data:
        sessions.append(("Sprint Qualifying", data["SprintQualifying"]))

    if "Sprint" in data:
        sessions.append(("Sprint", data["Sprint"]))

    if "Qualifying" in data:
        sessions.append(("Qualifying", data["Qualifying"]))

    for session in sessions:
        session_date = session[1]["date"]
        session_time = session[1]["time"]

        formatted_date = datetime.strptime(
            session_date,
            "%Y-%m-%d"
        ).strftime("%d %B %Y")

        formatted_time = session_time[:5]

        line = f"""
    {session[0]}
    {formatted_date} {formatted_time}
    """
        arr.append(line)

    print("\n".join(arr))
    print()