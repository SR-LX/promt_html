from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
import datetime

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 数据库模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=True)
    points = Column(Integer, default=0)
    is_admin = Column(Integer, default=0)  # 0: 普通用户, 1: 管理员
    articles = relationship("Article", back_populates="author")

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(128), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")

# 创建表
Base.metadata.create_all(bind=engine)

# FastAPI 应用
app = FastAPI(title="博客与MCP服务平台API", description="基于FastAPI和SQLite的后端服务", version="0.1.0")

# 依赖项

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 示例路由
@app.get("/")
def read_root():
    return {"msg": "Hello, FastAPI!"}

# 获取所有用户（示例）
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# 获取所有文章（示例）
@app.get("/articles/")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles 