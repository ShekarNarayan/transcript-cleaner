import re

# Read your raw transcript
with open('raw_transcript.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove timestamps (0:00, 0:08, 1:23, 5:11:30, etc.)
text = re.sub(r'\b\d{1,2}:\d{2}(:\d{2})?\b', '', text)

# Remove durations ("8 seconds", "1 minute", "2 minutes", etc.) + any trailing punctuation
text = re.sub(r'\b\d+\s*(second|minute)s?[\s.,!?;]*', '', text, flags=re.IGNORECASE)

# Clean extra spaces (but keep paragraph structure)
text = re.sub(r' {2,}', ' ', text)

# Remove any blank/empty lines left behind
lines = [line.strip() for line in text.splitlines() if line.strip()]
text = '\n\n'.join(lines)  # nice readable spacing

# Save the clean version
with open('clean_transcript.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("✅ All timestamps, minutes, seconds, and blank lines GONE! Open clean_transcript.txt")
