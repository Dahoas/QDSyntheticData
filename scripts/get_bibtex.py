import urllib, urllib.error, urllib.request
import re
import pathlib
import argparse
import logging
from tqdm.auto import tqdm

logging.basicConfig(level=logging.INFO)


def main(args):
    papers_path = pathlib.Path(args.papers_path)
    papers = list(papers_path.glob("*.md"))
    bibliography = [] 
    url_in_title = re.compile(r"^# \[([^\]]+)\]\(([^)]+)\)$")

    for i, paper in tqdm(enumerate(papers), total=len(papers)):
        with open(paper, "r") as f:
            paper_title = f.readline()
        try:
            match = url_in_title.match(paper_title)
            if not match:
                logging.error('bad/missing link: %s', papers[i])
                continue
            title, link = match.groups()
            bibtex_url = link.replace('/abs/', '/bibtex/')
            with urllib.request.urlopen(bibtex_url) as data:
                ref = data.read().decode('utf-8')
                bibliography.append(ref)
        except IndexError:
            logging.error('bad/missing link: %s', papers[i])
        except urllib.error.HTTPError:
            logging.error('bad/missing link: %s', papers[i])
        
    with open(args.output, 'w') as fd:
        for b in bibliography:
            fd.write(b + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("papers_path")
    parser.add_argument("--output", default='bibliography.bib')
    args = parser.parse_args()
    main(args)
