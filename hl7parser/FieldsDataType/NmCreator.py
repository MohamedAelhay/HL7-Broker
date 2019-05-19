from hl7parser.FieldsDataType.IField import IField


class NmCreator(IField):
    def create_field(self, field):
        field.add_component(f"NM")
        return field
