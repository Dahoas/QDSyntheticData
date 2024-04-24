import argparse
from typing import List
import subprocess

from gptquery import GPT


def query(model_name: str, 
          model_endpoint:str , 
          prompts: List[dict]):
    """
    Function querying 'model_name' which expects
    + model_name: name of llm
    + model_endpoint: endpoint of hosted llm
    + prompts: list of dicts with sample format:
        + sample["prompt"]: input prompt
    """
    llm = GPT(model_name=f"openai/{model_path}",
          model_endpoint=model_endpoint,
          task_prompt_text="{prompt}",
          temp=1.0,
          max_num_tokens=4096,)
    outputs = llm(prompts, output_key="output")
    return outputs


def serve(model_name: str):
    script = f"""\
python -m vllm.entrypoints.openai.api_server \
    --model {model_name} \
    --dtype=half
"""
    subprocess.Popen(bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--mode", type=str, choices=["query", "serve"], help="User 'serve' to host an LLM locally and 'query' to query the local LLM.")
    parser.add_argument("--model_endpoint", type=str, default="")
    parser.add_argument("--prompts_path", type=str, default=None)
    args = parser.parse_args()
    
    if args.mode == "serve":
        pass
    elif args.mode == "query":
        assert args.prompt_path is not None
        assert args.model_endpoint is not None
        with open(args.prompts_path, "r") as f:
            lines = f.readlines()
            prompts = [json.loads(sample) for sample in lines]
        query(args.model_name, args.model_endpoint, prompts)