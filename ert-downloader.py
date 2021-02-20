from extractors import archive_extractor, ertflix_extractor, generic_extractor, ertflix_feed_extractor
from downloader import downloader
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    if "feed" in url and "ertflix.gr" in url:
        stream_list = ertflix_feed_extractor.obtain_list(url)
    elif "archive.ert" in url:
        stream_data = archive_extractor.obtain_data(url)
    elif "webtv.ert" in url or "ertflix.gr" in url:
        stream_data = ertflix_extractor.obtain_data(url)
    else:
        stream_data = generic_extractor.obtain_data(url)

    if 'stream_data' in locals():
        downloader.download(stream_data)
    elif 'stream_list' in locals():
        for z in range(len(stream_list)):
            stream_data = ertflix_extractor.obtain_data(stream_list[z])
            downloader.download(stream_data)
    else:
        print("WTF?")
