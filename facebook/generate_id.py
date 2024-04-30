import random
import string

def generate_id(prefix, length=10):
    # Génère une chaîne de caractères aléatoire de longueur spécifiée
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    # Ajoute le préfixe à la chaîne aléatoire pour former l'identifiant
    return prefix + "_" + random_string

def generate_user_id():
    return generate_id("user")

def generate_page_id():
    return generate_id("page")

def generate_group_id():
    return generate_id("group")

def generate_event_id():
    return generate_id("event")

# Exemples d'utilisation
print("User ID:", generate_user_id())
print("Page ID:", generate_page_id())
print("Group ID:", generate_group_id())
print("Event ID:", generate_event_id())