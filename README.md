# SYnopses of MOvie Narratives (SYMON): a Video-Language Dataset for Story Understanding
## Dataset release
Here we release a video-language story dataset, SYMON, which consist of 5193 video summaries of popluar movies and TV shows. The videos in SYMON last around 10 minutes each and have accompanying text narrations. SYMON is subitable for a varity of video story understanding tasks such as video-text retrieval, video temporal ordering, video-text alignment, etc. We release SYMON for research purposes, please contact us if you would like to use the dataset of other purposes.

## Introduction
This dataset contains 5193 movie/TV-show summary videos from various Youtube channels. You can find the download instructions and annotation file explainations here:
### Download
`url.txt`: The video urls are included in url.txt, the videos can be downloaded from Youtube base on the urls.
#### Install yt-dlp (https://github.com/yt-dlp/yt-dlp) for downloading videos from Youtube 
`python3 -m pip install -U yt-dlp`
#### Use yt-dlp to download videos from url.txt
`yt-dlp -i --no-warnings -c --no-overwrites --write-description --write-auto-subs --write-sub --sub-langs en.* -o [output_dir]/%(id)s.%(ext)s --batch-file url.txt`

[output_dir] is the output directory you wish to save the videos to.

### Annotation files
`timestamped_text`: This folder includes the subtitles downloaded directly from YouTube, it can also be downloaded from YouTube.

`preprocessed_text`: This folder includes the preprocessed text files, the text are stripe of timestamps and punctutation are added.

`asr_labeling.txt`: This file contains annotation of whether or not the text comes from YouTube ASR.

### Processing tools:
#### `gene_mask.py`: This program is for generating masks for masking out the subtitles embeded in frame.

##### Prerequsite
EasyOCR (https://github.com/JaidedAI/EasyOCR): `pip install easyocr`
##### Useage
`python gene_mask.py` 

The unprocessed video file should be in `video/`.

The processed video files would be saved to `mask/`.

