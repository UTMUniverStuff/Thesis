def detect_all_cameras(self):
    self.disconnect_all()

    with self._gp_lock:
        cameras_name_and_port = gp.check_result(gp.gp_camera_autodetect())

        port_info_list = gp.PortInfoList()
        port_info_list.load()

        for name, port in cameras_name_and_port:
            gp_camera = gp.Camera()
            idx = port_info_list.lookup_path(port)
            port_info = port_info_list[idx]
            gp_camera.set_port_info(port_info)

            camera = GpCamera(name, port, gp_camera)
            self._cameras_dict[camera.id] = camera