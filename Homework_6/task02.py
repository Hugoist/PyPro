import uuid
from typing import Iterator


class UniqueIDIterator:
    """
    Iterator generates unique IDs based on UUID4
    """

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        return str(uuid.uuid4())


# test
ids = UniqueIDIterator()

for i, uid in zip(range(5), ids):  # print 5 unique IDs
    print(uid)
