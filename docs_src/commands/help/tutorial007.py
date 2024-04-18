from typing import Union

import types

app = types.Types(rich_markup_mode="rich")


@app.command()
def create(
    username: str = types.Argument(..., help="The username to create"),
    lastname: str = types.Argument(
        "", help="The last name of the new user", rich_help_panel="Secondary Arguments"
    ),
    force: bool = types.Option(False, help="Force the creation of the user"),
    age: Union[int, None] = types.Option(
        None, help="The age of the new user", rich_help_panel="Additional Data"
    ),
    favorite_color: Union[str, None] = types.Option(
        None,
        help="The favorite color of the new user",
        rich_help_panel="Additional Data",
    ),
):
    """
    [green]Create[/green] a new user. :sparkles:
    """
    print(f"Creating user: {username}")


@app.command(rich_help_panel="Utils and Configs")
def config(configuration: str):
    """
    [blue]Configure[/blue] the system. :wrench:
    """
    print(f"Configuring the system with: {configuration}")


if __name__ == "__main__":
    app()
