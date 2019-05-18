from hl7parser.FieldsDataType.IField import IField


class TsCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 3):
            field.add_component(f"TS_{field_number}")
        return field
