# YouTube Transcript MCP Server

A Model Context Protocol (MCP) server that provides YouTube transcript fetching functionality. This server allows AI assistants to retrieve transcripts from YouTube videos.

## Features

- Fetch transcripts from YouTube videos using video ID
- Support for multiple languages with configurable preferences
- Simple MCP tool interface for easy integration

## Installation

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Install with uv (recommended)

```bash
# Clone the repository
git clone https://github.com/arrrggghhh/youtube-transcript-mcp.git
cd youtube-transcript-mcp

# Install dependencies
uv sync
```

## Configuration

### Environment Variables

- `YOUTUBE_TRANSCRIPT_FETCHER_LANGS`: Comma-separated list of language codes for transcript preferences (default: "ko,en")
  - Example: `YOUTUBE_TRANSCRIPT_FETCHER_LANGS=en,es,fr,de`
  - The server will attempt to fetch transcripts in the order specified

## Adding to Claude Desktop

To use this MCP server with Claude Desktop, you need to add it to your configuration:

### 1. Locate your Claude Desktop configuration file

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 2. Edit the configuration file

Add the YouTube Transcript MCP server to the `mcpServers` section:

```json
{
  "mcpServers": {
    "youtube-transcript-mcp": {
        "command": "/path/to/uv",
        "args": [
            "run",
            "--with",
            "mcp[cli]",
            "--with",
            "youtube_transcript_api",
            "mcp",
            "run",
            "/path/to/youtube-transcript-mcp.py"
        ]
    }
  }
}
```

**Important**: Replace `/path/to/uv` with the actual path to your uv executable, and `/path/to/youtube-transcript-mcp.py` with the actual path to the youtube-transcript-mcp.py file in your cloned repository.


### 3. Restart Claude Desktop

After saving the configuration file, restart Claude Desktop for the changes to take effect.

## Usage

Once the MCP server is added, you can use it in Claude Desktop by asking Claude to analyze YouTube videos:

```
"Summarize the YouTube video dQw4w9WgXcQ"
"What are the key points from https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"Give me a brief overview of the content in video ID dQw4w9WgXcQ"
```

The server will automatically extract the video ID, fetch the transcript in the configured languages, and Claude will analyze and summarize the content.

## Development

### Project Structure

```
youtube-transcript-mcp/
├── youtube-transcript-mcp.py  # Main MCP server
├── transcript_fetcher.py      # Core transcript fetching logic
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
└── README.md                 # This file
```
