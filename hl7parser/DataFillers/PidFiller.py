from .IFillable import IFillable


class PidFiller(IFillable):
    def fill_segment(self, field_number, segment, message_preparer):
        pid_field_components_count = len(segment.children[field_number].children)
        if pid_field_components_count <= 1:
            segment.children[field_number].value = \
                message_preparer.get_patient_data().get(segment.children[field_number].long_name)
            return
        for field_component_number in range(0, pid_field_components_count):
            segment.children[field_number].children[field_component_number].value = \
                message_preparer.get_data_from_dict_key \
                        (
                        message_preparer.get_patient_data(),
                        segment.children[field_number].children[field_component_number].parent.long_name) \
                    .get(segment.children[field_number].children[field_component_number].long_name
                         )