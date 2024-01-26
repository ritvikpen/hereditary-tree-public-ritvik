# Hereditary Tree

## Overview

This directory serves as a project for UBIC's Workshop Series, WI24. Currently there are 2 levels of difficulty to the hereditary tree project: one of beginner and one of intermediate difficulty. Each difficulty can be found in the corresponding directory. 

## Getting Started

1. Make sure you have Python installed. Mac users have python pre-installed, for Windows and Linux go to [official Python website](https://www.python.org/downloads/). We recommend following some YouTube video on how to install Python, to ensure that everything goes right! To check that Python is installed run this in the terminal:
* Windows & Linux:
  ```
  python --version
  ```

* Mac:
  ```
  python3 --version
  ```
2. Install VS Studio Code if you haven't done so yet. Here's a great intro tutorial to VS Studio Code https://youtu.be/ORrELERGIHs?si=i1y8RGEpFSftlJi7

3. Install Github Desktop. Here is a beginner friendly tutorial: https://youtu.be/8Dd7KRpKeaE?si=VMxvgYu_c-XXqgjT

4. Get started with the project by forking this repository to create your own GitHub repository. Don't forget to invite collaborators, your teammates, in **repo**'s settings (**repo** – short for repository).

5. When working on beginner/intermediate steps of the project, don't forget to switch into the right folder when running code. In the example below, pay attention that I'm in `intermediate` folder:
    ```bash
    stephengolzari@Stephens-MacBook-Pro intermediate % python3 heredity_intermediate.py ./data/family1.csv   
    ```

    To change directory use `./cd/{directory-name}` in the terminal

Now let's go through the details of the project!

## Project Details

The whole project can be summed up by the following sentence: given a hereditary tree of the family and information about mutated trait for some members of the family, return probability of each person in the family having the trait.

### Command Line

```bash
python heredity.py data.csv
```

- `data.csv`: Input file in CSV format containing the family tree information. The file should have columns for "name," "mother," "father," and "trait."

### Input File Format

The input CSV file should have the following columns:

- **name**: The name of the individual.
- **mother**: The name of the mother (or leave it blank if unknown).
- **father**: The name of the father (or leave it blank if unknown).
- **trait**: The trait information, represented as 0 (absence of trait), 1 (presence of trait), or blank (unknown trait).

## Functionality

1. **Probability Calculation:**
   - The script calculates the probabilities of each individual having the specified trait based on the trait information of their parents.
   - It considers the genetic inheritance probabilities through the family tree.

2. **Output:**
   - The script outputs the probabilities for each individual, showing the likelihood of having the trait and the genetic makeup.

3. **Handling Unknown Traits:** - intermediate level
   - When an individual's trait is unknown, the script should explore the family tree to infer probabilities based on the traits of the known relatives.

## Customization

The script uses command-line arguments and allows users to customize the input file and functionality. The `arg_parser` function defines the command-line arguments, and the script can be modified for additional customization.

## Example

Consider the following family tree in `data.csv`:

```csv
name,mother,father,trait
Arthur,,,1
Molly,,,0
Jane,,,1
Tiffany,,,0
Charlie,Molly,Arthur,
Fred,Molly,Arthur,
Sarah,Jane,Charlie,
Ritvik,Tiffany,Fred
Wonka,Sarah,Ritvik
```

Running the script (here example for intermediate solution on family1.csv dataset):

```bash
python heredity_intermediate.py ./data/family1.csv
```

The output might look like:

```
Arthur:
  Gene:
    2: 1.0000
    1: 0.0000
    0: 0.0000
  Trait: 1.0
Molly:
  Gene:
    2: 0.0000
    1: 0.0000
    0: 1.0000
  Trait: 0.0
Jane:
  Gene:
    2: 1.0000
    1: 0.0000
    0: 0.0000
  Trait: 1.0
Tiffany:
  Gene:
    2: 0.0000
    1: 0.0000
    0: 1.0000
  Trait: 0.0
Charlie:
  Gene:
    2: 0.0000
    1: 1.0000
    0: 0.0000
  Trait: 0.0
Fred:
  Gene:
    2: 0.0000
    1: 1.0000
    0: 0.0000
  Trait: 0.0
Sarah:
  Gene:
    2: 0.5000
    1: 0.5000
    0: 0.0000
  Trait: 0.5
Ritvik:
  Gene:
    2: 0.0000
    1: 0.5000
    0: 0.5000
  Trait: 0.0
Wonka:
  Gene:
    2: 0.1875
    1: 0.6250
    0: 0.1875
  Trait: 0.1875
```

## Error Handling

The script includes error handling for incorrect command-line usage and checks for the correct file extension.

## Note

This README serves as documentation for the usage and functionality of the `heredity.py` script. Users can refer to this information to understand how to use and customize the script for their specific needs.

This script is part of a broader computational genetics project and serves as a foundation for understanding the probabilities associated with genetic inheritance and traits.

Feel free to explore and modify the script to suit your specific genetic data and research requirements.