import os
import requests

BASE_URL = "https://opencricketapi.com/v1"

def get_headers():
    key = os.getenv("OPENCRICKET_API_KEY")

    if not key:
        raise ValueError("Cricket API key is missing")

    return {
        "Authorization": f"Bearer {key}",
        "Accept": "application/json"
    }


def get_recent_matches(competition=None, season=None):
    params = {}

    if competition:
        params["competition"] = competition

    if season:
        params["season"] = season

    response = requests.get(
        f"{BASE_URL}/matches",
        headers=get_headers(),
        params=params,
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def get_match_details(match_id):
    response = requests.get(
        f"{BASE_URL}/matches/{match_id}",
        headers=get_headers(),
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def get_scorecard(match_id):
    response = requests.get(
        f"{BASE_URL}/matches/{match_id}/scorecard",
        headers=get_headers(),
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def create_research_report(match_id):

    match = get_match_details(match_id)
    scorecard = get_scorecard(match_id)

    return {
        "match_id": match_id,
        "match_details": match,
        "scorecard": scorecard,
        "research_status": "completed",
        "source": "OpenCricket API"
    }