import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from settings.setting import sentry

sentry_sdk.init(
    dsn=sentry,
    enable_tracing=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    integrations=[SqlalchemyIntegration()]
)