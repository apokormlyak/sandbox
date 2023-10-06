
def is_staff_only(func):
    def inner(user_id):
        print(f"User with user_id: {user_id}")
        #go to db
        if user_id == 1:
            result = func(user_id)
            return result
    return inner


@is_staff_only
def get_rights(user_id):
    return {"user_is": user_id,
            "access": "Accepted"}


if __name__ == '__main__':
    print(get_rights(5))
