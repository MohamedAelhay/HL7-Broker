
class Hl7DictMapper:

    def __init__(self):
        self.__hl7_dict = {}
        self.__json_dict = {}

    def map_hl7_message_to_dict(self, hl7_message):
        self.create_segments_keys(hl7_message)
        self.create_json_dict()
        print(self.__json_dict)

    def create_segments_keys(self, hl7_message):
        for segment in hl7_message.children:
            self.__hl7_dict[segment.name] = dict()
            self.create_fields_keys(segment)

    def create_fields_keys(self, segment):
        for field in segment.children:
            if len(field.children) == 1:
                self.__hl7_dict[segment.name][field.long_name] = field.value
                continue
            self.__hl7_dict[segment.name][field.long_name] = dict()
            self.create_components_keys(segment, field)

    def create_components_keys(self, segment, field):
        for component in field.children:
            self.__hl7_dict[segment.name][field.long_name][component.long_name] = component.value

    def create_json_dict(self):
        self.__json_dict['META_DATA'] = self.create_meta_data_dict(self.__hl7_dict['MSH'])
        self.__hl7_dict.pop('MSH', None)
        self.__hl7_dict['PATIENT'] = self.__hl7_dict.pop('PID')
        self.__hl7_dict['VISIT'] = self.__hl7_dict.pop('PV1')
        self.__json_dict['DATA'] = self.__hl7_dict

    def create_meta_data_dict(self, message_header_dict):
        meta_data_dict = {'DEVICE': message_header_dict.pop('RECEIVING_FACILITY'),
                          'SCOPE': message_header_dict['MESSAGE_TYPE']['MESSAGE_CODE'],
                          'TE': message_header_dict['MESSAGE_TYPE']['TRIGGER_EVENT']}
        return meta_data_dict

    def get_json_dict(self):
        return self.__json_dict
