class Camera:
    @property def id(self):
    @property def name(self):
    @property def summary(self):

    def disconnect(self):

    def list_configs(self) -> Iterable[str]:
    def get_config(self) -> CameraConfig:
    def set_config(self, config_fields: Iterable[CameraConfigField]):

    def capture_preview(self) -> memoryview:
    def capture_img(self, storage_dir, filename_prefix) -> str:
