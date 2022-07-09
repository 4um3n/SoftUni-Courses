class Area:
    def __init__(self, row, col, size, number):
        self.row = row
        self.col = col
        self.size = size
        self.number = number

    def __str__(self):
        return f"({self.row}, {self.col}), size: {self.size}"


class AreasFounder:
    def __init__(self, rows, cols, field, area_cls):
        self.rows = rows
        self.cols = cols
        self.field = field
        self.area_cls = area_cls
        self.areas = []

    def _get_area_size(self, row, col):
        def is_inbound():
            return 0 <= row < len(self.field) and 0 <= col < len(self.field[row])

        def is_wall():
            return self.field[row][col] == '*'

        def is_visited():
            return self.field[row][col] == 'v'

        if not is_inbound() or is_wall() or is_visited():
            return 0

        self.field[row][col] = 'v'
        size = 1
        size += self._get_area_size(row + 1, col)
        size += self._get_area_size(row - 1, col)
        size += self._get_area_size(row, col + 1)
        size += self._get_area_size(row, col - 1)
        return size

    def get_areas(self):
        for r in range(self.rows):
            for c in range(self.cols):
                size = self._get_area_size(r, c)
                if size > 0:
                    self.areas.append(self.area_cls(r, c, size, len(self.areas) + 1))

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
