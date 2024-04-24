from controllers.menu_controllers import ApplicationController
from models import Base
from config import engine


Base.metadata.create_all(engine)

app = ApplicationController()
app.start()
