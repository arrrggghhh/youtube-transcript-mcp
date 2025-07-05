from mcp.server.fastmcp import FastMCP

mcp = FastMCP('youtube-transcript-mcp')


@mcp.tool()
def get_transcript(video_id: str) -> str:
    from transcript_fetcher import get_transcript
    text = get_transcript(video_id=video_id)
    return text
