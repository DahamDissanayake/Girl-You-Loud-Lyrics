import sys
from time import sleep
import time

def for_sanu():
    # List with lyrics and their typing durations (alternating: lyric, duration)
    lyrics_with_duration = [
        "Walking down the street with my head up high", 2.5,
        "Looking at the stars in the midnight sky", 2.0,
        "Dreams are calling out my name tonight", 2.2,
        "Everything's gonna be alright", 1.8,
        "Music playing in my heart so loud", 2.3,
        "Standing strong and standing proud", 2.0,
        "This is my moment, this is my time", 2.4,
        "Watch me climb, watch me shine", 1.9
    ]
    
    # List of delays between each line (in seconds)
    line_delays = [1.0, 1.2, 0.8, 1.5, 1.1, 0.9, 1.3, 2.0]
    
    # Extract just the lyrics for processing
    lyrics = [lyrics_with_duration[i] for i in range(0, len(lyrics_with_duration), 2)]
    durations = [lyrics_with_duration[i] for i in range(1, len(lyrics_with_duration), 2)]
    
    for index, lyric in enumerate(lyrics):
        # Get the duration for typing this line
        typing_duration = durations[index]
        
        # Calculate delay between each character for typing effect
        char_delay = typing_duration / len(lyric)
        
        # Type out the lyric character by character
        for char in lyric:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
        
        # Print newline after the complete lyric
        print()
        
        # Add delay before next line (if not the last line)
        if index < len(line_delays):
            sleep(line_delays[index])

# Run the function
if __name__ == "__main__":
    print("Starting lyrics display...\n")
    sleep(1)  # Initial pause
    for_sanu()
    print("\nLyrics display completed!")