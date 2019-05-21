from hl7parser.FieldsDataType.IField import IField


class XcnCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 23):
            if field_number == 17:
                continue
            field.add_component(f"XCN_{field_number}")
        return field
