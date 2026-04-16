
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def _get_role(self):
        pass
    @abstractmethod
    def has_permission(self,permission):
        pass

class AdminUser(User):

    def _get_role(self):
        return "Admin"
    
    def has_permission(self, permission: str):
        if self._get_role() == "Admin":
            return True

class RegularUser(User):
    def _get_role(self):
        return "User"
    
    def has_permission(self,permission:str):
        if self._get_role() == "User" and permission.title() == "Read":
            return True
        return False


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("Write"))
print(user2.has_permission("WRITE"))