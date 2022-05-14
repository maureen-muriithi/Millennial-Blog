from app import Create_app
from flask_script import Manager, Server

app = Create_app('development')


manager = Manager(app)


manager.add_command('run',Server(use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app = app)


if __name__ == "__main__":
    manager.run()
