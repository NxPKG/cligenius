import types


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise types.Exit(code=1)
    print(f"New user created: {username}")


if __name__ == "__main__":
    types.run(main)
