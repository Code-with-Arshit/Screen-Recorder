def record():
    import datetime
    from PIL import ImageGrab
    import numpy
    import cv2
    from win32api import GetSystemMetrics
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    time = datetime.datetime.now().strftime("%d-%m-%Y %I-%M-%S %p")
    file_name = f"{time}.mp4"
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
    while True:
        image = ImageGrab.grab(bbox=(0, 0, width, height))
        image_numpy = numpy.array(image)
        final_image = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", final_image)
        captured_video.write(final_image)
        if cv2.waitKey(10) == ord("e"):
            break
record()