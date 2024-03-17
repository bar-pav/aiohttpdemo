from sqlalchemy import create_engine

from aiohttpdemo_polls.settings import config
from aiohttpdemo_polls.db import meta, question, choice


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'Question_1',
         'pub_date': '2024-03-03 00:00:00.001+03'}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Choice_1', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Choice_2', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Choice_3', 'votes': 0, 'question_id': 1},
    ])
    # conn.commit()
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
