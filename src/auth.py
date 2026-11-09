users = {
    "admin": "admin123",
    "student": "student123"
}


def authenticate(username, password):
    if username in users and users[username] == password:
        return True

    return False