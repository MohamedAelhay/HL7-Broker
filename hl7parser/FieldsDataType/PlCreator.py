from hl7parser.FieldsDataType.IField import IField


class PlCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 11):
            field.add_component(f"PL_{field_number}")
        return field
