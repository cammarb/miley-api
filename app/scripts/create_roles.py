from app.app import create_app
from app.model.role import Role
from app.extensions.database import db

app = create_app()
app.app_context().push()

roles_data = {1: {"name": "view"}, 2: {"name": "edit"}, 3: {"name": "dev"}}

for id, role in roles_data.items():
    new_role = Role(id=id, name=role["name"])
    db.session.add(new_role)

db.session.commit()
