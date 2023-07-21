from Account.models import User

"""
check if any fields is empty
if empty return true
"""
def isEmpty(*args):
    for item in args:
        if not item:
            return True
    return False


def checkEmailExists(email):
    user = User.objects.filter(email= email)
    if user:
        return True
    return False