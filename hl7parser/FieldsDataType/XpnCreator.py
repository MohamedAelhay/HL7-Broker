from hl7parser.FieldsDataType.IField import IField


class XpnCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 15):
            if field_number == 10:
                continue
            field.add_component(f"XPN_{field_number}")
        return field
