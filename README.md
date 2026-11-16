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

echo 'alias ap3="source venv/bin/activate"' >> ~/.bashrc
source ~/.bashrc
