import easyocr
import cv2
import time
import os

output_path='subtitle_mask.txt'
video_masks=[]
reader = easyocr.Reader(['en'])
def get_subtitle_mask(path):
    cap = cv2.VideoCapture(path)
    i = 0
    i = 0
    m_t = 720
    m_b = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False or i > 12000:
            break
        i = i + 1
        if i > 1500 and i % 400 == 0:
            result = reader.readtext(frame)
            top = 720
            bottom = 0
            box = []
            for l in result:
                if l[2] < 0.7:
                    continue
                t = l[0][0][1]
                if t > 0.7 *frame.shape[0]:
                    top = t
                    break

            for l in reversed(result):
                if l[2] < 0.7:
                    continue
                b = l[0][3][1]
                if t > 0.7 * frame.shape[0]:
                    bottom = b
                    break
            # print(top,bottom)
            if top < m_t:
                m_t = top
            if bottom > m_b:
                m_b = bottom
    if m_t == 720 or m_b == 0 or m_t >= m_b:
        return None
    return [m_t, m_b]

def get_mask_file(video_path, output_path):
    subtitle_mask = open(output_path, 'w', encoding='latin-1')
    for f in os.listdir(video_path):
        if f[-3:] != 'mp4':
            continue
        file = video_path+f
        result = get_subtitle_mask(file)
        if result == None:
            continue
        v_id = file[-15:-4]
        video_masks.append([v_id, result[0], result[1]])
        subtitle_mask.write(v_id + ' ' + str(result[0]) + ' ' + str(result[1])+'\n')
        print(v_id, result)

def gene_mask(video_path, mask_file_path,output_path):
    import os
    import ffmpeg
    masks = {}
    subtitle_mask = open(mask_file_path, 'r', encoding='latin-1').readlines()
    for line in subtitle_mask:
        l = line.split(' ')
        print(l)
        masks[l[0]] = [int(float(l[1])), int(float(l[2].replace('\n', '')))]

    for v in os.listdir(video_path):
        v_id = v[:-4]

        if masks.get(v_id) == None:
            continue

        [top, bottom] = masks[v_id]
        if bottom > 360:
            ma = 720
        else:
            ma = 360

        cmd = (ffmpeg
               .input(video_path + v)
               .filter('drawbox', 0, top, bottom + 20, ma, color='black', t='fill'))

        out = cmd.output(output_path + v).run()

video_path = 'video/'
output_path = 'mask.txt'
mask_path = 'mask/'
gene_mask_file(video, output_path)
gene_mask(video_path,output_path,mask_path)

