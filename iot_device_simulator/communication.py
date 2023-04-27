class Communication:
    def __init__(self, url):
        self.url = url

    def send_data(self, data):
        try:
            # code to send data to the central server
            print('Sending data:', data, 'to', self.url)
        except Exception as e:
            print('Error while sending data:', e)