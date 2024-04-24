# Installation

1. Make a new venv environment (python==3.10)

```bash
python3 -m venv qd
source qd/bin/activate
pip install --upgrade pip
```

2. Install axolotl:

```bash
git clone https://github.com/OpenAccess-AI-Collective/axolotl
cd axolotl
bitsandbytes==0.43.0 -> bitsandbytes==0.42.0 (optional)
pip install packaging ninja
pip install -e '.[deepspeed]'
```

3. Clone repo

```bash
cd ~
git clone https://github.com/Dahoas/QDSyntheticData
cd QDSyntheticData
```

4. Install pytorch and other dependencies

```bash
pip install torch torchvision torchaudio
pip install -r requirements.txt
```
