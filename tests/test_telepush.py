import os, sys, types
sys.modules.setdefault('requests', types.SimpleNamespace(get=lambda *a, **k: None))

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Telepush'))
import telepush
import reply


def test_chat_query():
    chat1 = telepush.Chat(window='#test', nick='test')
    assert chat1.query is True
    chat2 = telepush.Chat(window='#chan', nick='nick')
    assert chat2.query is False


def test_reply_consume():
    msg = {
        'chat': {'first_name': 'John', 'id': 1, 'last_name': 'Doe', 'type': 'private', 'username': 'johndoe'},
        'from': {'first_name': 'Jane', 'id': 2, 'is_bot': False, 'language_code': 'en', 'last_name': 'Smith', 'username': 'janesmith'},
        'date': 123456,
        'message_id': 7,
        'text': 'hello'
    }
    m = reply.consume(msg, 42)
    assert m.chat.id == 1
    assert m.user.username == 'janesmith'
    assert m.update_id == 42
    assert m.text == 'hello'
