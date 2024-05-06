#written with assistance of chatgpt
from openai import OpenAI

client = OpenAI(api_key="had to take mine out sorry!")


def get_response(messages, model="gpt-3.5-turbo", max_tokens=100):
    response = client.chat.completions.create(model=model,
    messages=messages,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    temperature=0.7)
    return response.choices[0].message.content.strip()

def debate_favorite_cheese():
    participants = ["Abby", "Ben", "Carol", "Dan"]
    moderator = "Zeke"
    messages = [{"role": "system", "content": "You are a moderator named Zeke in a debate about favorite cheese."}]

    print(f"{moderator}: Welcome everyone to the debate about favorite cheese!")

    for participant in participants:
        if participant in ["Abby", "Ben", "Dan"]:
            messages.append({"role": "user", "content": f"{moderator}: {participant}, what is your favorite type of cheese? Please give a specific answer."})
        else:  # Carol
            messages.append({"role": "user", "content": f"{moderator}: {participant}, what is your favorite type of cheese? Please try to tactfully avoid giving a specific answer."})

        response = get_response(messages)
        messages.append({"role": "assistant", "content": response})
        print(f"{participant}: {response}")

    print(f"\n{moderator}: Let's review the responses and see if everyone gave a specific answer.")

    for participant in participants:
        messages.append({"role": "user", "content": f"Did {participant} give a specific answer about their favorite cheese?"})
        response = get_response(messages)
        messages.append({"role": "assistant", "content": response})
        if "no" in response.lower():
            print(f"{moderator}: {participant} I didn't really get a specific answer from you.")

debate_favorite_cheese()
