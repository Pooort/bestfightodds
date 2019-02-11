from db import session, Fighters

for fighter in session.query(Fighters).all():
    surname = fighter.name.split(' ')[1]
    if surname[0] in ('A', 'B', 'C'):
        print(fighter.name)
