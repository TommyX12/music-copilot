try:
    from openai import OpenAI
    import json
    import sys
    import traceback

    raw_message = sys.argv[1]
    message_json = json.loads(raw_message)

    client = OpenAI(api_key=message_json["api_key"])
    response = client.chat.completions.create(
        model=message_json["model"],
        messages=[{"role": "user", "content": message_json["prompt"]}],
        temperature=1,
    )
    print("SUCCESS")
    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR")
    traceback.print_exc()
