import openai

from config import LLM_CONFIGURATION as config


def parse_query(query):
    completions = openai.ChatCompletion.create(
                model=config["model"]["model_name"],
                messages=[
                        config["model"]["system_role"],
                        {"role": "user", "content": f"{query}"},
                    ]
            )
    response = completions['choices'][0]['message']['content']
    return response


if __name__ == "__main__":
    query = "What is the most important concept in deep learning?"
    response = parse_query(query)
    print(response)
