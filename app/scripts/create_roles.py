from app.app import create_app
from app.model.role import Role
from app.extensions.database import db

app = create_app()
app.app_context().push()

roles_data = [{"name": "view"}, {"name": "edit"}, {"name": "dev"}]

for role in roles_data:
    new_role = Role(name=role["name"])
    db.session.add(new_role)

db.session.commit()
