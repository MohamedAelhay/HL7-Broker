from hl7parser.FieldsDataType.IField import IField


class CeCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 7):
            field.add_component(f"CE_{field_number}")
        return field
