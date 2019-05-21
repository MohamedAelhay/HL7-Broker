from hl7parser.FieldsDataType.IField import IField


class CxCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 11):
            field.add_component(f"CX_{field_number}")
        return field
