from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_recording('video.h264')
camera.wait_recording(10)
camera.stop_recording()

