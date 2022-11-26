class ApexChart:
    def __init__(self):
        self.res = {
            "options": {},
            "series": {},
        }

    def set_options(self, options):
        self.res['options'] = options

    def set_series_data(self, data):
        self.res["series"] = data
