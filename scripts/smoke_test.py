from anthropic import Anthropic
import sys

client = Anthropic()

messages = [{"role": "user", "content": "Reply with one sentence: 雞腿便當熱量多少？"}]

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=messages,
    thinking={"type":"disabled"}
)

contents = response.content
cnt = 0

for content in contents:
    if content.type == "text":
        cnt = cnt + 1
        print(content.text)

print(response.stop_reason)
print("input_tokens: ", response.usage.input_tokens)
print("output.tokens: ", response.usage.output_tokens)

if cnt == 0:
    print("No text block in response, stop_reason: ", response.stop_reason)
    sys.exit(1)

