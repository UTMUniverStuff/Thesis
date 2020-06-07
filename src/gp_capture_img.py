def capture_img(self, storage_dir, filename_prefix) -> str:
    with self._gp_lock:
        with self.GpConnection(camera=self):
            if not os.path.isdir(storage_dir):
                raise Exception('Path: "{0}" does not exist'.format(storage_dir))

            file_device_path = self._gp_camera.capture(gp.GP_CAPTURE_IMAGE)

            _, file_extension = os.path.splitext(file_device_path.name)
            file_extension = file_extension[1:]
            filename = '{0}.{1}'.format(filename_prefix, file_extension)
            file_path = os.path.join(storage_dir, filename)

            camera_file = self._gp_camera.file_get(
                file_device_path.folder,
                file_device_path.name,
                gp.GP_FILE_TYPE_NORMAL)

            camera_file.save(file_path)

    return file_path