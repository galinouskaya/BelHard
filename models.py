from sqlalchemy import Column, INT, VARCHAR, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)

class Product(Base):
    __tablename__ = 'products'
    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

engine = create_engine('postgresql://postgres:q1w2e3r4t5y6@localhost:5433/bh35d')
Session = sessionmaker(bind=engine)


from csv import DictReader

with open('categories.csv', 'r', encoding='utf-8') as file:
    reader = DictReader(file)


    with Session() as session:
        for category in reader:
            cat = Category(**category)
            session.add(cat)
            session.commit()


    # cat = Category(name='Drinks')
    # session.add(cat)
    # session.commit()
    # session.refresh(cat)
    # print(cat.name)
    # print(cat.id)
