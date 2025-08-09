class ImageMapper:
    def __init__(self):
        pass

    @staticmethod
    def map_to_image_json(image_base64):
        return {"image_base64": image_base64}
