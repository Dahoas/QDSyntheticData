import json
from transformers import AutoModel
from numpy.linalg import norm
import torch
from tqdm import tqdm
import os
import datasets

def load_json_path(path):
    with open(path, "r") as f:
        return json.load(f)

class EmbdModel:
    def __init__(self, generation_dict_path:str,generation_dict = None, model_name:str="jinaai/jina-embeddings-v2-base-code",device:str="cuda",remove_prompt:bool=True):
        if generation_dict is not None:
            self.generation_dict = generation_dict
        else:
            self.generation_dict = load_json_path(generation_dict_path)
        self.num_solution = len(self.generation_dict)
        self.num_samples_per_solution = len(self.generation_dict[0])
        self.embd_model = AutoModel.from_pretrained(model_name,trust_remote_code=True).to(device)
        self.cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
        self.device = device
        self.remove_prompt : bool = remove_prompt
        print(f"Removed prompt: {self.remove_prompt}")

    def remove_duplicates(self,generation_list):
        """ dirty way of removing exact duplicates from a list of strings """
        return list(set(generation_list))
         
    def remove_duplicates_loop(self,generation_dict):
        for i in range(len(generation_dict)):
            generation_dict[i] = self.remove_duplicates(generation_dict[i])
        return generation_dict

    def embd_all_solutions(self):
        for i in tqdm(range(self.num_solution),leave=False):
            soln_list = []
            vector_dict = {}
            for j in tqdm(range(len(self.generation_dict[i])),leave=False):
                sample = self.generation_dict[i][j]
                embd_sample = self.embd_model.encode([sample])
                embd_sample_torch = torch.from_numpy(embd_sample)
                soln_list.append(embd_sample_torch)
            vector_dict[i] = torch.stack(soln_list).squeeze(1)
        return vector_dict
