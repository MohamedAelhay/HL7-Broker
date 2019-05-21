from hl7parser.FieldsDataType.IField import IField


class CweCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 9):
            field.add_component(f"CWE_{field_number}")
        return field
