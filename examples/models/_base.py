import typing as t

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flex_alchemy import ActiveRecord


class Base(DeclarativeBase, ActiveRecord):
    id: Mapped[int] = mapped_column(sa.BigInteger(), primary_key=True)

    def __repr__(self) -> str:
        """Returns representation of the object"""

        return "{name}({attrs})".format(
            name=self.__class__.__name__,
            attrs=", ".join(
                f"{attr}={getattr(self, attr)}" for attr in self.__repr_attrs__
            ),
        )
