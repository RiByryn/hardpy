from pathlib import Path

import rtoml

from hardpy.common.config import (
    ConfigManager,
    DatabaseConfig,
    FrontendConfig,
    HardpyConfig,
    SocketConfig,
)

db_no_default_user = "dev1"
db_no_default_password = "dev1"
db_no_default_host = "localhost1"
db_no_default_port = 5985

frontend_no_default_host = "localhost1"
frontend_no_default_port = 8001

socket_no_default_host = "localhost1"
socket_no_default_port = 6526


def test_config_manager_init(tmp_path: Path):
    tests_dir = tmp_path / "my_tests"
    ConfigManager.init_config(
        tests_dir=str(tests_dir),
        database_user=db_no_default_user,
        database_password=db_no_default_password,
        database_host=db_no_default_host,
        database_port=db_no_default_port,
        frontend_host=frontend_no_default_host,
        frontend_port=frontend_no_default_port,
        socket_host=socket_no_default_host,
        socket_port=socket_no_default_port,
    )
    config = ConfigManager.get_config()
    assert isinstance(config, HardpyConfig)
    assert config.tests_dir == str(tests_dir)
    assert config.database.user == db_no_default_user
    assert config.database.password == db_no_default_password
    assert config.database.host == db_no_default_host
    assert config.database.port == db_no_default_port
    assert config.frontend.host == "localhost1"
    assert config.frontend.port == 8001
    assert config.socket.host == "localhost1"
    assert config.socket.port == 6526


def test_database_config():
    config = DatabaseConfig()
    assert config.user == "dev"
    assert config.password == "dev"
    assert config.host == "localhost"
    assert config.port == 5984

    connection_url = config.connection_url()
    assert connection_url == "http://dev:dev@localhost:5984/"


def test_frontend_config():
    config = FrontendConfig()
    assert config.host == "localhost"
    assert config.port == 8000


def test_socket_config():
    config = SocketConfig()
    assert config.host == "localhost"
    assert config.port == 6525


def test_hardpy_config():
    config = HardpyConfig(
        title="HardPy TOML config",
        tests_dir="tests",
        database=DatabaseConfig(),
        frontend=FrontendConfig(),
        socket=SocketConfig(),
    )
    assert config.title == "HardPy TOML config"
    assert config.tests_dir == "tests"
    assert config.database.user == "dev"
    assert config.frontend.host == "localhost"
    assert config.socket.port == 6525


def test_config_manager_create_config(tmp_path: Path):
    tests_dir = tmp_path / "my_tests"
    Path.mkdir(tests_dir, exist_ok=True, parents=True)

    ConfigManager.init_config(
        tests_dir=str(tests_dir),
        database_user="dev",
        database_password="dev",
        database_host="localhost",
        database_port=5984,
        frontend_host="localhost",
        frontend_port=8000,
        socket_host="localhost",
        socket_port=6525,
    )

    ConfigManager.create_config(tests_dir)

    config_file: Path = tests_dir / "hardpy.toml"
    assert config_file.read_text() == rtoml.dumps(
        ConfigManager.get_config().model_dump(),
    )


def test_read_config_success(tmp_path: Path):
    test_config_data = {
        "title": "Test HardPy Config",
        "tests_dir": "my_tests",
        "database": {
            "user": "dev",
            "password": "dev",
            "host": "localhost",
            "port": 5984,
        },
        "frontend": {"host": "localhost", "port": 8000},
        "socket": {"host": "localhost", "port": 6525},
    }
    tests_dir = tmp_path / "tests"
    Path.mkdir(tests_dir, exist_ok=True, parents=True)
    with Path.open(tests_dir / "hardpy.toml", "w") as file:
        file.write(rtoml.dumps(test_config_data))

    config = ConfigManager.read_config(tests_dir)
    assert isinstance(config, HardpyConfig)
    assert config.title == test_config_data["title"]
    assert config.tests_dir == test_config_data["tests_dir"]
    assert config.database.user == test_config_data["database"]["user"]
