from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)  # Init - Indica que o parâmetro id não deve ser passado na requisição
    username: Mapped[str] = mapped_column(unique=True)  # Unique - Indica que o username não poderá ser repetido
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    update_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())  # server_default=func.now() diz que, quando a classe for instanciada,
    # o resultado de func.now() será o valor atribuído a esse atributo. No caso, a data e hora em que ele foi instanciado.
