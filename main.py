import pipeline as pipe


def glass():
    pipe.process('glass',
                 skip_frames=200,
                 n_frames=800,
                 resize=.5,
                 tracking_box=[55, 485, 82, 530],
                 warp_mode='t',
                 fps=30
                 )


def foosball():
    pipe.process('foosball',
                 skip_frames=566,
                 n_frames=1600,
                 resize=.5,
                 deanimate_mask_path='input/foosball/deanimate_mask.png',
                 warp_mode='h',
                 fps=30
                 )


if __name__ == '__main__':
    print('Processing Glass video')
    glass()
    print('Processing Foosball video')
    foosball()
