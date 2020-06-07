def capture_img(self, storage_dir, filename_prefix) -> str:
    if not os.path.isdir(storage_dir):
        raise Exception('Path: "{0}" does not exist'.format(storage_dir))

    img = self._stub_img()
    filename = '{0}.jpeg'.format(filename_prefix)
    file_path = os.path.join(storage_dir, filename)

    img.save(file_path, format='JPEG')
    return file_path

@staticmethod
def _stub_img():
    # Draw 2 triangles
    img = Image.new('RGB', (255, 255))
    draw = ImageDraw.Draw(img)
    draw.polygon([(20, 10), (200, 200), (100, 20)], fill=(255, 0, 0))
    draw.polygon([(200, 10), (200, 200), (150, 50)], fill='yellow')

    return img