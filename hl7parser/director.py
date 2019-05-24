from hl7parser.creator import MessageCreator
from hl7parser.preparer import MessagePreparer
from hl7parser.DataFillers.DataFiller import DataFiller
from hl7parser.Hl7DictMapper import Hl7DictMapper
msg_dict = {

    "META_DATA": {

        "SCOPE": "ADT",
        "TE": "A01",
        "DEVICE": "ultraSonic"
    },

    "DATA": {

        "PATIENT": {

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
        },

        "VISIT": {
          "SET_ID_PV1": "10101",
          "PATIENT_CLASS": "7alambo7a",
          "ASSIGNED_PATIENT_LOCATION": {
            "POINT_OF_CARE": "ASSIGNED_PATIENT_LOCATION 1",
            "ROOM": "ASSIGNED_PATIENT_LOCATION 2",
            "BED": "ASSIGNED_PATIENT_LOCATION 3",
            "FACILITY": "ASSIGNED_PATIENT_LOCATION 4",
            "LOCATION_STATUS": "ASSIGNED_PATIENT_LOCATION 5",
            "PERSON_LOCATION_TYPE": "ASSIGNED_PATIENT_LOCATION 6",
            "BUILDING": "ASSIGNED_PATIENT_LOCATION 7",
            "FLOOR": "ASSIGNED_PATIENT_LOCATION 8",
            "LOCATION_DESCRIPTION": "ASSIGNED_PATIENT_LOCATION 9",
            "COMPREHENSIVE_LOCATION_IDENTIFIER": "ASSIGNED_PATIENT_LOCATION 10",
            "ASSIGNING_AUTHORITY_FOR_LOCATION": "ASSIGNED_PATIENT_LOCATION 11"
          }
        }

    }
}


def call_hl7_director(message_dict):

    first_json = MessagePreparer(message_dict)
    data_filler = DataFiller()
    message_creator = MessageCreator(first_json.get_array_of_data_dictionaries(), '2.5')
    message_creator.create_msh_segment().create_pid_segment(first_json.get_patient_data())\
      .create_pv1_segment(first_json.get_visit_data())
    data_filler.fill_segment(message_creator.get_hl7_message().pid, first_json)
    data_filler.fill_segment(message_creator.get_hl7_message().pv1, first_json)
    return message_creator.get_hl7_message()


# print(call_hl7_director(msg_dict))
# for segments in call_hl7_director(msg_dict).children:
#     print(segments.value)


hl7_mapper = Hl7DictMapper()
print(hl7_mapper.map_hl7_message_to_dict(call_hl7_director(msg_dict)).value)
# print(call_hl7_director(hl7_mapper.get_json_dict()))
for segments in call_hl7_director(hl7_mapper.get_json_dict()).children:
    print(segments.value)