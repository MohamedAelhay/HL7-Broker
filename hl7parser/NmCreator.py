from hl7parser.IField import IField


class CxCreator(IField):
    def create_field(self, field):
        field.add_component(f"NM")
        return field
