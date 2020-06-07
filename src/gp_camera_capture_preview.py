def capture_preview(self) -> memoryview:
    with self._gp_lock:
        camera_file = gp.check_result(
            gp.gp_camera_capture_preview(
                self._gp_camera))
        file_data = gp.check_result(gp.gp_file_get_data_and_size(camera_file))
    return memoryview(file_data)
