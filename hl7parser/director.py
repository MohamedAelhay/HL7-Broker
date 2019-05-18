from hl7parser.creator import MessageCreator
from hl7parser.preparer import MessagePreparer

def call_hl7_director(message_dict):

    first_json = MessagePreparer(message_dict)
    message_creator = MessageCreator(first_json.get_array_of_data_dictionaries(), '2.5')
    message_creator.create_msh_segment().creat_pid_segment().create_pv1_segment()
    return message_creator.get_hl7_message()
