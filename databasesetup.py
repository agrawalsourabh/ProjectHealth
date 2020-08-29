from project import db
from project.models import UserLogin

db.create_all()

user1 = UserLogin(empId='4532', password="123")

db.session.add(user1)

db.session.commit()

