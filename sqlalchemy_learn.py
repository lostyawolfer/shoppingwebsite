from typing import Optional
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

engine = create_engine('sqlite:///./test.db')
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Database(Base):
    __tablename__ = 'testing_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)

Base.metadata.create_all(bind=engine)

def create_user(username: str, email: str) -> Optional[Database]:
    session = sessionlocal()

    try:
        a = session.query(Database).filter_by(email=email).first()
        if a:
            print(f'user: {email} already exists')
            return None
        newuser = Database(username=username, email=email)
        session.add(newuser)
        session.commit()
        print(f'user: {username}; email: {email}; registered successfully')
        return newuser

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()



def session_gen():
    db = sessionlocal()
    try:
        yield db

    finally:
        db.close()


if __name__ == '__main__':
    create_user('lostyawolfer', 'lostyawolfer123@gmail.com')