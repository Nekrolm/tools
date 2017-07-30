"""
   Usage:
      wav_concat w1 [w2 [w3 ...]] wOut
   Concat wavs with same configuration (nchanels, samplerate, samplewidth)
"""

import wave
import sys



def main():
    out = wave.open(sys.argv[-1], "w")
    W = sys.argv[1:-1]
    out.setparams(wave.open(W[0]).getparams())
    for w in W:
        f = wave.open(w)
        out.writeframesraw(f.readframes(f.getnframes()))
    out.close()
    


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main()
    else:
        print(__doc__)
