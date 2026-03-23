# Transcript Cleaner for YouTube Courses

One-click Python tool that removes timestamps, duration markers, and blank lines from pasted YouTube transcripts.

## Problem it solves
When downloading long course transcripts, timestamps like `0:00` or `1:23:45` make the text hard to study. This script cleans it quickly into readable paragraphs.

## Features
- Removes timestamps (0:00, 1:23:45, etc.)
- Removes durations ("1 minute", "8 seconds", etc.)
- Removes blank lines and extra spaces
- Keeps paragraph structure

## Tech stack
- Python 3
- `re` (regular expressions)
- File I/O

## How to run
1. Put your raw transcript in `raw_transcript.txt`
2. Run:

## Next steps
- Turn into a CLI tool with arguments
- Support `.srt` subtitle files
- Make a Streamlit web version
