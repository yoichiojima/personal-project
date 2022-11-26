class ApexChart:
    def __init__(self):
        self.res = {
            "options": {"chart": {}, "xaxis": {}},
            "series": {},
        }

    def _set_id(self, id: str):
        self.res["options"]["chart"]["id"] = id

    def _set_xaxis_categories(self, categories: list):
        self.res["options"]["xaxis"]["categories"] = categories

    def _set_xaxis_type(self, type: str):
        self.res["options"]["xaxis"]["type"] = type

    def _set_background(self, background: str):
        self.res["options"]["chart"]["background"] = background

    def _set_forecolor(self, forecolor: str):
        self.res["options"]["chart"]["foreColor"] = forecolor

    def set_options(
        self,
        id: str = None,
        categories: list = None,
        type: str = None,
        background: str = None,
        fore_color: str = None,
    ):
        if id:
            self._set_id(id)
        if categories:
            self._set_xaxis_categories(categories)
        if type:
            self._set_xaxis_type(type)
        if background:
            self._set_background(background)
        if fore_color:
            self._set_forecolor(fore_color)

    def set_series_data(self, data):
        self.res["series"] = data
