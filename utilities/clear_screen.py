import os


def clear_screen():
    ''' Fonction pour effacer l'écran'''
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
