# Typing Speed Leaderboard

A simple Python project that tracks typing speeds and maintains a leaderboard. This project exposes a **Model Context Protocol (MCP) server** that can be used with Claude Desktop to interact with the leaderboard.

---

## Features

- **Add scores:** Users can submit their typing speed (words per minute).  
- **View leaderboard:** Displays the top 10 scores.  
- **Check rank:** Users can see their current rank based on WPM.  
- **Persistent storage:** All scores are saved in a SQLite database so data is retained across sessions.  

---

## Technologies Used

- **Python** – main programming language  
- **FastAPI** – API backend  
- **FastMCP** – MCP server module  
- **SQLAlchemy** – ORM for interacting with SQLite  
- **Requests** – sending HTTP requests from MCP tools

## Claude Desktop MCP Configuration

Connecting an AI client to an MCP server is pretty easy. For claude, you edit the claude_desktop_config.json file and
some json that configures the MCP server with the client and runs the server on start up of the client. Here is the
configuration needed to connect to this MCP server:
```json
{
  "mcpServers": {
    "TypingLeaderboard": {
      "command": "Path/To/Your/Python/Executable",
      "args": ["Path/To/MCP Server File"]
    }
  }
}
```

The command argument is the file path to the python executable that is going to run the main.py file. If your using a
virtual environment, then it will be in the virtual environment folder, under scripts. 

The args argument is just the path to the main.py file that has your MCP server code in it. 

For me, I had to re-install claude every time I changed this configuration to get it to run automatically with the
updated version. If it's working correctly, you should be able to open claude and ask it to start using the tools. If 
it isn't working correctly, you will open claude and it will give you a red error message saying it failed to connect to
the MCP server. 