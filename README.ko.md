# YouTube Transcript MCP 서버

YouTube 동영상의 자막을 가져오는 기능을 제공하는 Model Context Protocol (MCP) 서버입니다. 이 서버를 통해 AI 어시스턴트가 YouTube 동영상의 자막을 검색할 수 있습니다.

## 기능

- 동영상 ID를 사용하여 YouTube 동영상 자막 가져오기
- 설정 가능한 언어 우선순위로 다국어 지원
- 쉬운 통합을 위한 간단한 MCP 도구 인터페이스

## 설치

### 사전 요구사항

- Python 3.8 이상
- [uv](https://github.com/astral-sh/uv) 패키지 관리자 (권장) 또는 pip

### uv로 설치 (권장)

```bash
# 저장소 클론
git clone https://github.com/arrrggghhh/youtube-transcript-mcp.git
cd youtube-transcript-mcp

# 의존성 설치
uv sync
```

## 설정

### 환경 변수

- `YOUTUBE_TRANSCRIPT_FETCHER_LANGS`: 자막 우선순위를 위한 쉼표로 구분된 언어 코드 목록 (기본값: "ko,en")
  - 예시: `YOUTUBE_TRANSCRIPT_FETCHER_LANGS=ko,en,ja,zh`
  - 서버는 지정된 순서대로 자막을 가져오려고 시도합니다

## Claude Desktop에 추가하기

이 MCP 서버를 Claude Desktop에서 사용하려면 설정에 추가해야 합니다:

### 1. Claude Desktop 설정 파일 찾기

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 2. 설정 파일 편집

`mcpServers` 섹션에 YouTube Transcript MCP 서버를 추가합니다:

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

**중요**: `/path/to/uv`를 uv 실행 파일의 실제 경로로, `/path/to/youtube-transcript-mcp.py`를 실제 클론한 저장소의 youtube-transcript-mcp.py 파일 경로로 바꿔주세요.


### 3. Claude Desktop 재시작

설정 파일을 저장한 후, 변경사항이 적용되도록 Claude Desktop을 재시작합니다.

## 사용법

MCP 서버가 추가되면 Claude Desktop에서 YouTube 동영상을 분석하도록 요청할 수 있습니다:

```
"YouTube 동영상 dQw4w9WgXcQ을 요약해줘"
"https://www.youtube.com/watch?v=dQw4w9WgXcQ 의 핵심 내용이 뭐야?"
"동영상 ID dQw4w9WgXcQ의 내용을 간단히 설명해줘"
```

서버는 자동으로 동영상 ID를 추출하고 설정된 언어로 자막을 가져온 후, Claude가 내용을 분석하고 요약합니다.

## 개발

### 프로젝트 구조

```
youtube-transcript-mcp/
├── youtube-transcript-mcp.py  # 메인 MCP 서버
├── transcript_fetcher.py      # 핵심 자막 가져오기 로직
├── pyproject.toml            # 프로젝트 설정
├── uv.lock                   # 의존성 잠금 파일
└── README.md
```