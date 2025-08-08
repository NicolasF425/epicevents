from views.login_view import LoginView
import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import os
from dotenv import load_dotenv


load_dotenv()  # Charge automatiquement le fichier .env

sentry_sdk.init(
    dsn=os.getenv("dsn"),
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    integrations=[SqlalchemyIntegration()],
    traces_sample_rate=1.0,  # Active la collecte de performance (1.0 = 100% des traces)
    send_default_pii=True,
)

login_view = LoginView()
login_view.display_view()
