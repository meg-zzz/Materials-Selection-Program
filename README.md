# Materials Selection Program

Python program that uses data from the Materials Project API to help users identify materials based on composition, and selected material properties.
## Description

This program retrieves material data from the Materials Project API and allows the user to filter the results according to their requirements.

The available properties are:

- Density
- Bulk modulus
- Shear modulus
- Homogeneous Poisson's ratio
- Band gap
- Magnetic behaviour

Of which one or more can be selected.

Then, the program will ask the user to specify suitable minimum and/or maximum values for the selected properties. Boolean indexing is used to filter the found materials based on the specifications.

For bulk and shear modulus, the program accounts for the different values provided by the Materials Project API (Voigt, Reuss, vrh).

After filtering, the user can choose a property by which to sort the remaining materials and select either ascending or descending order.

The results include information such as the material ID, chemical formula, composition, warnings, and the selected material properties.

## Getting Started

### Dependencies

The program requires:

- Python 3
- `pymatgen`
- `mp-api`
- `pandas`
- A Materials Project API key

The program was developed using macOS, but should work on other operating systems with the required Python packages installed.

### Installing

1. Download or clone this repository from GitHub.

2. Open the project folder in a terminal.

3. Create a Python virtual environment and .env file OR skip step and replace API_KEY in:
   <img width="294" height="72" alt="image" src="https://github.com/user-attachments/assets/a8f9a570-4bf0-4046-bec3-a1351bf4cda2" />

   with your Materials Project API key.
4. Activate the virtual environment:

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

**On Windows:**

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install mp-api pymatgen pandas
```
## Executing the Program

1. Activate the virtual environment.

2. Run the program from the terminal:

```bash
python main.py
```

3. Enter the required elements.

For example:

```text
Elements needed separated by commas (eg. Fe, C): Fe, C
```

4. Select the required material properties for filtering.

For example:

```text
Please specify the desired properties separated by commas:
density, band_gap
```

5. Enter the minimum and maximum values for each property.

6. The program retrieves the relevant materials and applies the conditions.

7. Choose a property to sort the results by and select ascending or descending order.

8. Specify how many rows of results you would like to see.
   
10. The resulting DataFrame displays the materials that fit the specifications.

## Example

```text
Elements needed: Fe, C

Properties:
density, band_gap

Minimum density: 2
Maximum density: 10

Minimum band gap: 0
Maximum band gap: 2
```

Which would look something like this: 

<img width="764" height="630" alt="image" src="https://github.com/user-attachments/assets/0d9ecf8a-2e72-4f43-8c54-de3c7097daa2" />


## Technologies Used

- Python
- pandas
- Materials Project API
- pymatgen
- mp-api
- Boolean indexing
- List comprehensions
- Loops and conditional statements
- DataFrame manipulation

## Project Status

This project is currently under development. Additional features and improvements may be added in future versions.
