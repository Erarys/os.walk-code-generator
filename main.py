import os
from collections.abc import Iterable
from typing import Tuple


class Walk:

    def __init__(self, path: Iterable[str]):
        self.pathMain = path
        self.next = self.nextPath()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.next)

    def nextPath(self) -> Tuple[str]:
        for path in self.pathMain:
            folders = []
            files = []
            try:
                for elem in os.listdir(path):
                    underPath = os.path.join(path, elem)
                    if os.path.isdir(underPath):
                        folders.append(elem)
                    elif os.path.isfile(underPath):
                        files.append(elem)
            except PermissionError:
                pass

            yield path, folders, files

            if folders:
                yield from Walk(iter([os.path.join(path, folder) for folder in folders])).nextPath()


path = os.path.abspath("..")


main = Walk(iter([path]))

for i in main:
    print(i)