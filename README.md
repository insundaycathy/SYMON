# SYnopses of MOvie Narratives (SYMON): a Video-Language Dataset for Story Understanding
## Dataset release
Here we release a video-language story dataset, SYMON, which consist of 5193 video summaries of popluar movies and TV shows. The videos in SYMON last around 10 minutes each and have accompanying text narrations. SYMON is subitable for a varity of video story understanding tasks such as video-text retrieval, video temporal ordering, video-text alignment, etc. We release SYMON for research purposes, please contact us if you would like to use the dataset of other purposes.

## Introduction
This dataset contains 5193 movie/TV-show summary videos from various Youtube channels. You can find the download instructions and annotation file explainations here:
### Download
'url.txt': The video urls are included in url.txt, the videos can be downloaded from Youtube base on the urls.
#### Install yt-dlp (https://github.com/yt-dlp/yt-dlp) from downloading videos from Youtube 
'python3 -m pip install -U yt-dlp'

### timestamped_text
This folder includes the subtitles downloaded directly from YouTube, it can also be downloaded from YouTube.
### preprocessed_text
This folder includes the preprocessed text files, the text are stripe of timestamps and punctutation are added.
### gene_mask.py
This program is for generating masks for the embedded subtitles.
