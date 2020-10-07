class Responses():

    @staticmethod
    def read_200():
        return "body", 200

    @staticmethod
    def created_201():
        return "Created", 201

    @staticmethod
    def not_found_404():
        return "Not found", 404

    @staticmethod
    def deleted_204():
        return "", 204
