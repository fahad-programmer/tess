import random

def greet_main():
    options = ["hi", "hello! sir", "hey there!", "hi, good to have u back"]
    return(random.choice(options))

def saying_bye_main():
    options = ["bye", "see you soon take care!", "sad to say u bye hope to see u soon!", "bye take care", "will be waiting"]
    return(random.choice(options))

def saying_thanks_main():
    options = ["Mine Pleasure!", "Always at your service", "Always there for you.", "Mention Not!"]
    return (random.choice(options))
