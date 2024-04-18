import types

app = types.Types()


def old_callback():
    """
    Old callback help.
    """


users_app = types.Types(callback=old_callback)
app.add_types(users_app)


@users_app.callback()
def users():
    """
    Manage users in the app.
    """


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
