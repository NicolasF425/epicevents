from views.login_view import LoginView
import sentry_sdk


sentry_sdk.init(
    dsn="https://709ac84f126afba33f99a2c28a17ae1b@o4509790547148800.ingest.de.sentry.io/4509790549901392",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

login_view = LoginView()
login_view.display_view()
