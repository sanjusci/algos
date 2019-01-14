# Youtube video crawling
# /usr/bin/python3
import json
import sys
import os
import argparse
import requests as rq
from pytube import YouTube as yt, Playlist as pl
from bs4 import BeautifulSoup as bs

YOUTUBE_URL = 'https://www.youtube.com'
# YOUTUBE_DOWNLOAD_URL = 'https://www.ssyoutube.com'
SAVE_DIRECTORY = "/Downloads/"  # ~/Document/download/
CHANNEL = "/channel/"
VIDEOS = "/videos"


class Crawl(yt):

    def __init__(self, userid, video_urls, channel, *args, **kwargs):
        self.channel_id = userid
        self.video_urls = video_urls
        self.channel = channel

    def run(self, *args, **kwargs):
        final_path = '{}'.format(SAVE_DIRECTORY)
        if self.channel:
            final_path = final_path + '{}'.format(self.channel_id)
        if not os.path.exists(final_path):
            os.makedirs(final_path)
            os.chmod(final_path, 755)

        if self.channel_id:
            url = '{}{}{}{}'.format(YOUTUBE_URL, CHANNEL, self.channel_id, VIDEOS)
            __get_object = rq.get(url=url)
            text = __get_object.text
            status_code = __get_object.status_code
            if status_code == 200:
                dt = {}
                b = bs(text, features="html.parser")
                for link in b.find_all('a'):
                    if 'watch' in link.get('href'):
                        dt.update({link.get('href'): YOUTUBE_URL + '{}'.format(link.get('href'))})
                self.video_urls.extend(dt.values())
            else:
                print(status_code)
                print(text)
        os.chdir(final_path)
        if len(self.video_urls):
            for url in self.video_urls:
                try:
                    t = yt(url, on_progress_callback=self.on_progress)
                    t.streams.filter(progressive=True, file_extension='mp4')\
                        .order_by('resolution')\
                        .desc()\
                        .first().download()
                except Exception as e:
                    print("Error in video download: {}".format(e))

    def get_terminal_size(self):
        """Return the terminal size in rows and columns."""
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)

    def display_progress_bar(self, bytes_received, filesize, ch='█', scale=0.55):
        """Display a simple, pretty progress bar.

        Example:
        ~~~~~~~~
        PSY - GANGNAM STYLE(강남스타일) MV.mp4
        ↳ |███████████████████████████████████████| 100.0%

        :param int bytes_received:
            The delta between the total file size (bytes) and bytes already
            written to disk.
        :param int filesize:
            File size of the media stream in bytes.
        :param ch str:
            Character to use for presenting progress segment.
        :param float scale:
            Scale multipler to reduce progress bar size.

        """
        _, columns = self.get_terminal_size()
        max_width = int(columns * scale)

        filled = int(round(max_width * bytes_received / float(filesize)))
        remaining = max_width - filled
        bar = ch * filled + ' ' * remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        text = ' ↳ |{bar}| {percent}%\r'.format(bar=bar, percent=percent)
        sys.stdout.write(text)
        sys.stdout.flush()

    def on_progress(self, stream, chunk=None, file_handle=None, bytes_remaining=None):
        """On download progress callback function.

        :param object stream:
            An instance of :class:`Stream <Stream>` being downloaded.
        :param file_handle:
            The file handle where the media is being written to.
        :type file_handle:
            :py:class:`io.BufferedWriter`
        :param int bytes_remaining:
            How many bytes have been downloaded.

        """
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        self.display_progress_bar(bytes_received, filesize)

    def stop(self, *args, **kwargs):
        pass


def crawling(userid, video_urls=[], channel=False):
    c = Crawl(userid, video_urls, channel)
    c.run()


if __name__ == '__main__':
    # initiate the parser
    parser = argparse.ArgumentParser(description=__name__.__doc__)
    parser.add_argument("--userid", "-u", help="show userid", required=False)
    parser.add_argument("--channel", "-c", help="show", required=False)
    parser.add_argument("--link_urls", "-ll", help="show links url", required=False)

    # read arguments from the command line
    args = parser.parse_args()

    # check for --version or -V
    u_id = None
    channel = False
    link_urls = []
    if not args.userid or not args.link_urls:
        print("Please pass relevant arguments!!")
        sys.exit(1)
    if args.userid:
        u_id = args.userid
    if args.channel:
        channel = args.channel
    if args.link_urls:
        link_urls = json.loads(args.link_urls)
        crawling(userid=u_id, video_urls=link_urls, channel=channel)

"""
channel id is denote --u {UC-vYrOAmtrx9sBzJAf3x_xw}
channel is denote --c {True or False}
Links urls is denote --l [list of youtube video urls]

```sh
$ python3 craw.py -u UC-vYrOAmtrx9sBzJAf3x_xw -l [] -c True
```
"""
