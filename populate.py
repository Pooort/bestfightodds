from db import Events, session, Fighters
from network import get_content
from parser import parse

content = get_content()
data = parse(content)
event = session.query(Events).filter(Events.name == data['name']).one_or_none()
if event is None:
    event = Events(**{'name': data['name'], 'date': data['date']})
    session.add(event)
    session.flush()
    for fighter_name in data['fighters_names']:
        fighter = Fighters(name=fighter_name, event_id=event.id)
        session.add(fighter)
    session.commit()
