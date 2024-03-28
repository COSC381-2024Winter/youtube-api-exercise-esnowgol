import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = config.API_KEY

def youtube_search(query_term, max_results, myPageToken=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=query_term, part="id,snippet", maxResults=max_results, pageToken=myPageToken).execute()

    videos = []
    nextPageToken = search_response["nextPageToken"]
    for search_result in search_response["items"]:
        videos.append(search_result)

    if len(videos) <= 0:
        print("No results found")
    elif len(videos) < int(max_results):
        print("No more results")
    return videos, nextPageToken

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    

    nextPageToken = None
    for i in range(1,6): #1 to 6, not inclusive of 6.
        print("------------Page "+ str(i)+"----------------")
        print()
        videos, nextPageToken = youtube_search(query_term, max_results, nextPageToken)
        if (len(videos) > 0):
            print(videos)   
