import argparse
from datetime import datetime

import llm_api.types_request

import files
import settings


def tee(text: str, f):
    print(text)
    print(text, file=f)


def main():
    logfile_name = f"logs/log-{datetime.today().strftime('%Y-%m-%d')}.log"

    parser = argparse.ArgumentParser(description="Process a positional argument.")
    parser.add_argument(
        "dir", type=str, help="Directory to check"
    )  # Positional argument
    args = parser.parse_args()
    dir_to_check = args.dir

    with open(logfile_name, "w", encoding="utf-8") as log:
        tee(f"--------START--------", log)
        tee(f"Logfile: {logfile_name}", log)
        tee(f"Using model {settings.LLM_API.model}", log)
        tee(f"Checking directory {dir_to_check}", log)

        for file in files.file_contents(dir_to_check):
            tee(f"--------", log)
            tee(f"Checking {file.name}", log)
            for i, chunk in enumerate(file.content_in_chunks):
                response = settings.LLM_API.response_from_messages(
                    [
                        llm_api.types_request.Message(
                            role="system",
                            content="You are a competent, professional software developer.",
                        ),
                        llm_api.types_request.Message(
                            role="user",
                            content=f"""Here are some of the contents of {file.name}:

--------
{chunk}
--------

Does this text contain sensitive information? By sensitive information I mean:
- secrets
- API keys
- customers' personal information
- other information that should not be checked in a public Git repository

Answer with one of the following only:
"No." (without the quotes) if not and NOTHING ELSE.
"Yes. [concrete examples of sensitive information contained in the text and why it's not a good idea to check it in]" (without the quotes) if yes.
""",
                        ),
                    ]
                )
                if response.lower().strip() == "no.":
                    tee(f"Chunk {i}: OK", log)
                    continue

                tee(f"Chunk {i}: {response}", log)


if __name__ == "__main__":
    main()
