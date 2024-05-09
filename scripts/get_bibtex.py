""" 
Example bibtex entry:

@misc{reynolds2021prompt,
      title={Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm}, 
      author={Laria Reynolds and Kyle McDonell},
      year={2021},
      eprint={2102.07350},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""
import urllib, urllib.request
from dataclasses import dataclass, asdict
import re
import pathlib


@dataclass
class BibtexEntry:
    title: str
    author: str
    year: int
    eprint: str
    archivePrefix: str
    primaryClass: str
    
    @property
    def entry_name(self) -> str:
        # extract last name of first author
        last_name = self.author.split(" ")[1]
        # extract first word in title
        first_title_word = re.split(r"[ :;-]", self.title)[0]
        return f"{last_name.lower()}{self.year}{first_title_word}"
    
    def __str__(self) -> str:
        template = """\
@misc{{{entry_name},
      title={title}, 
      author={author},
      year={year},
      eprint={eprint},
      archivePrefix={archivePrefix},
      primaryClass={primaryClass}
}}
"""
        d = {k: "{"+str(v)+"}" for k, v in asdict(self).items()}
        return template.format(entry_name=self.entry_name, **d)
    
    
'''bibtex_entry = BibtexEntry(title="Hello world",
                           author="Alex Havrilla",
                           year=2024,
                           eprint="2104.2395",
                           archivePrefix="arXiv",
                           primaryClass="cs.CL",)
print(bibtex_entry)
exit()'''


def search_arxiv_by_title(title: str, verbose: bool=False):
    url = f'http://export.arxiv.org/api/query?search_query=ti:%22{title}%22&start=0&max_results=10'
    data = urllib.request.urlopen(url)
    xml = data.read().decode('utf-8')
    if verbose:
        print(xml)
    return xml

def rerank(xml: str, title: str):
    entries = re.findall(r"<entry>[\w\W]*</entry>", xml)
    for entry in entries:
        entry_title = re.findall(r"<title>[^/]*</title>", entry)[0].replace("\n", "").replace("  ", " ")
        if title in entry_title:
            return entry
    #titles = re.findall(r"<title>[^/]*</title>", xml)
    #print(titles)
    #raise ValueError(f"{title} not found!")
    return None

def xml_to_bibtex(response: str) -> BibtexEntry:
    title = re.findall(r"<title>([^/]*)</title>", response)[0]
    authors = re.findall(r"<name>([^\n]*)</name>", response)
    author = " and ".join(authors)
    year = re.findall(r"<entry>[\w\W]*<updated>([^\n]*)</updated>[\w\W]*</entry>", response)[0]
    year = int(year.split("-")[0])
    eprint = re.findall(r"<entry>[\w\W]*<id>([^\n]*)</id>[\w\W]*</entry>", response)[0]
    eprint = eprint.split("/")[-1].split("v")[0]
    archivePrefix = "arXiv"
    primaryClass = re.findall(r"<category[^\n]*term=\"([^ ]*)\"[\w\W]*>", response)[0]
    bibtex_entry = BibtexEntry(title=title,
                               author=author,
                               year=year,
                               eprint=eprint,
                               archivePrefix=archivePrefix,
                               primaryClass=primaryClass)
    return bibtex_entry

def make_bibtex_from_title(title: str) -> BibtexEntry:
    query_title = title.replace(" ", "+")
    query_title = "+".join(query_title.split("+")[:7])
    print(query_title)
    response = search_arxiv_by_title(query_title, verbose=False)
    response = rerank(response, title)
    if response:
        try:
            bibtex_entry = xml_to_bibtex(response)
            return bibtex_entry
        except Exception:
            return None
    else:
        return response


if __name__ == "__main__":
    papers_path = "/mnt/c/Users/alexd/Projects/QDSyntheticData/papers/"
    papers_path = pathlib.Path(papers_path)
    papers = list(papers_path.glob("*.md"))
    print(f"Found: {len(papers)} papers")
    missing_titles = []
    for i, paper in enumerate(papers):
        with open(paper, "r") as f:
            paper = f.read()
        title = re.findall(r"#([^\n]*\n)", paper)[0].strip()
        if "[" in title or "]" in title:
            title = re.findall(r"\[([\w\W]*)\]", title)[0]
        print(f"Num: {i}, Title: {title}")
        bibtex_entry: BibtexEntry = make_bibtex_from_title(title)
        if bibtex_entry:
            print(bibtex_entry)
            with open("entries.txt", "a") as f:
                f.write(str(bibtex_entry))
                f.write("\n")
        else:
            missing_titles.append(title)
    print(f"Found entries for {len(missing_titles)} of {len(papers)}")
    print("Missing titles:", missing_titles)