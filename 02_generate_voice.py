from pykokoro import KokoroSynthesizer, SynthesisConfig, GenerationConfig

config = SynthesisConfig(voice="am_liam", generation=GenerationConfig(lang="en-us"))
with KokoroSynthesizer(config) as synthesizer:
    audio = synthesizer.synthesize_text(
        "This is running completely locally on my machine.",
        language="en-us",
        voice="am_liam"
    )
    audio.save_wav("output.wav")
    print("Audio guardado en output.wav")