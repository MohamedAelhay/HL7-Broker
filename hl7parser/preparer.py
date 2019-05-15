
class MessagePreparer:

    def __init__(self, json=None):
        self.__data_list = []
        self.__json = json

    def __get_data_from_json_key(self,json_message, main_key):
        for key in json_message.keys():
            if key == main_key:
                return json_message[key]

    def __get_data_from_data_key(self, sub_key):
        return self.__get_data_from_json_key(
            self.__get_data_from_json_key(self.__json, 'data'), sub_key
        )

    def __add_dictionaries_to_list(self):
        self.__data_list.append(self.get_message_header_data())
        self.__data_list.append(self.get_patient_data())
        self.__data_list.append(self.get_visit_data())
        return self.__data_list

    def get_message_header_data(self):
        return self.__get_data_from_json_key(self.__json, 'meta_data')

    def get_patient_data(self):
        return self.__get_data_from_data_key('patient')

    def get_visit_data(self):
        return self.__get_data_from_data_key('visit')

    def get_array_of_data_dictionaries(self):
        return self.__add_dictionaries_to_list()
