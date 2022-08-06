from flaskblog import db, bcrypt, create_app
from flaskblog.models import User

while True:
    command = input('1. Add\n2. Delete\n3. Cancel\n')
    if command == '1':
        username = input('Username: ')
        password = input('Password: ')

        with create_app().app_context():
            user = User.query.filter_by(username=username).first()
            if user:
                print('User already exists.')
            else:
                user_to_add = User(username=username, password=bcrypt.generate_password_hash(password).decode('utf-8'))
                db.session.add(user_to_add)
                db.session.commit()
                print("Successfully added new Administrator!")
        break
        
    elif command=='2':
        username = input('Username: ')
        
        with create_app().app_context():
            user = User.query.filter_by(username=username).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                print("Successfully deleted Administrator!")
            else:
                print('No user by that name exists.')
        break
    elif command=='3':
        break
