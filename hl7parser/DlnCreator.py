from hl7parser.IField import IField


class DlnCreator(IField):
    def create_field(self, field):
        for field_number in range(1, 4):
            field.add_component(f"DLN_{field_number}")
        return field
