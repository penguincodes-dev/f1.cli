

def helpFunc():
    print("""
    F1 CLI - Available Commands
    ============================

    CHAMPIONSHIP
      dStandings       Show current driver championship standings
      tStandings       Show current constructor championship standings
      dChart           Show driver standings with a points chart
      tChart           Show constructor standings with a points chart

    RACES
      nextRace         Show the next race and session schedule
      lastRace         Show the results of the most recent race

    DRIVER & TEAM INFO
      driverIds        List all available driver IDs
      teamIds          List all available team IDs
      dInfo <driver>   Show driver information and Wikipedia description
      tInfo <team>     Show team information and Wikipedia description

    GENERAL
      help             Show this help menu
      clear            Clear the terminal
      exit             Exit the F1 CLI
      Ctrl+C           Exit the F1 CLI

    TIP
      Use driverIds or teamIds to find the ID needed by dInfo/tInfo.
    """)