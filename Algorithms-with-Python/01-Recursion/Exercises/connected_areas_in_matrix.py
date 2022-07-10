class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

    def __str__(self):
        return f"({self.row}, {self.col}), size: {self.size}"


class AreasFounder:
    def __init__(self, rows, cols, field, area_cls):
        self.rows = rows
        self.cols = cols
        self.field = field
        self.area_cls = area_cls
        self.areas = []

    def __is_inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def __is_wall(self, row, col):
        return self.field[row][col] == '*'

    def __is_visited(self, row, col):
        return self.field[row][col] == 'v'

    def _get_area_size(self, row, col):
        if not self.__is_inbound(row, col) \
                or self.__is_wall(row, col) \
                or self.__is_visited(row, col):
            return 0

        self.field[row][col] = 'v'

        size = 1
        size += self._get_area_size(row + 1, col)
        size += self._get_area_size(row - 1, col)
        size += self._get_area_size(row, col + 1)
        size += self._get_area_size(row, col - 1)
        return size

    def get_areas(self):
        for row in range(self.rows):
            for col in range(self.cols):
                size = self._get_area_size(row, col)
                if size > 0:
                    self.areas.append(self.area_cls(row, col, size))

        return self.areas

    def __str__(self):
        message = [f"Total areas found: {len(self.areas)}"]

        for ind, area in enumerate(sorted(self.areas, key=lambda a: (-a.size, a.row, a.col))):
            message.append(f"Area #{ind + 1} at {str(area)}")

        return '\n'.join(message)


def main():
    rows = int(input())
    cols = int(input())
    field = [list(input()) for _ in range(rows)]
    founder = AreasFounder(rows, cols, field, Area)
    founder.get_areas()
    print(founder)


if __name__ == '__main__':
    main()
