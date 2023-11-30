import numpy as np
import sounddevice as sd
import time

# Mapeamento de notas para frequências
note_mapping = {
    # Do maior
    "C": 261.63,  # Dó central (C4)
    "C#": 277.18,  # Dó sustenido (C#4)
    "D": 293.66, # Ré central (D4)
    "D#": 311.13, # Ré sustenido (D#4)
    "E": 329.63, # Mi central (E4)
    "F": 349.23, # Fá central (F4)
    "F#": 369.99, # Fá sustenido (F#4)
    "G": 392.00, # Sol central (G4)
    "G#": 415.30, # Sol sustenido (G#4)
    "A": 440.00, # Lá central (A4)
    "A#": 466.16, # Lá sustenido (A#4)
    "B": 493.88, # Si central (B4)

}

# Melodia de "Jingle Bells" com pausas indicadas por "R"
# melody = [
#     "B", "B", "B", "R",
#     "B", "B", "B", "R",
#     "B", "D", "G", "A", "B", "R",
#     "C", "C", "C", "R",
#     "B", "B", "B", "R",
#     "B", "A", "A", "B", "A", "D",
#     "B", "B", "B", "R",
#     "B", "B", "B", "R",
#     "B", "D", "G", "A", "B", "R",
#     "C", "C", "C", "R",
#     "B", "B", "B", "R",
#     "D", "D", "C", "A", "B", "R",
# ]

# Melodia de "Tocam os Sinos" com pausas indicadas por "R"
# melody = [
#     "F#", "F#", "F#", "F#",
#     "F#", "F#", "F#", "F#", "R",
#     "F#", "A", "D", "E", "F#", "R",
#     "G", "G", "G", "G",
#     "G", "F#", "F#", "F#", "R",
#     "F#", "E", "E", "F#", "E", "A", "R",
# ]

# Melodia de "Hino nacional brasileiro" com pausas indicadas por "R"
melody = [
    "C", "F", "E", "F", "G", "A", "G", "A", "A#", "B", "C", "F",
    "C", "F", "E", "G", "F", "A", "G", "A#", "A", "F#", "G", "R",
    "D", "G", "F#", "G", "A", "A#", "A", "A#", "C#", "C#", "D", "G", "R",
    "C", "G", "F#", "A", "G", "A#", "A", "C", "A#", "G#", "A", "R",
    "A", "A", "A#", "A", "A", "A#", "A", "A", "D", "R",
    "C", "A#", "A#", "A", "A", "G", "G", "F", "F", "E", "E", "D", "R",
    "G", "G", "A", "G", "G", "A", "G", "G", "C", "R",
    "B", "A", "A", "G", "G", "F", "F", "E", "E", "D", "D", "C", "R",
    "C", "E", "G", "A#",
    "C", "E", "G", "A#",
    "C", "E", "G", "A#", "A#", "R",
]

# Durações correspondentes às notas (em segundos)
note_durations = {
    "whole": 1.0,  # semibreve
    "half": 0.5,  # mínima
    "quarter": 0.25,  # semínima
    "eighth": 0.125,  # colcheia
}

def play_note(note, duration, amplitude=0.1):
    frequency = note_mapping[note]
    sample_rate = 44100

    # Gere uma onda senoidal para a nota
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)

    # Reproduza a onda sonora
    sd.play(wave, samplerate=sample_rate, blocking=True)

def main():
    # Reproduza a melodia de "Jingle Bells" com pausas indicadas na melodia
    while True:
        for note, duration in zip(melody, ["quarter"] * len(melody)):
            if note == "R":  # Se a nota for "R", adicione uma pausa
                time.sleep(note_durations[duration])
            else:
                play_note(note, note_durations[duration], amplitude=0.1)

            print(note)

if __name__ == "__main__":
    main()
