from tkinter import Tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def FFT_analysis(file_path):
    data = np.loadtxt(file_path)
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]

    N = len(x)
    Fs = 50  # Sampling rate (Hz)

    fft_x = np.fft.fft(x)
    fft_y = np.fft.fft(y)
    fft_z = np.fft.fft(z)

    fft_frq = np.fft.fftfreq(N, d=1/Fs)
    half_N = N // 2

    plt.figure(figsize=(12, 6))
    plt.plot(fft_frq[:half_N], np.abs(fft_x[:half_N]), label='X-axis')
    plt.plot(fft_frq[:half_N], np.abs(fft_y[:half_N]), label='Y-axis')
    plt.plot(fft_frq[:half_N], np.abs(fft_z[:half_N]), label='Z-axis')

    plt.title("FFT of 3-Axis Acceleration")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("FFT analysis for X, Y, Z axes displayed.")


def main():
    Tk().withdraw()

    file_path = askopenfilename(
        title="Select Data File",
        filetypes=[("Text or CSV Files", "*.txt *.csv")]
    )
    if not file_path:
        print("No file selected.")
        return

    print("Uploaded file is analysised")
    FFT_analysis(file_path)

if __name__ == "__main__":
    main()