
from datetime import datetime, timedelta, timezone
import secrets

from sqlalchemy.orm import Session

from app.models.session_tokens import Session_Token


DEFAULT_SESSION_TTL = timedelta(hours=24)
REMEMBERED_SESSION_TTL = timedelta(days=30)


def create_session(db: Session, user_id: int, remember: bool = False):
    session_id = secrets.token_urlsafe(32)
    ttl = REMEMBERED_SESSION_TTL if remember else DEFAULT_SESSION_TTL

    session_token = Session_Token(
        id=session_id,
        user_id=user_id,
        expires_at=datetime.now(timezone.utc) + ttl
    )

    db.add(session_token)
    db.commit()

    return session_token

def get_session_token_by_id(db: Session, id: str):
    return db.query(Session_Token).filter(Session_Token.id == id).first()