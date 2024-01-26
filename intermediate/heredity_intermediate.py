import csv
import argparse

# TODO HINT Workshop 4
def arg_parser():
    parser = argparse.ArgumentParser(
        prog='Hereditary Tree',
        description='Finds probabilities of inheriting trait for every person in a family'
    )
    # Define the command-line arguments.
    raise NotImplementedError


# TODO HINT: Workshop 4
def file_type_checker(extension):
    raise NotImplementedError


def main():
    # Parse the command-line arguments.
    ARGS = arg_parser()

    people = load_data(ARGS.i)

    # Keep track of gene and trait probabilities for each person

    probabilities = dict()

    for person, data in people.items():
        '''
        TODO: iterate over the 'trait' value of 'data' to assign the 
            correct value in probabilities. 
        
            probabilities should be structured as such:
            probabilities = {
                "person": {
                    "gene": {
                        2: 1,
                        1: 1, 
                        0: 0
                    }, 
                    "trait": 1
                }, 
                "person2": ...
            }
        '''
        raise NotImplementedError


    calculate_trait(probabilities, people)

    # names = set(people)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            if field.capitalize() == "Trait":
                print(f"  {field.capitalize()}: {probabilities[person][field]}")
                continue
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def calculate_trait(probabilities, people):
    for person, data in probabilities.items():
        if data['trait'] == None:
            '''
            TODO: fetch the father and mother genotypes from the 'person' we're looking at
                    using the people dictionary. Then assign the appropriate value in the
                    probabilities dictionary using the trait_helper() function.
            '''
            raise NotImplementedError
    


# calculates probability of a child having a trait given parent's trait & genotype information
# @returns an object to_return with 
def trait_helper(father, mother, probabilities, people):
    to_return = {
        "gene": {
            2: 0,
            1: 0,
            0: 0
        },
        "trait": 0
    }
    '''
    TODO: Given the two genotypes of parents as an input, known probabilities and
            family tree determine the correct possible genotypes and traits 
            to return. For the given person.

            Here we need to make sure that when we calculate probability for a 
            person X, the probabilities for 0,1,2 traits for their ancestors 
            are known. For instance, we have 3 generations and initially we only
            know the "trait" information of the grandparents. Then, if our code
            is iterating through the people in the order e.g. grandson first, 
            parent after, we would not be able to calculate probability of 
            grandson rightaway! There's 2 approaches you could use to tackle this:
            1. Build an actual heredity tree data structure and pre-order traverse it
                or use topological sort and traverse it.
            2. (An easier approach) Recursively call for trait_helper() whenever
            we don't know the genotype of the parent.
    '''


    raise NotImplementedError



def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # TODO: load data from each row into the dictionary data here
            raise NotImplementedError
    return data

# runs when we call the python file
if __name__ == "__main__":
    main()
