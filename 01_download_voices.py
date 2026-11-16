from pykokoro import KokoroSynthesizer, SynthesisConfig, GenerationConfig

for voz in ["af_heart", "am_liam"]:
    config = SynthesisConfig(voice=voz, generation=GenerationConfig(lang="en-us"))
    with KokoroSynthesizer(config):
        pass