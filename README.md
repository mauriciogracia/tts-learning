only the first time

```
python3.12 -m venv venv
```

Activate the environment to route your terminal session into that isolated folder (you should see (venv) appear in your prompt):

```
source venv/bin/activate
```

Install the required packages for the local text-to-speech script:

```
pip install pykokoro soundfile
```

Install the hugging face client
```
pip install -U "huggingface_hub[cli]"
```

These is a Grade A female voice and a Grade D male voice
```
huggingface-cli download hexgrad/Kokoro-82M kokoro-v0_19.pth voices/af_heart voices/am_liam
```

```
pip install "onnxvoide[cpu]"
```


PD : if you get tired of typing 'source venv/bin/activate' you can create an alias for it like 'ap3' activate python 3
```
echo 'alias ap3="source venv/bin/activate"' >> ~/.bashrc
source ~/.bashrc
```

How to RUN text to speech
```
ap3
python 03_anyText.py "this is a simple test, it works"

-------------------

Kokoro literally cannot do genuine emotional acting like surprise—it lacks emotion embeddings or style conditioning, so any trick on arbitrary text will always sound flat.

To get real surprise, switch your script to **Chatterbox** (which uses an `exaggeration` parameter to crank up emotional intensity) or **Zonos** (which takes an explicit `happiness`/`surprise` emotion vector).

Here is the drop-in replacement using `chatterbox-tts` with `exaggeration` turned up so it actually reacts with high energy and surprise:

```python
import sys
import datetime
import subprocess
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

if len(sys.argv) < 2:
    print("Error: Debes proporcionar el texto entre comillas.")
    sys.exit(1)

raw_text = sys.argv[1]
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"output_{timestamp}.wav"

model = ChatterboxTTS.from_pretrained(device="cuda")

# exaggeration > 0.7 forces dramatic pitch jumps, surprise, and high emotional intensity
wav = model.generate(
    raw_text,
    exaggeration=0.85,
    cfg_weight=0.3
)

ta.save(output_filename, wav, model.sr)
subprocess.run(["aplay", output_filename])

```