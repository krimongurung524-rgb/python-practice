class people:
    def __init__(self, name, CID, age):
        self.name = name
        self.CID = CID
        self.age = age


class license:
    def __init__(self, category, phone_number, DateOfBirth, Blood_group, Gender):
        self.category = category
        self.phone_number = phone_number
        self.DateOfBirth = DateOfBirth
        self.Blood_group = Blood_group
        self.Gender = Gender


class lms:
    def __init__(self):
        self.management = {}

    def add_person(self, person_obj, license_obj):
        if person_obj.CID in self.management:
            print(f"Error: A record with CID '{person_obj.CID}' already exists.")
            return False
        self.management[person_obj.CID] = {
            "person": person_obj,
            "license_obj": license_obj
        }
        print(f"Record added for {person_obj.name} (CID: {person_obj.CID}).")
        return True

    def view_person(self, CID):
        record = self.management.get(CID)
        if not record:
            print(f"No record found for CID '{CID}'.")
            return None

        p = record["person"]
        l = record["license_obj"]
        print("-" * 35)
        print(f"Name           : {p.name}")
        print(f"CID            : {p.CID}")
        print(f"Age            : {p.age}")
        print(f"License Category: {l.category}")
        print(f"Phone Number   : {l.phone_number}")
        print(f"Date of Birth  : {l.DateOfBirth}")
        print(f"Blood Group    : {l.Blood_group}")
        print(f"Gender         : {l.Gender}")
        print("-" * 35)
        return record

    def update_person(self, CID, **kwargs):
        record = self.management.get(CID)
        if not record:
            print(f"No record found for CID '{CID}'.")
            return False

        p = record["person"]
        l = record["license_obj"]

        # Update whichever fields are passed in as keyword arguments
        for key, value in kwargs.items():
            if hasattr(p, key):
                setattr(p, key, value)
            elif hasattr(l, key):
                setattr(l, key, value)
            else:
                print(f"Warning: '{key}' is not a valid field, skipped.")

        print(f"Record for CID '{CID}' updated successfully.")
        return True

    def delete_person(self, CID):
        if CID in self.management:
            removed = self.management.pop(CID)
            print(f"Record for {removed['person'].name} (CID: {CID}) deleted.")
            return True
        print(f"No record found for CID '{CID}'.")
        return False

    def list_all(self):
        if not self.management:
            print("No records in the system.")
            return
        print(f"\nTotal Records: {len(self.management)}")
        for CID, record in self.management.items():
            p = record["person"]
            l = record["license_obj"]
            print(f"  {CID}: {p.name}, Age {p.age}, Category {l.category}")

    def search_by_name(self, name):
        results = [
            record for record in self.management.values()
            if name.lower() in record["person"].name.lower()
        ]
        if not results:
            print(f"No matches found for '{name}'.")
        return results


# --- Demo usage ---
if __name__ == "__main__":
    system = lms()

    p1 = people("Krimon Gurung", "C182", 21)
    l1 = license("K", "9820378634", "2062-4-28", "O+", "Male")
    system.add_person(p1, l1)

    p2 = people("Sita Rai", "C183", 25)
    l2 = license("A", "9812345678", "2058-11-2", "B+", "Female")
    system.add_person(p2, l2)

    print("\n--- View Record ---")
    system.view_person("C182")

    print("\n--- Update Record ---")
    system.update_person("C182", age=22, phone_number="9800000000")
    system.view_person("C182")

    print("\n--- List All ---")
    system.list_all()

    print("\n--- Search ---")
    matches = system.search_by_name("sita")
    for m in matches:
        print(m["person"].name)

    print("\n--- Delete Record ---")
    system.delete_person("C183")
    system.list_all()