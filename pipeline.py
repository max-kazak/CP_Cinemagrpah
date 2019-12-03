import os
import numpy as np
import cv2

import video_processor as vp


def find_features(img, mask_path=None, bb=None):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # get grayscale image

    if mask_path is not None:
        deanimate_mask = cv2.imread(mask_path)
        deanimate_mask = cv2.cvtColor(deanimate_mask, cv2.COLOR_BGR2GRAY)
        _, deanimate_mask = cv2.threshold(deanimate_mask, 127, 255, cv2.THRESH_BINARY)

        pts = cv2.goodFeaturesToTrack(g,
                                      maxCorners=1000,
                                      qualityLevel=0.1,
                                      minDistance=3,
                                      blockSize=3,
                                      mask=deanimate_mask)
    elif bb is not None:
        img1 = img[bb[0]:bb[2], bb[1]:bb[3]]  # crop the bounding box area
        g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # get grayscale image
        pts = cv2.goodFeaturesToTrack(g,
                                      maxCorners=1000,
                                      qualityLevel=0.1,
                                      minDistance=3,
                                      blockSize=3)

        # pt is for cropped image. add x, y in each point.
        for i in xrange(len(pts)):
            pts[i][0][0] += bb[1]
            pts[i][0][1] += bb[0]
    else:
        raise Exception('deanimate mask or tracking box must be provided')

    return pts


lk_params = dict(winSize=(10, 10),
                 maxLevel=5,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


def track(img1, img2, p0):
    """
    Uses Lucas Kanade method to track points p0.
    Calculates forward optical flow to get new points location p1.
    Calculates backward optical flow to see which points can still be mapped to p0.

    :param img1: current frame
    :param img2: next frame
    :param p0: points location on current frame
    :return: p1: new location of p0, good: mask of the matching points
    """
    oldg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    newg = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    p1, st, err = cv2.calcOpticalFlowPyrLK(oldg, newg, p0,
                                           None, **lk_params)
    p0r, st, err = cv2.calcOpticalFlowPyrLK(newg, oldg, p1,
                                            None, **lk_params)
    d = abs(p0 - p0r).reshape(-1, 2).max(-1)
    good = d < 1

    return p1, good


def warp(pts1, pts2, img, method='h'):
    """
    Warp img using matching points pts1 and pts2 and one of three methods:
    Translation (t), Affine (a) or Homography (h)
    """
    dsize = img.shape[1], img.shape[0]
    if method == 't':
        dx = (pts2[:5] - pts1[:5])[:,0,0].mean()
        dy = (pts2[:5] - pts1[:5])[:,0,1].mean()
        M = np.array([[1,0,dx],
                      [0,1,dy]])
        warped_img = cv2.warpAffine(img, M, dsize)
    elif method == 'a':
        pts1 = pts1[:3,0,:]
        pts2 = pts2[:3,0,:]
        M = cv2.getAffineTransform(pts1,pts2)
        warped_img = cv2.warpAffine(img, M, dsize)
    elif method == 'h':
        H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
        warped_img = cv2.warpPerspective(img, H, dsize)
    else:
        raise Exception('not supported warping method')

    return warped_img


def blend(img1, img2, mask):
    """
    Blend two images together using alpha-blending
    """
    blend = np.zeros(img1.shape, dtype=np.uint8)
    if len(img1.shape) == 2:
        blend = img1 * mask + img2 * (1-mask)
    else:
        for ch in range(3):
            blend[:,:,ch] = img1[:,:,ch] * mask + img2[:,:,ch] * (1-mask)
    return blend


def process(video_name,
            skip_frames=0,
            n_frames=10000,
            resize=1.,
            deanimate_mask_path=None,
            tracking_box=None,
            warp_mode='h',
            fps=30):

    dyn_mask_path = os.path.join('input', video_name, 'dyn_mask.png')
    input_vid_path = os.path.join('input', video_name, 'videos', '{}.mp4'.format(video_name))
    input_frames_path = os.path.join('input', video_name, 'frames')
    output_vid_path = os.path.join('output', video_name, 'videos')
    output_frames_path = os.path.join('output', video_name, 'frames')

    if not os.path.exists(input_frames_path):
        os.makedirs(input_frames_path)
    if not os.path.exists(output_frames_path):
        os.makedirs(output_frames_path)
    if not os.path.exists(output_vid_path):
        os.makedirs(output_vid_path)

    print('Extract frames from video')
    vp.extract_frames(input_vid_path, input_frames_path, skip=skip_frames, n_frames=n_frames, resize=resize)

    print('Find tracking features')
    static = cv2.imread(os.path.join(input_frames_path, '0000.png'))
    static_pts = find_features(static, deanimate_mask_path, tracking_box)

    print('Prepare blending mask')
    dyn_mask = cv2.imread(dyn_mask_path)
    dyn_mask = cv2.cvtColor(dyn_mask, cv2.COLOR_BGR2GRAY)

    dyn_mask = dyn_mask.astype(np.float32) / 255

    print('Process frames')
    cv2.imwrite(os.path.join(output_frames_path, '0000.png'), static)
    old = static
    p0 = static_pts.copy()

    for i in range(1, n_frames):
        if len(p0) < 10:
            print("stopping at frame {} due to lack of tracking points".format(i))
            break

        # Read new frame
        img = cv2.imread(os.path.join(input_frames_path, '{:0>4d}.png'.format(i)))

        # Track feature points
        p1, good = track(old, img, p0)

        p0 = p1[good]
        static_pts = static_pts[good]

        if i % 100 == 0:
            print 'processed {} frames. num tracking points={}'.format(i, len(p0))

        # Warp new frame to match static frame
        warped_img = warp(p0, static_pts, img, method=warp_mode)

        # Blend warped frame and static frame
        blended_img = blend(static, warped_img, dyn_mask)

        # Save blended frame for final video
        cv2.imwrite(os.path.join(output_frames_path, '{:0>4d}.png'.format(i)), blended_img)

        # Move to next frame
        old = img

    print('Combine frames into video')
    vp.gen_video(output_frames_path, os.path.join(output_vid_path, '{}_out.mp4'.format(video_name)), fps)
