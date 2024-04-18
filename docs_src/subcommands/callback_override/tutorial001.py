import types

app = types.Types()

users_app = types.Types()
app.add_types(users_app, name="users")


@users_app.callback()
def users_callback():
    print("Running a users command")


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
