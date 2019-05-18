from hl7parser.IField import IField


class XtnCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 13):
            field.add_component(f"XTN_{field_number}")
        return field
