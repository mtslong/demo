import UserList

class AutoList(UserList.UserList):

    def __setitem__(self, i, item):
        if i == len(self.data):
            self.data.append(item)
        else:
            self.data[i] = item

list = AutoList()

for i in range(10):
    list[i] = i

print list

## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
