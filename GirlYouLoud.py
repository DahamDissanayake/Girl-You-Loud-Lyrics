import sys 
from time import sleep

def boob():
    lyrics_with_duration = [
        "I put that diamond in you, boob", 1.32,
        "Put on your favorite birthday suit", 1.64,
        "I hit them lights, we in the mood", 1.15,
        "I'ma slide inside and don't you move", 1.80,
        "Scorpio, sex drive for two", 1.52,
        "Who else you know would die for you?", 1.64,
        "Them niggas ain't livin' that shit", 1.24,
        "I showed you shit them niggas won't ever do", 2.16,
        " ", 0.0,
        "This year I do my thing (thing)", 1.52,
        "'Bout to put that def to shame", 1.64,
        "So high, eyes low", 1.01,
        "How you scream my name the only time you use in vain", 2.18 
    ]
    
    line_delays = [0.28, 0.22, 0.25, 0.25, 0.25, 0.21, 0.27, 0.25, 0.25, 0.25, 0.20]

    lyrics = [lyrics_with_duration[i] for i in range(0, len(lyrics_with_duration), 2)]
    durations = [lyrics_with_duration[i] for i in range(1, len(lyrics_with_duration), 2)]
    
    for index, lyric in enumerate(lyrics):
        typing_duration = durations[index]
        
        char_delay = typing_duration / len(lyric)
        
        for char in lyric:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
        
        print()
        
        if index < len(line_delays):
            sleep(line_delays[index])

if __name__ == "__main__":
    boob()
    print("\n---")