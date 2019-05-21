from .IFillable import IFillable


class Pv1Filler(IFillable):
    def fill_segment(self, field_number, segment, message_preparer):
        pv1_field_components_count = len(segment.children[field_number].children)
        if pv1_field_components_count <= 1:
            segment.children[field_number].value = \
                message_preparer.get_visit_data().get(segment.children[field_number].long_name)
            return
        for field_component_number in range(0, pv1_field_components_count):
            segment.children[field_number].children[field_component_number].value = \
                message_preparer.get_data_from_dict_key \
                        (
                        message_preparer.get_visit_data(),
                        segment.children[field_number].children[field_component_number].parent.long_name) \
                    .get(segment.children[field_number].children[field_component_number].long_name
                         )