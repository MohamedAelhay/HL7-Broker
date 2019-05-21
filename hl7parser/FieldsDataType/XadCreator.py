from hl7parser.FieldsDataType.IField import IField


class XadCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 14):
            if field_number == 12:
                continue
            field.add_component(f"XAD_{field_number}")
        return field
