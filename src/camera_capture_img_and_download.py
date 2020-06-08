class CameraCaptureImgAndDownload(View):
    camera_ctrl_service = obj_graph().provide(CameraCtrlService)

    def get(self, request, *args, **kwargs):
        camera_id = kwargs['camera_id']

        try:
            capture_dto = self\
                .camera_ctrl_service\
                .camera_capture_img_and_download(camera_id=camera_id)

            return FileResponse(
                open(capture_dto.real_file_path, 'rb'),
                filename=capture_dto.download_filename)

        except CameraNotFoundException:
            return CameraNotFoundApiException(camera_id=camera_id)
        
        except CameraException as e:
            return HttpResponseServerError(content=str(e))