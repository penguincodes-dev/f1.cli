

import requests
import textwrap

def wiki(target):
    wikiUrl = target["url"]
    wikiPage = wikiUrl.split("/wiki/")[1]

    # Create the URL for Wikipedia's API.
    # wikiPage contains something like "Max_Verstappen"
    wikiUrl = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wikiPage}"


    # Tell Wikipedia what program is making the request.
    # The User-Agent identifies your application.

    headers = {
        "User-Agent": "F1CLI/1.0 (your-email@example.com)"
    }


    # Send a GET request to the Wikipedia API.
    # wikiUrl = where we're sending the request
    # headers = extra information we're sending with the request
    responseWiki = requests.get(
        wikiUrl,
        headers=headers
    )

    responseWiki.raise_for_status()

    dataWiki = responseWiki.json()

    description = dataWiki["extract"]

    description = textwrap.fill(
        description,
        width=70
    )

    return description