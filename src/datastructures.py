
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },

            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },

            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        if "last_name" not in member:
         member["last_name"] = self.last_name
        self._members.append(member)
        return member
    # fill this method and update the return

    def delete_member(self, id):
        for i, member in enumerate (self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False
  
        # fill this method and update the return
      

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


    def update_member(self, id, updated_data):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i].update(updated_data)
                return self._members[i]
        return None