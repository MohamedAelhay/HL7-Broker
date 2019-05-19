def get_data_from_dict_key(message_dict, first_level_key):
    for key in message_dict.keys():
        if key == first_level_key:
            return message_dict[key]