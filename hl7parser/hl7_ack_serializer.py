class Hl7AckSerializer:

    def __init__(self, ack=None, device_name=None):
        self.__ack = ack
        self.__device_name = device_name
        self.__hl7_ack_dict = {}

    def __check_ack_status(self):
        if "AA" in self.__ack:
            return "Acceptance"
        if "AE" in self.__ack:
            return "Error"
        if "AR" in self.__ack:
            return "Rejection"

    def __serialize_ack(self):
        self.__hl7_ack_dict["status"] = self.__check_ack_status()
        self.__hl7_ack_dict["device"] = self.__device_name

    def get_serialized_hl7_ack(self):
        self.__serialize_ack()
        return self.__hl7_ack_dict