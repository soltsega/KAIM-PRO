# KAIM Internship: Solar Data Discovery Project

## Overview

This project is part of the KAIM internship, focusing on the analysis of solar farm data from three countries: Benin, Sierra Leone, and Togo. The goal is to perform exploratory data analysis (EDA) on solar radiation measurements to inform strategic solar investments by MoonLight Energy Solutions.

## Project Structure for the Main Branch

```
KAIM-PRO
├── .github/
│   └── workflows/
│       └── CI.yml
├── .venv/
├── Include/
├── Lib/
├── Scripts/
├── launch.json
├── settings.json
├── pyvenv.cfg
├── .gitignore
├── .vscode/
├── data/
│   ├── benin-malanville.csv
│   ├── sierra-leone-bumbuna.csv
│   ├── togo-dapaong_qc.csv
│   └── processed/
│       ├── benin_clean.csv
│       ├── sierra_leone_clean.csv
│       └── togo_clean.csv
├── metadata/
│   └── data_description.md
├── notebook/
│   ├── eda_benin.ipynb
│   ├── eda_sierra_leone.ipynb
│   └── eda_togo.ipynb
├── src/
│   ├── __init__.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Branches

This project utilizes the following branches for development:

- **main**: Contains the stable version of the code.
- **dev**: For ongoing development and features.
- **eda-benin**: Focused on exploratory data analysis for Benin.
- **eda-sierra-leone**: Focused on exploratory data analysis for Sierra Leone.
- **eda-togo**: Focused on exploratory data analysis for Togo.

## Business Objective

MoonLight Energy Solutions aims to enhance operational efficiency and sustainability through targeted solar investments. This analysis will help identify high-potential regions for solar installations based on statistical analysis and EDA insights.

## Dataset Overview

The datasets include various environmental measurements relevant to solar energy production. Each CSV file contains the following columns:

- **Timestamp**: Date and time of the observation.
- **GHI (W/m²)**: Global Horizontal Irradiance.
- **DNI (W/m²)**: Direct Normal Irradiance.
- **DHI (W/m²)**: Diffuse Horizontal Irradiance.
- **Tamb (°C)**: Ambient Temperature.
- **RH (%)**: Relative Humidity.
- **WS (m/s)**: Wind Speed.
- **Precipitation (mm/min)**: Precipitation rate.
- **Cleaning**: Indicates if cleaning occurred (1 or 0).

### Data Files

- `benin-malanville.csv`: Contains solar data for Benin.
- `sierra-leone-bumbuna.csv`: Contains solar data for Sierra Leone.
- `togo-dapaong_qc.csv`: Contains solar data for Togo.
- `processed/`: Directory containing cleaned datasets:
  - `benin_clean.csv`: Cleaned solar data for Benin.
  - `sierra_leone_clean.csv`: Cleaned solar data for Sierra Leone.
  - `togo_clean.csv`: Cleaned solar data for Togo.

### Metadata

Refer to `metadata/data_description.md` for detailed descriptions of the dataset and its columns.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/KAIM-PRO.git
   cd KAIM-PRO
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To perform exploratory data analysis, navigate to the corresponding notebook files and execute the cells. For example, to analyze the data for Benin:

```bash
jupyter notebook
```

Then open the relevant notebook and run the cells.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request for any improvements or bug fixes.

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## Contact

For inquiries or further information, please contact:

tsegasolomon538@gmail.com  
- GitHub: [soltsega](https://github.com/soltsega)

This README aims to provide a comprehensive overview of the project, including its structure, objectives, and how to get started. Adjust any specific details as necessary!
```