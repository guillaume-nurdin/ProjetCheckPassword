# password_checker.py

def check_length(password):
    """
    Vérifie si le mot de passe a une longueur minimale de 8 caractères.
    """
    return len(password) >= 8


def check_characters(password):
    """
    Vérifie si le mot de passe contient :
    - Au moins une majuscule.
    - Au moins un chiffre.
    - Au moins un caractère spécial.
    """
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=" for char in password)
    return has_upper and has_digit and has_special


def check_common_passwords(password, common_passwords_file):
    """
    Vérifie si le mot de passe est présent dans une liste de mots de passe communs.
    """
    try:
        with open(common_passwords_file, 'r', encoding='utf-8', errors='ignore') as file:
            common_passwords = file.read().splitlines()
        return password in common_passwords
    except FileNotFoundError:
        print(f"Erreur : Le fichier {common_passwords_file} est introuvable.")
        return False


def is_password_strong(password, common_passwords_file):
    """
    Vérifie la force du mot de passe en combinant les critères.
    """
    if not check_length(password):
        return "Mot de passe trop court. Utilisez au moins 8 caractères."
    if not check_characters(password):
        return "Mot de passe faible. Ajoutez une majuscule, un chiffre, et un caractère spécial."
    if check_common_passwords(password, common_passwords_file):
        return "Mot de passe trop commun. Choisissez un mot de passe plus original."
    return "Mot de passe fort !"


if __name__ == "__main__":
    # Chemin vers le fichier rockyou.txt
    common_passwords_file = "rockyou.txt"
    
    print("Bienvenue dans le vérificateur de mot de passe !")
    password = input("Entrez un mot de passe à vérifier : ")
    
    # Vérification de la force du mot de passe
    result = is_password_strong(password, common_passwords_file)
    print(result)
