from hl7parser.FieldsDataType.IField import IField


class DldCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 2):
            field.add_component(f"DLD_{field_number}")
        return field
