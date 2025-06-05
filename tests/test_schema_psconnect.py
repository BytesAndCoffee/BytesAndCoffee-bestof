import os, sys, types
from datetime import datetime

# Provide stubs for external packages
pymysql_stub = types.ModuleType('pymysql')
pymysql_stub.Connection = object
pymysql_stub.MySQLError = Exception
pymysql_stub.connect = lambda *a, **k: None
cursors_stub = types.ModuleType('cursors')
cursors_stub.DictCursor = object
pymysql_stub.cursors = cursors_stub
sys.modules.setdefault('pymysql', pymysql_stub)
sys.modules.setdefault('pymysql.cursors', cursors_stub)

dotenv_stub = types.ModuleType('dotenv')
dotenv_stub.load_dotenv = lambda *a, **k: None
sys.modules.setdefault('dotenv', dotenv_stub)

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'zlog_parsing'))
import schema
import psconnect


def test_convert_type():
    assert schema.convert_type('int') is int
    assert schema.convert_type('varchar') is str
    assert schema.convert_type('unknown') == 'Any'


def test_validate_schema_success():
    row = {
        'created_at': datetime.now(),
        'id': 1,
        'message': 'msg',
        'network': 'net',
        'nick': 'nick',
        'type': 'msg',
        'user': 'user',
        'window': 'win'
    }
    assert psconnect.validate_schema(row, 'logs') is True


def test_validate_schema_failure_missing_column():
    row = {'id': 1}
    assert psconnect.validate_schema(row, 'logs') is False
