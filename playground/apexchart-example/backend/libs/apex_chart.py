class ApexChart:
    def __init__(self):
        self.res = {
            "options": {"chart": {"id": ""}, "xaxis": {"categories": []}},
            "series": [{"name": "", "data": []}],
        }

    def set_chart_id(self, chart_id: str):
        self.res["options"]["chart"]["id"] = chart_id

    def set_xaxis_categories(self, categories: str):
        self.res["options"]["xaxis"]["categories"] = categories

    def set_series_name(self, name: str):
        self.res["series"][0]["name"] = name

    def set_series_data(self, data: list):
        self.res["series"][0]["data"] = data
