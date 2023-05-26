from library import create_app

if __name__ == "__main__":
    app = create_app()

    app.run(
        debug=True,
        port=app.config["PORT"],
        host=app.config["HOST"]
    )