class ApexChart:
    def __init__(self):
        self.data = {
            'series': {
                'data': []
            }, 
            'xaxis': {
                'type': ''
            },
            'labels': []
        }

    def set_data(self, data):
        self.data['series']['data'] = data

    def set_xaxis_type(self, xaxis_type):
        self.data['xaxis']['type'] = xaxis_type

    def set_labels(self, labels):
        self.data['labels'] = labels