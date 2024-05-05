from controllers.menu_controllers import ApplicationController
from models import Base
from settings.database import engine
from controllers.role_controllers import RoleController
import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

sentry_sdk.init(
    dsn="https://a7122892fad60f7545036ec00dda215e@o4507205449023488.ingest.de.sentry.io/4507205471633488",
    enable_tracing=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    integrations=[SqlalchemyIntegration()]

)

Base.metadata.create_all(engine)

role_controller = RoleController()
role_controller.init_role_database()

app = ApplicationController()
app.start()
