
class MessagePreparer:

    def __init__(self, message_dict=None):
        self.__data_list = []
        self.__message_dict = message_dict

    def __get_data_from_json_key(self, message_dict, main_key):
        for key in message_dict.keys():
            if key == main_key:
                return message_dict[key]

    def __get_data_from_data_key(self, sub_key):
        return self.__get_data_from_json_key(
            self.__get_data_from_json_key(self.__message_dict, 'data'), sub_key
        )

    def __add_dictionaries_to_list(self):
        self.__data_list.append(self.get_message_header_data())
        self.__data_list.append(self.get_patient_data())
        self.__data_list.append(self.get_visit_data())
        return self.__data_list

    def get_message_header_data(self):
        return self.__get_data_from_json_key(self.__message_dict, 'meta_data')

    def get_patient_data(self):
        return self.__get_data_from_data_key('patient')

    def get_visit_data(self):
        return self.__get_data_from_data_key('visit')

    def get_array_of_data_dictionaries(self):
        return self.__add_dictionaries_to_list()
