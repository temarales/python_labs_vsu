from Game.Unit import Unit
from Game.Color import  *

class Field(object):
    def __init__(self, size, color_count):
        self.__color_count = color_count
        self.__size = size
        self.array = []
        for i in range(size):
            __row = []
            for j in range(size):
                __row.append(Unit(color_count))
            self.array.append(__row)
        self.clear_field()

    def delete_line(self, row_begin, column_begin, row_end, column_end):
        if row_begin == row_end:
            for current_column in range(column_begin, column_end):
                self.array[row_begin][current_column].color = Color.NONE_COLOR
        else:
            for current_row in range(row_begin, row_end):
                self.array[current_row][column_begin].color = Color.NONE_COLOR

    def fill_emptinesses(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.array[i][j].what_color == Color.NONE_COLOR:
                    self.array[i][j] = Unit(self.__color_count)

    def move_elements(self, row_begin, column_begin, row_end, column_end): # падение элементов после удаления строки или столбца
        if row_begin == row_end:
            for current_row in reversed(range(1, row_end + 1)):
                for current_column in range(column_begin, column_end):
                    self.array[current_row][current_column].color = self.array[current_row - 1][current_column].color
            for current_column in range(column_begin, column_end):
                self.array[0][current_column].color = Color.NONE_COLOR
        else:
            if row_begin > row_end:
                for current_row in reversed(range(row_begin - row_end, row_begin)):
                    self.array[current_row][column_begin].color = self.array[current_row - (row_begin - row_end + 1)][column_begin].color
                for current_row in reversed(range(row_begin - row_end)):
                    self.array[current_row][column_begin].color = Color.NONE_COLOR
            else:
                for current_row in reversed(range(row_end - row_begin, row_end)):
                    self.array[current_row][column_begin].color = self.array[current_row - (row_end - row_begin + 1)][column_begin].color
                for current_row in reversed(range(row_end - row_begin)):
                    self.array[current_row][column_begin].color = Color.NONE_COLOR

    def change_positions(self, row1, column1, row2, column2):
        if (row1 == row2 or column1==column2):
            self.array[row1][column1], self.array[row2][column2] = self.array[row2][column2], self.array[row1][column1]
            if not self.is_nearby_similar(row1, column1, row2, column2):
                self.array[row1][column1], self.array[row2][column2] = self.array[row2][column2], self.array[row1][column1]

    def is_nearby_similar(self, row1, column1, row2, column2):
        i, j = self.check_vertical(column1)
        if not j == -1:
            return True
        i, j = self.check_vertical(column2)
        if not j == -1:
            return True
        i, j = self.check_horizontal(row1)
        if not j == -1:
            return True
        i, j = self.check_vertical(row2)
        if not j == -1:
            return True
        return False

    def check_vertical(self, column):
        count = 0
        row_begin = -1
        row_end = -1
        flag = False
        for i in range(self.__size - 1):
            if (self.array[i][column].what_color == self.array[i + 1][column].what_color):
                if not flag:
                    row_begin = i
                    flag = True
                count += 1
                if (i + 1 == self.__size - 1):
                    if flag:
                        if count >= 2:
                            row_end = i + 2
            else:
                if flag:
                    if count >= 2:
                        row_end = i + 1
                        break
                    flag = False
                    count = 0
                    row_begin = -1
        print("rows", row_begin, row_end)
        return row_begin, row_end

    def check_horizontal(self, row):
        count = 0
        column_begin = -1
        column_end = -1
        flag = False
        for i in range(self.__size - 1):
            if (self.array[row][i].what_color == self.array[row][i + 1].what_color): #and not i + 1 == self.__size - 1):
                if not flag:
                    column_begin = i
                    flag = True
                count += 1
                if (i + 1 == self.__size - 1):
                    if flag:
                        if count >= 2:
                            column_end = i + 2
            else:
                if flag:
                    if count >= 2:
                        column_end = i + 1
                        break
                    flag = False
                    count = 0
                    column_begin = -1
        print("columns", column_begin, column_end)
        return column_begin, column_end

    def clear_field(self):
        k = 0
        while (not k == self.__size * 2):
            k = 0
            for i in range(self.__size):
                column_begin, column_end = self.check_horizontal(i)
                if not column_end == -1:
                    self.delete_line(i, column_begin, i, column_end)
                    self.fill_emptinesses()
                else:
                    k += 1
            for i in range(self.__size):
                row_begin, row_end = self.check_vertical(i)
                if not row_end == -1:
                    self.delete_line(row_begin, i, row_end, i)
                    self.fill_emptinesses()
                else:
                    k += 1






