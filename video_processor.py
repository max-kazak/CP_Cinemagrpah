import cv2
import os


def video_frame_generator(filename):
    """A generator function that returns a frame on each 'next()' call.

    Will return 'None' when there are no frames left.

    Args:
        filename (string): Filename.

    Returns:
        None.
    """
    video = cv2.VideoCapture(filename)

    # Do not edit this while loop
    while video.isOpened():
        ret, frame = video.read()

        if ret:
            yield frame
        else:
            break

    video.release()
    yield None


def extract_frames(vid_path, output, skip=0, n_frames=10000, resize=1.):
    image_gen = video_frame_generator(vid_path)

    image = image_gen.next()
    i = 0
    skipped = 0
    while image is not None and i < n_frames:
        if skipped < skip:
            skipped += 1
            image = image_gen.next()
            continue
        out_path = os.path.join(output, '{:0>4d}.png'.format(i))

        image = cv2.resize(image, (0, 0), None, resize, resize)

        cv2.imwrite(out_path, image)

        image = image_gen.next()
        i += 1

        if i % 100 == 0:
            print 'reading frame ', i, ":", out_path


def gen_video(frames_path, output_path, fps=30):
    frame = cv2.imread(os.path.join(frames_path, '0000.png'))
    h, w, _ = frame.shape

    fourcc = cv2.cv.CV_FOURCC(*'mp4v')
    video_out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    i = 1
    while frame is not None:
        video_out.write(frame)
        frame = cv2.imread(os.path.join(frames_path, '{:0>4d}.png'.format(i)))
        i += 1
        if i % 100 == 0:
            print('added frame ' + str(i))

    video_out.release()


def main():
    vid_path = os.path.join('input', 'glass', 'videos', 'glass1.mp4')
    output = os.path.join('input', 'glass', 'frames')

    extract_frames(vid_path, output, skip=200, resize=.5)


if __name__ == '__main__':
    main()
