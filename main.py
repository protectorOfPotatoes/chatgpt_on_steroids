import proj0 as z
import proj1 as o
import subprocess as s


if __name__ == '__main__':
    print("============RECORDING=============")
    s.run(['rec', '-r', '44100', '-c', '2', '-b', '16', 'output.wav', 'trim', '0', '10'])

    print("========RECORDING COMPLETED=========")
    print("Processing...")
    text = z.whisper()
    f_args = o.respond(text) #f_args means final args
    s.call(['espeak', f_args])
    s.call(['rm', 'output.wav'])


