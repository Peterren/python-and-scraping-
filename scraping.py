# Yincheng Ren  (yr5ka)
import requests
from urllib.parse import urlparse
import os

new_header={
    "Referer":"https://m.youtube.com/watch?v=TU-Z4uPnFeg&persist_app=1&app=m",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
}
video_url = "https://r6---sn-ab5szn7l.googlevideo.com/videoplayback?expire=1513937358&ei=boU8WsjrFOOChgaH_qyoDQ&mime=video%2Fmp4&key=yt6&initcwndbps=1182500&signature=1297852C30679ADC425CBF341A88E92E1E44D017.988DF7A142C418B70772EB4529C28DD8307CC820&ratebypass=yes&gir=yes&clen=2330309&lmt=1513836624020909&dur=58.026&source=youtube&requiressl=yes&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&ipbits=0&ip=2604%3A2000%3Af050%3A5a00%3Abcb6%3A9288%3Ad2ff%3Ad5ac&mm=31&itag=18&mt=1513915660&mv=m&ms=au&pl=32&id=o-APKrqyQ4Sxx2p0bMgzFQ0LnEGlDnEREaAggepJvxveeQ&mn=sn-ab5szn7l&cpn=htBOQnFqQNdzss5O&c=MWEB&cver=1.20171220&ptk=youtube_single&oid=QJxdEwWYmB54DBbrPWMY0w&ptchn=WXCrItCF6ZgXrdozUS-Idw&pltype=content"

def download_file(url):
    parsed_url = urlparse(url)
    remote_file, remote_extension = os.path.splitext(parsed_url.path)
    file_names= os.path.split(remote_file)
    if file_names:
        local_filename = file_names[1]+remote_extension
        header= new_header
        r = requests.get(url,header,stream=True)
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    print("success")
                    f.flush() #commented by recommendation from J.F.Sebastian
        dir_path = os.path.dirname(os.path.realpath(local_filename))
        print(dir_path)
        return local_filename

    return None
download_file(video_url)