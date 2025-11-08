# Hbeat – Heart Stroke Risk Analyzer

Hbeat is a command-line application that predicts potential heart disease risk using a machine-learning model. Users supply patient health parameters through command-line arguments, and the tool processes these inputs to generate a risk assessment.

This project is designed for educational and prototyping purposes only. It must not be used for real medical diagnosis or clinical decision-making.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Required Arguments](#required-arguments)
  - [Optional Arguments](#optional-arguments)
- [Output](#output)
- [Model Information](#model-information)
- [Disclaimer](#disclaimer)
---

## Overview

Hbeat evaluates patient indicators such as age, blood pressure, chest pain type, cholesterol level, oxygen levels, hereditary factors, and more. Using a pre-trained `.joblib` model, the tool estimates whether the patient may be at risk of heart disease.

The application is lightweight, fast, and suitable for experimentation with various machine-learning models.

---

## Features

- Clean and efficient command-line interface  
- Accepts required and optional physiological parameters  
- Supports custom model loading via `--model` argument  
- Produces clear, interpretable prediction output  
- Minimal dependencies for easy setup  
- Extensible structure for ML model experimentation  

---

## Installation

### Prerequisites

Ensure your environment includes:

- Python 3.8 or later  
- `joblib`  
- `pandas`  

### Install Dependencies

```bash
pip install joblib pandas
```
### Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```
## Usage

### Basic Command Example

```bash
python Hbeat.py 56 1 1 120 236 0 124
```
### Full Usage Example with Optional Parameters

```bash
python Hbeat.py 56 1 1 120 236 0 124 \
    --inherited 1 \
    --oxygenlevels 2 \
    --aw 79.825 \
    --model "./models/alt_Hbeat.joblib"
```

## Required Arguments

| Argument     | Type | Description |
|--------------|------|-------------|
| `Age`        | int  | Age of the patient |
| `Sex`        | int  | 0 = Female, 1 = Male |
| `Chestpain`  | int  | Chest pain type (0–3) |
| `BP`         | int  | Resting blood pressure (mm Hg) |
| `Cholestrol` | int  | Serum cholesterol (mg/dl) |
| `Sugar`      | int  | Fasting blood sugar >120 mg/dl (1=True, 0=False) |
| `HeartRate`  | int  | Maximum heart rate achieved |

## Optional Arguments

| Flag              | Type  | Default       | Description |
|-------------------|--------|---------------|-------------|
| `--inherited`     | int    | 0             | Family history of heart disease (1=True, 0=False) |
| `--oxygenlevels`  | int    | 1             | Oxygen level indicator |
| `--aw`            | float  | 0.0           | Artery width measurement |
| `--model`         | str    | Hbeat.joblib  | Path to a custom machine-learning model |

## Output

Hbeat returns one of the following results:

### Risk Detected

Prediction: risk of heart disease detected. Please consult a doctor.
Data:
   <input dataframe>

### No Significant Risk

Prediction: No significant heart risk detected. Stay healthy!

### Unexpected Output

Unexpected prediction value: <value>

## Model Information

Hbeat requires a machine-learning model trained using the following features:

- Age
- Sex
- Chestpain
- BP
- Cholestrol
- Sugar
- HeartRate
- Inherited
- Oxygenlevels
- AW

The model must be:

- Saved in `.joblib` format  
- Compatible with scikit-learn or similar frameworks  
- Structured to accept the exact feature order and names listed above

## Disclaimer

This project is intended strictly for educational, research, and demonstration purposes.  
It is not a medical device and must not be used for diagnosis, treatment, or clinical decision-making.  
Always consult a licensed healthcare professional for medical advice and evaluation.


