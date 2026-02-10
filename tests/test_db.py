from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):

    with mock_db_time(model=User) as time:
        dados = {"username": "Alice", "password": "secret", "email": "teste@teste.com"}

        new_user = User(**dados)
        session.add(new_user)  # Adiciona o objeto a sessão, mas ainda é transiente, ou seja, não foi persistido ainda
        # breakpoint()
        session.commit()

        user = session.scalar(select(User).where(User.username == "Alice"))  # O método scalar pega um registro no banco e transforma em objeto, no caso um objeto User

    assert asdict(user) == {
        "id": 1,
        "username": "Alice",
        "password": "secret",
        "email": "teste@teste.com",
        "update_at": time,
        "created_at": time,
    }


# def test_update_user(session, mock_db_updateTime):

#     with mock_db_updateTime(model=User) as uptime:
#         dados = {"username": "Alice", "password": "secret", "email": "teste@teste.com"}

#         new_user = User(**dados)
#         session.add(new_user)  # Adiciona o objeto a sessão, mas ainda é transiente, ou seja, não foi persistido ainda
#         # breakpoint()
#         session.commit()

#         user = session.scalar(select(User).where(User.username == "Alice"))  # O método scalar pega um registro no banco e transforma em objeto, no caso um objeto User
#         # breakpoint()
#     assert asdict(user) == {
#         "id": 1,
#         "username": "Alice",
#         "password": "secret",
#         "email": "teste@teste.com",
#         "update_at": uptime,
#         "created_at": user.created_at,
#     }
