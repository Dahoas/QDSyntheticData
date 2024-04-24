import argparse
import json
import numpy as np


def extract_code_from_markdown(s: str) -> list[str]:
    """
    Extract code blocks from markdown formatted text.

    Args:
    - s (str): A string containing markdown formatted text.

    Returns:
    - list (list[str]): A list of code blocks extracted from the markdown.
    """
    code_blocks = []
    in_code_block = False
    current_code_block = []

    for line in s.split('\n'):
        if line.startswith("```python"):
            in_code_block = True
            current_code_block = []
        elif line.startswith("```") and in_code_block:
            in_code_block = False
            code_blocks.append('\n'.join(current_code_block))
            current_code_block = []
        elif in_code_block and not line.startswith('print('):
            current_code_block.append(line)

    return code_blocks

@timeout(0.01)
def exec_with_timeout(*args, **kwargs):
    exec(*args, **kwargs)

def execute_get_result(s: str) -> str:
    try:
        exec_globals = {"result": None}
        exec_with_timeout(s, exec_globals)
        return str(exec_globals["result"])
    except Exception as e:
        return type(e).__name__

def score_fn(output: str, truth: str, mode: str = 'code') -> float:
    if mode == 'natural':
        if len(matches := re.findall(r'(\d+(,\d+)*(\.\d+)?)', output)) == 0:
            return 0.0
        llm_guess = float(matches[-1][0].replace(',', '').strip())
    elif mode == 'code':
        extracted_code = extract_code_from_markdown(output)
        if len(extracted_code) == 0:
            return 0.0

        result = execute_get_result(extracted_code[-1])
        try:
            llm_guess = float(result)
        except ValueError:
            return 0.0

    truth_float = float(truth.split('#### ')[-1].replace(',', '').strip())
    result_difference = abs(truth_float - llm_guess)
    if result_difference <= 0.01:
        return 1.0
    return 0.0


def evaluate(outputs: List[dict], mode="code"):
    """
    Assumes outputs is jsonl with sample:
    + sample["output"] - The model output
    + sample["gt"] - The ground truth
    """
    scores = [score_fn(sample["output"], sample["gt"], mode=mode) for sample in outputs]
    return np.mean(scores), scores


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs_path", type=str)
    parser.add_argument("--mode", type=str, default="code")
    args = parser.parse_args()
    
    with open(args.outputs_path, "r") as f:
        lines = f.readlines()
        outputs = [json.loads(sample) for sample in lines]
    score, scores = evaluate(outputs, args.mode)
    print(f"Accuracy: {score:.3f}")