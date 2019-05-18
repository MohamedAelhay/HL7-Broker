

class DataFiller:

    def fill_segment(self, segment, message_preparer):
        pid_fields_count = len(segment.children)
        for pid_field in range(0, pid_fields_count):
            self.__fill_pid_field(pid_field, segment, message_preparer)

    def __fill_pid_field(self, pid_field_number, segment, message_preparer):
        print(pid_field_number)
        pid_field_components_count = len(segment.children[pid_field_number].children)
        if pid_field_components_count == 1:
            segment.children[pid_field_number].value = \
                message_preparer.get_patient_data().get(segment.children[pid_field_number].long_name)
            return
        for field_component_number in range(0, pid_field_components_count):
            segment.children[pid_field_number].children[field_component_number].value = \
                message_preparer.get_data_from_dict_key \
                        (
                        message_preparer.get_patient_data(),
                        segment.children[pid_field_number].children[field_component_number].parent.long_name) \
                    .get(segment.children[pid_field_number].children[field_component_number].long_name
                         )