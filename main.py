from controllers.menu_controllers import ApplicationController
from models import Base
from settings.database import engine
from controllers.role_controllers import RoleController

Base.metadata.create_all(engine)

role_controller = RoleController()
role_controller.init_role_database()

app = ApplicationController()
app.start()
