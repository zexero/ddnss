from dataclasses import dataclass

from app.exts import db
from datetime import datetime


# 记录实体类型
@dataclass
class Record(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(50), primary_key=True)
    host = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    ip = db.Column(db.String(100))
    key = db.Column(db.String(50))
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)