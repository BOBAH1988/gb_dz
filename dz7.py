#1
# class Matrix:
#     def __init__(self, my_list):
#         self.my_list = my_list
#     def __str__(self):
#         for row in self.my_list:
#             for i in row:
#                 print(f"{i:4}", end="")
#             print()
#         return ''
#     def __add__(self, other):
#         for i in range(len(self.my_list)):
#             for i_2 in range(len(other.my_list[i])):
#                 self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
#         return Matrix.__str__(self)
# m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
# new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
# print(m.__add__(new_m))
# print('>' * 50)

#2
# class Textil:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#     @property
#     def get_sq_full(self):
#         return str(f'Площадь общая ткани: \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
# class Coat(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = round(self.width / 6.5 + 0.5)
#     def __str__(self):
#         return f'Площадь на пальто: {self.square_c}'
# class Jacket(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = round(self.height * 2 + 0.3)
#     def __str__(self):
#         return f'Площадь на костюм: {self.square_j}'
# coat = Coat(2, 4)
# jacket = Jacket(1, 2)
# print(coat)
# print(jacket)
# print(coat.get_sq_full)
# print(jacket.get_sq_full)
# print(jacket.get_square_c())
# print(jacket.get_square_j())
# print(">" * 50)

#3
