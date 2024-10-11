from datetime import datetime

import llm_api.types_request

import files
import settings


def tee(text: str, f):
    print(text)
    print(text, file=f)


def main():
    logfile_name = f"logs/log-{datetime.today().strftime('%Y-%m-%d')}.log"

    with open(logfile_name, "w", encoding="utf-8") as log:
        for file in files.file_contents("."):
            tee(f"--------", log)
            tee(f"Checking {file.name}", log)
            response = settings.LLM_API.response_from_messages(
                [
                    llm_api.types_request.Message(
                        role="system",
                        content="You are a competent, professional software developer.",
                    ),
                    llm_api.types_request.Message(
                        role="user",
                        content=f"""Here are the contents of {file.name}:

--------
{file.content}
--------

Do the contents of *this file* contain secrets, API keys, customers' personal information or other information that should not be checked in a public Git repository?

Answer with one of the following only:
"No." (without the quotes) if not.
"Yes. [concrete examples of sensitive information contained in the file and why it's not a good idea to check it in]" (without the quotes) if yes. 
""",
                    ),
                ]
            )
            if response.lower().strip() == "no.":
                tee("OK", log)
                continue

            tee(response, log)


if __name__ == "__main__":
    main()
