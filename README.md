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
