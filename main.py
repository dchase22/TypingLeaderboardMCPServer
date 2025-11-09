import requests
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("DChase Typing Test")

BASE_URL = "http://127.0.0.1:8000"


@mcp.tool()
def add_score(username: str, a_wpm: float):
    """
    Send a new score to the API.

    Args:
        username (str): username for leaderboard
        a_wpm (float): typing speed of the user

    Returns:
        str: A response telling you the score was added or the error if the score wasn't added
    """
    payload = {"username": username, "wpm": a_wpm}
    response = requests.post(f"{BASE_URL}/score", json=payload)
    if response.status_code == 200:
        return f"Added score for {username}: {a_wpm} WPM"
    else:
        return f"Error adding score: {response.text}"


@mcp.tool()
def show_leaderboard():
    """
    This tool will retrieve the leaderboard from the database and return it formatted as in the example below

    Ex:
    Leaderboard (Top 10):
    1. dchase - 80.0 WPM
    2. dchase - 80.0 WPM
    3. alima - 80.0 WPM
    4. croy - 60.0 WPM
    5. croy - 60.0 WPM

    if there is an error in fetching the leaderboard from the database, it returns a string saying that

    """
    response = requests.get(f"{BASE_URL}/leaderboard")
    if response.status_code == 200:
        leaderboard = response.json()["leaderboard"]
        result = "\nLeaderboard (Top 10):\n"
        for i, entry in enumerate(leaderboard, 1):
            result += f"{i}. {entry['username']} - {entry['wpm']} WPM\n"
        return result
    else:
        return "Could not fetch leaderboard."


@mcp.tool()
def get_rank(username: str):
    """
    This tool checks the rank for a given user

    Args:
        username (str): username to be looked up

    Returns:
        The specified username and their corresponding rank
    """
    response = requests.get(f"{BASE_URL}/rank/{username}")
    if response.status_code == 200:
        data = response.json()
        return f"\n{data['username']}'s rank: #{data['rank']} ({data['wpm']} WPM)"
    else:
        return f"{response.json()['detail']}"


if __name__ == "__main__":
    mcp.run(transport='stdio')
