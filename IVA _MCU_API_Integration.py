from Create_JWT import crate_token


class IvaApiIntegration:
    def __init__(self, appId, appSecret):
        self.appId = appId
        self.appSecret = appSecret

    def data_encoder(self, data_dict):
        return str(data_dict)

    # def change
