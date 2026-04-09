from __future__ import annotations

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine
from models import CampShift, Curator, News, ParticipationRequest, Question, User
from schemas import (
    CampShiftCreate,
    CampShiftRead,
    CuratorCreate,
    CuratorRead,
    NewsCreate,
    NewsRead,
    ParticipationRequestCreate,
    ParticipationRequestRead,
    QuestionCreate,
    QuestionRead,
    UserCreate,
    UserRead,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FP Backend API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/users", response_model=UserRead)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    entity = User(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@app.post("/requests", response_model=ParticipationRequestRead)
def create_participation_request(
    payload: ParticipationRequestCreate, db: Session = Depends(get_db)
) -> ParticipationRequest:
    entity = ParticipationRequest(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@app.post("/questions", response_model=QuestionRead)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)) -> Question:
    entity = Question(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@app.post("/shifts", response_model=CampShiftRead)
def create_shift(payload: CampShiftCreate, db: Session = Depends(get_db)) -> CampShift:
    entity = CampShift(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@app.post("/news", response_model=NewsRead)
def create_news(payload: NewsCreate, db: Session = Depends(get_db)) -> News:
    entity = News(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@app.post("/curators", response_model=CuratorRead)
def create_curator(payload: CuratorCreate, db: Session = Depends(get_db)) -> Curator:
    entity = Curator(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity