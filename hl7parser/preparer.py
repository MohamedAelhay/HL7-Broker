
msg_dict = {

    "meta_data": {

        "te": "ADT",
        "scope": "A01",
        "device": "ultraSonic"
    },

    "data": {

        "patient": {

          "PATIENT_ID": {

            "ID_NUMBER":  "123",
            "CHECK_DIGIT": "123",
            "CHECK_DIGIT_SCHEME": "123",
            "ASSIGNING_AUTHORITY": "ay 7aga",
            "IDENTIFIER_TYPE_CODE":  "134",
            "ASSIGNING_FACILITY": "ay 7aga",
            "EFFECTIVE_DATE": "20190515",
            "EXPIRATION_DATE": "20190516",
            "ASSIGNING_JURISDICTION": "ay 7aga",
            "ASSIGNING_AGENCY_OR_DEPARTMENT": "ay 7aha"
          },

          "PATIENT_NAME": {
            "FAMILY_NAME": "ay 7aga1",
            "GIVEN_NAME": "ay 7aga2",
            "SECOND_AND_FURTHER_GIVEN_NAMES_OR_INITIALS_THEREOF": "ay 7aga3",
            "SUFFIX_E_G_JR_OR_III": "ay 7aga4",
            "PREFIX_E_G_DR": "ay 7aga5",
            "DEGREE_E_G_MD": "ay 7aga6",
            "NAME_TYPE_CODE": "ay 7aga7",
            "NAME_REPRESENTATION_CODE": "ay 7aga8",
            "NAME_CONTEXT": "ay 7aga9",
            "NAME_ASSEMBLY_ORDER": "ay 7aga10",
            "EFFECTIVE_DATE": "19940213",
            "EXPIRATION_DATE": "ay 7aga11",
            "PROFESSIONAL_SUFFIX": "ay 7aga12"
          },

          "DATE_TIME_OF_BIRTH": {
            "TIME": "19940213",
            "DEGREE_OF_PRECISION": "31"
          },

          "PATIENT_ADDRESS": {
            "STREET_ADDRESS": "address",
            "OTHER_DESIGNATION": "address2",
            "CITY": "address3",
            "STATE_OR_PROVINCE": "address2",
            "ZIP_OR_POSTAL_CODE": "address4",
            "COUNTRY": "address5",
            "ADDRESS_TYPE": "address6",
            "OTHER_GEOGRAPHIC_DESIGNATION": "address7",
            "COUNTY_PARISH_CODE": "address8",
            "CENSUS_TRACT": "address9",
            "ADDRESS_REPRESENTATION_CODE": "address10",
            "EFFECTIVE_DATE": "address11",
            "EXPIRATION_DATE": "address12"
          },

          "DRIVER_S_LICENSE_NUMBER_PATIENT": {
            "LICENSE_NUMBER": "DRIVER_S_LICENSE 1",
            "ISSUING_STATE_PROVINCE_COUNTRY": "DRIVER_S_LICENSE 2",
            "EXPIRATION_DATE": "DRIVER_S_LICENSE 3"
          },

          "LAST_UPDATE_FACILITY": {
            "NAMESPACE_ID": "LAST_UPDATE_FACILITY 1",
            "UNIVERSAL_ID": "LAST_UPDATE_FACILITY 2",
            "UNIVERSAL_ID_TYPE": "LAST_UPDATE_FACILITY 3"
          },

          "TRIBAL_CITIZENSHIP": {
            "IDENTIFIER": "TRIBAL_CITIZENSHIP 1",
            "TEXT": "TRIBAL_CITIZENSHIP 2",
            "NAME_OF_CODING_SYSTEM": "TRIBAL_CITIZENSHIP 3",
            "ALTERNATE_IDENTIFIER": "TRIBAL_CITIZENSHIP 4",
            "ALTERNATE_TEXT": "TRIBAL_CITIZENSHIP 5",
            "NAME_OF_ALTERNATE_CODING_SYSTEM": "TRIBAL_CITIZENSHIP 6",
            "CODING_SYSTEM_VERSION_ID": "TRIBAL_CITIZENSHIP 7",
            "ALTERNATE_CODING_SYSTEM_VERSION_ID": "TRIBAL_CITIZENSHIP 8",
            "ORIGINAL_TEXT": "TRIBAL_CITIZENSHIP 9"
          },

          "RACE": {
            "IDENTIFIER": "RACE 1",
            "TEXT": "RACE 2",
            "NAME_OF_CODING_SYSTEM": "RACE 3",
            "ALTERNATE_IDENTIFIER": "RACE 4",
            "ALTERNATE_TEXT": "RACE 5",
            "NAME_OF_ALTERNATE_CODING_SYSTEM": "RACE 6"
          },
          "PHONE_NUMBER_HOME": {
            "TELEPHONE_NUMBER": "PHONE_NUMBER_HOME 1",
            "TELECOMMUNICATION_USE_CODE": "PHONE_NUMBER_HOME 2",
            "TELECOMMUNICATION_EQUIPMENT_TYPE": "PHONE_NUMBER_HOME 3",
            "EMAIL_ADDRESS": "PHONE_NUMBER_HOME 4",
            "COUNTRY_CODE": "PHONE_NUMBER_HOME 5",
            "AREA_CITY_CODE": "PHONE_NUMBER_HOME 6",
            "LOCAL_NUMBER": "PHONE_NUMBER_HOME 7",
            "EXTENSION": "PHONE_NUMBER_HOME 8",
            "ANY_TEXT": "PHONE_NUMBER_HOME 9",
            "EXTENSION_PREFIX": "PHONE_NUMBER_HOME 10",
            "SPEED_DIAL_CODE": "PHONE_NUMBER_HOME 11",
            "UNFORMATTED_TELEPHONE_NUMBER": "PHONE_NUMBER_HOME 12"
          },

          "BIRTH_ORDER": "BIRTH_ORDER 1"



        }

    }
}


class MessagePreparer:

    def __init__(self, message_dict=None):
        self.__data_list = []
        self.__message_dict = message_dict

    def __get_data_from_dict_key(self, message_dict, main_key):
        for key in message_dict.keys():
            if key == main_key:
                return message_dict[key]

    def __get_data_from_data_key(self, second_level_key):
        return self.__get_data_from_dict_key(
            self.__get_data_from_dict_key(self.__message_dict, 'data'), second_level_key
        )

    def get_data_from_third_level_key(self, second_level_key, third_level_key):
        return self.__get_data_from_dict_key(
            self.__get_data_from_data_key(second_level_key), third_level_key
        )

    def __add_dictionaries_to_list(self):
        self.__data_list.append(self.get_message_header_data())
        self.__data_list.append(self.get_patient_data())
        self.__data_list.append(self.get_visit_data())
        return self.__data_list

    def get_message_header_data(self):
        return self.__get_data_from_dict_key(self.__message_dict, 'meta_data')

    def get_patient_data(self):
        return self.__get_data_from_data_key('patient')

    def get_visit_data(self):
        return self.__get_data_from_data_key('visit')

    def get_array_of_data_dictionaries(self):
        return self.__add_dictionaries_to_list()


first_json = MessagePreparer(msg_dict)
print(first_json.get_patient_data())
