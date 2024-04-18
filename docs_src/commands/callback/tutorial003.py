import types


def callback():
    print("Running a command")


app = types.Types(callback=callback)


@app.callback()
def new_callback():
    print("Override callback, running a command")


@app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
