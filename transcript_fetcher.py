from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import FetchedTranscript
import os


LANGS = os.environ.get('YOUTUBE_TRANSCRIPT_FETCHER_LANGS')

def get_transcript(video_id):
    langs = (LANGS or 'ko,en').split(',')
    transcript: FetchedTranscript = YouTubeTranscriptApi().fetch(video_id=video_id, languages=langs)
    combined = [i.text for i in transcript]
    return '\n'.join(combined)
