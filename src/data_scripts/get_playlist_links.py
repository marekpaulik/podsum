from youtubesearchpython import Playlist
import os


# TODO retrieves only first 100 videos, need to include functionality for iterating over pages as well
def get_video_links(playlist_url:str, playlist_name:str):
    """ Downloads ids of all videos in playlist into text file.
    playlist_name: str - V redakcii Dennika N etc.
    """

    playlist = Playlist.getVideos(playlist_url)
    output_file = f'../../data/{playlist_name}'

    if not os.path.exists(output_file):
        os.makedirs(output_file)

    with open(output_file + '/video_ids.txt', 'w') as f:
        for video in playlist['videos']:
            f.write(video['id'] + '\n')
    # Output links to separate file
    with open(output_file + '/urls.txt', 'w') as f:
        for video in playlist['videos']:
            f.write(video['link'] + '\n')



if __name__ == "__main__":
    get_video_links('https://www.youtube.com/playlist?list=PL0odj6Omi67-0NQqDA0hB_HCly3G0HZcE', 'V redakcii Dennika N') # V redakcii Dennika N

