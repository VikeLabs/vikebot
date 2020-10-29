from sqlalchemy import Column, Integer, String, BOOLEAN, engine


class Data:
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    verified = Column(BOOLEAN)
    email = Column(String)
    verify_code = Column(String)


def __repr__(self):
    return "<User(id='%s', verified='%s', email='%s')>" % (
    self.id, self.verified, self.email)