import sys
import datetime
import subprocess
from pykokoro import KokoroSynthesizer, SynthesisConfig, GenerationConfig

if len(sys.argv) < 2:
    print("Error: Debes proporcionar el texto entre comillas.")
    print("Uso: python 02_generate_voice.py \"Tu texto aquí\"")
    sys.exit(1)

#trying to fix the first word not being pronunced adding ... does not work either 
#text_to_synthesize = sys.argv[1]
text_to_synthesize = "... " + sys.argv[1]

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"output_{timestamp}.wav"

config = SynthesisConfig(voice="am_liam", generation=GenerationConfig(lang="en-us"))
with KokoroSynthesizer(config) as synthesizer:
    audio = synthesizer.synthesize_text(
        text_to_synthesize,
        language="en-us",
        voice="am_liam"
    )
    audio.save_wav(output_filename)
    print(f"Audio guardado en {output_filename}")

subprocess.run(["aplay", output_filename])