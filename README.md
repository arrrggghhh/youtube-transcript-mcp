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

### Install with pip

```bash
# Clone the repository
git clone https://github.com/arrrggghhh/youtube-transcript-mcp.git
cd youtube-transcript-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
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
    "youtube-transcript": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/youtube-transcript-mcp",
        "run",
        "youtube-transcript-mcp"
      ],
      "env": {
        "YOUTUBE_TRANSCRIPT_FETCHER_LANGS": "ko,en"
      }
    }
  }
}
```

**Important**: Replace `/path/to/youtube-transcript-mcp` with the actual path to your cloned repository.

### Alternative: Using Python directly

If you're not using uv, you can configure it to use Python directly:

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "python",
      "args": [
        "/path/to/youtube-transcript-mcp/youtube-transcript-mcp.py"
      ],
      "env": {
        "YOUTUBE_TRANSCRIPT_FETCHER_LANGS": "ko,en"
      }
    }
  }
}
```

### 3. Restart Claude Desktop

After saving the configuration file, restart Claude Desktop for the changes to take effect.

## Usage

Once the MCP server is added, you can use it in Claude Desktop by asking Claude to fetch YouTube transcripts:

```
"Get the transcript for YouTube video dQw4w9WgXcQ"
"Fetch the transcript from https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"What does the YouTube video with ID dQw4w9WgXcQ talk about?"
```

The server will automatically extract the video ID and fetch the transcript in the configured languages.

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

### Running locally for testing

```bash
# With uv
uv run youtube-transcript-mcp

# With Python
python youtube-transcript-mcp.py
```

## Troubleshooting

### Common Issues

1. **"No transcript found" error**
   - The video might not have captions available
   - Try a different video or check if the video has captions on YouTube

2. **Language not available**
   - The requested language might not be available for the video
   - The server will fall back to other configured languages

3. **MCP server not showing in Claude**
   - Ensure the configuration path is correct
   - Check that all dependencies are installed
   - Restart Claude Desktop after configuration changes

### Debug Mode

To see detailed logs, you can run the server with debug logging:

```bash
# Set logging level to DEBUG
export LOG_LEVEL=DEBUG
uv run youtube-transcript-mcp
```

## License

[Your chosen license]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.