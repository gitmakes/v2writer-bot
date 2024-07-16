from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Manager(Base):
    __tablename__ = "managers"
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    data: Mapped[str] = mapped_column(String)


class Note(Base):
    __tablename__ = "notes"
    name: Mapped[str] = mapped_column(String, primary_key=True)
    urls: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String, default="")
    user_id: Mapped[int] = mapped_column(BigInteger)

    def __repr__(self) -> str:
        obj = dict(
            name=self.name,
            urls=self.urls.splitlines(),
            content=self.content,
            user_id=self.user_id,
        )
        return str(obj)


class BotOptions(Base):
    __tablename__ = "bot_options"
    name: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        obj = dict(name=self.name, value=self.value)
        return str(obj)
