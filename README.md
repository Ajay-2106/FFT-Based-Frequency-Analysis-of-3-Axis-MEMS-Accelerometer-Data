# FFT-Based Frequency Analysis of 3-Axis MEMS Accelerometer Data

This Python tool allows users to perform a Fast Fourier Transform (FFT) on acceleration data collected from MEMS sensors (e.g., X, Y, Z axes) and visualize the frequency spectrum for each axis.

## 📌 Features

- GUI-based file selection (TXT or CSV)
- Parses 3-axis space-separated data (X, Y, Z)
- Performs FFT for each axis
- Visualizes the frequency spectrum using `matplotlib`
- Clean and simple interface for data inspection

---

## 📂 Input Data Format

The input file should be a **space-separated** text file or CSV file with **three columns**, representing X, Y, and Z axis acceleration data and No headers should be included in the file.

---

## 🚀 Getting Started

### 🧰 Requirements

- Python 3.x
- numpy
- matplotlib
- tkinter (comes pre-installed with Python)
