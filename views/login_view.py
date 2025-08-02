import getpass
from utilities.clear_screen import clear_screen
from controlers.login_controler import LoginControler


class LoginView:

    login_controler = LoginControler()

    def display_view(self):
        clear_screen()
        login = input("login: ")
        password = getpass.getpass("password: ")

        self.login_controler.check_credentials(login, password)
