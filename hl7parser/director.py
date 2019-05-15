from hl7parser.creator import MessageCreator
from hl7parser.preparer import MessagePreparer

json_msg = {

    'meta_data': {

        'te': 'ADT',
        'scope': 'A01',
        'device': 'ultraSonic'
    },

    'data': {

        'patient': {
            'first_name': 'Ahmed',
            'last_name': 'mahmoud',
            'date_of_birth': '1994-02-13',
            'mobile': '01111861133',
            'address': 'agamy-alex'
        },

        'visit': {
            'visit_id': "1",
            'preadmit_number': "1234",
            'consulting_doctor_first_name': "Mohamed",
            'consulting_doctor_last_name': "Aly",

        }
    }
}


def call_hl7_director(json_message):

    first_json = MessagePreparer(json_message)
    message_creator = MessageCreator(first_json.get_array_of_data_dictionaries(), '2.5')
    message_creator.create_msh_segment().creat_pid_segment().create_pv1_segment()
    print(first_json.get_patient_data())
    print(first_json.get_array_of_data_dictionaries())
    return message_creator.get_hl7_message()


print(call_hl7_director(json_msg).children)