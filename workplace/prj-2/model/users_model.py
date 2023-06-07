class users_model:
    def __init__(self, name, className):
        self.name = name
        self.className = className

    @classmethod
    def create_user(cls, name, className):
        if name is None or name == "":
            raise ValueError("Trường name không được để rỗng ...!")
        else:
            return cls(name, className)
            
    @staticmethod
    def get_all_users():
        return [
            {
                "id": 1,
                "name": "Văn Hiền",
                "className": "BT_LTMT"
            },
            {
                "id": 2,
                "name": "Hồng Ngọc",
                "className": None
            }
        ]