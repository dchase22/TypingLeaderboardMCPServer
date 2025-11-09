from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# ------------------------
# Database setup
# ------------------------
DATABASE_URL = "sqlite:///./leaderboard.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# ------------------------
# Database model
# ------------------------
class ScoreDB(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    wpm = Column(Float)


Base.metadata.create_all(bind=engine)


# ------------------------
# Pydantic model
# ------------------------
class Score(BaseModel):
    username: str
    wpm: float


# ------------------------
# Routes
# ------------------------
@app.get("/")
def home():
    return {"message": "Welcome to the Persistent Typing Speed Leaderboard API!"}


@app.post("/score")
def add_score(score: Score):
    db = SessionLocal()
    new_score = ScoreDB(username=score.username, wpm=score.wpm)
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    db.close()
    return {"message": f"Score added for {score.username}!", "score": {"wpm": score.wpm}}


@app.get("/leaderboard")
def get_leaderboard():
    db = SessionLocal()
    scores = db.query(ScoreDB).order_by(ScoreDB.wpm.desc()).limit(10).all()
    db.close()
    return {"leaderboard": [{"username": s.username, "wpm": s.wpm} for s in scores]}


@app.get("/rank/{username}")
def get_rank(username: str):
    db = SessionLocal()
    user = db.query(ScoreDB).filter(ScoreDB.username == username).first()
    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    higher_scores = db.query(ScoreDB).filter(ScoreDB.wpm > user.wpm).count()
    rank = higher_scores + 1
    db.close()
    return {"username": username, "rank": rank, "wpm": user.wpm}
