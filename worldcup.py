"""Module for World Cup things"""

import json
import requests


def get_team_details_by_id(team_id):
    """Gets a team's details by team ID

    Args:
        team_id (int): The team ID

    Returns:
        dict: Contains data related to id, name (long and short), country code,
                abbreviation, wins, losses, draws, and a picture URL
    """
    teamform = requests.get(
        f"https://api.fifa.com/api/v3/teamform/{team_id}",
        params={"count": 1, "language": "en"},
        timeout=3,
    )
    teamform_json = json.loads(teamform.content)
    return {
        "id": teamform_json["IdTeam"],
        "name": teamform_json["TeamName"][0]["Description"],
        "country_code": teamform_json["IdCountry"],
        "short_name": teamform_json["ShortClubName"],
        "abbreviation": teamform_json["Abbreviation"],
        "wins": teamform_json["Wins"],
        "losses": teamform_json["Losses"],
        "draws": teamform_json["Draws"],
        "picture_url": f"https://api.fifa.com/api/v3/picture/flags-sq-1/{teamform_json['Abbreviation']}",
    }


print(get_team_details_by_id(43935))
