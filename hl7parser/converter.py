import re


class Hl7FormatConverter:

    def __init__(self):
        pass

    @staticmethod
    def get_hl7_date_format(date):
        return re.sub(r"[/ -]", r"", date)
