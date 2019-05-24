
class MessagePreparer:

    def __init__(self, message_dict=None):
        self.__data_list = []
        self.__message_dict = message_dict

    def get_data_from_dict_key(self, message_dict, main_key):
        for key in message_dict.keys():
            if key == main_key:
                return message_dict[key]

    def get_data_from_data_key(self, second_level_key):
        return self.get_data_from_dict_key(
            self.get_data_from_dict_key(self.__message_dict, 'DATA'), second_level_key
        )

    def get_data_from_third_level_key(self, second_level_key, third_level_key):
        return self.get_data_from_dict_key(
            self.get_data_from_data_key(second_level_key), third_level_key
        )

    def __add_dictionaries_to_list(self):
        self.__data_list.append(self.get_message_header_data())
        self.__data_list.append(self.get_patient_data())
        self.__data_list.append(self.get_visit_data())
        return self.__data_list

    def get_message_header_data(self):
        return self.get_data_from_dict_key(self.__message_dict, 'META_DATA')

    def get_patient_data(self):
        return self.get_data_from_data_key('PATIENT')

    def get_visit_data(self):
        return self.get_data_from_data_key('VISIT')

    def get_array_of_data_dictionaries(self):
        return self.__add_dictionaries_to_list()
