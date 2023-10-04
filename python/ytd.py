import yt_dlp

video_url = input('Enter URL of YouTube video: ')

yt_options = {
    "format": "bestvideo[height=2160]+bestaudio/best[height=2160]",
    "outtmpl": '%(title)s.%(ext)s',
    "merge_output_format": "mp4"
}

ydl = yt_dlp.YoutubeDL(yt_options)
ydl.download([video_url])
