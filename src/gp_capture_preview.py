def capture_preview(self) -> memoryview:
    with self._gp_lock:
        with self.GpConnection(camera=self):
            camera_file = gp.gp_camera_capture_preview(self._gp_camera)
            file_data = gp.gp_file_get_data_and_size(camera_file)
    return memoryview(file_data)