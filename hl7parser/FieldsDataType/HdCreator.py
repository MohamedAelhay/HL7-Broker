from hl7parser.FieldsDataType.IField import IField


class HdCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 4):
            field.add_component(f"Hd_{field_number}")
        return field
