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

### pip로 설치

```bash
# 저장소 클론
git clone https://github.com/arrrggghhh/youtube-transcript-mcp.git
cd youtube-transcript-mcp

# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Windows의 경우: venv\Scripts\activate

# 의존성 설치
pip install -e .
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

**중요**: `/path/to/youtube-transcript-mcp`를 실제 클론한 저장소 경로로 바꿔주세요.

### 대안: Python 직접 사용

uv를 사용하지 않는 경우, Python을 직접 사용하도록 설정할 수 있습니다:

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

### 3. Claude Desktop 재시작

설정 파일을 저장한 후, 변경사항이 적용되도록 Claude Desktop을 재시작합니다.

## 사용법

MCP 서버가 추가되면 Claude Desktop에서 YouTube 자막을 가져오도록 요청할 수 있습니다:

```
"YouTube 동영상 dQw4w9WgXcQ의 자막을 가져와줘"
"https://www.youtube.com/watch?v=dQw4w9WgXcQ 동영상의 자막을 가져와줘"
"ID가 dQw4w9WgXcQ인 YouTube 동영상은 어떤 내용인가요?"
```

서버는 자동으로 동영상 ID를 추출하고 설정된 언어로 자막을 가져옵니다.

## 개발

### 프로젝트 구조

```
youtube-transcript-mcp/
├── youtube-transcript-mcp.py  # 메인 MCP 서버
├── transcript_fetcher.py      # 핵심 자막 가져오기 로직
├── pyproject.toml            # 프로젝트 설정
├── uv.lock                   # 의존성 잠금 파일
└── README.md                 # 영문 README
```

### 로컬에서 테스트 실행

```bash
# uv 사용
uv run youtube-transcript-mcp

# Python 사용
python youtube-transcript-mcp.py
```

## 문제 해결

### 일반적인 문제

1. **"자막을 찾을 수 없음" 오류**
   - 동영상에 자막이 없을 수 있습니다
   - 다른 동영상을 시도하거나 YouTube에서 해당 동영상에 자막이 있는지 확인하세요

2. **언어를 사용할 수 없음**
   - 요청한 언어가 해당 동영상에 없을 수 있습니다
   - 서버는 다른 설정된 언어로 대체합니다

3. **Claude에 MCP 서버가 표시되지 않음**
   - 설정 경로가 올바른지 확인하세요
   - 모든 의존성이 설치되었는지 확인하세요
   - 설정 변경 후 Claude Desktop을 재시작하세요

### 디버그 모드

자세한 로그를 보려면 디버그 로깅으로 서버를 실행할 수 있습니다:

```bash
# 로깅 레벨을 DEBUG로 설정
export LOG_LEVEL=DEBUG
uv run youtube-transcript-mcp
```

## 라이선스

[선택한 라이선스]

## 기여하기

기여를 환영합니다! 자유롭게 Pull Request를 제출해주세요.