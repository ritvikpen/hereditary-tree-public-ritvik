import csv
import argparse

# really cool code

# TODO HINT Workshop 4
def arg_parser():
    parser = argparse.ArgumentParser(
        prog='Hereditary Tree',
        description='Finds probabilities of inheriting trait for every person in a family'
    )
    # Define the command-line arguments.
    raise NotImplementedError


# TODO IMPLEMENT. HINT: Workshop 4
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



    # calculate_trait will determine the phenotype('trait') based on genotype
    calculate_trait(probabilities, people)

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

# This method will determine 
def calculate_trait(probabilities, people):
    for person, data in probabilities.items():
        # we only want to calculate the trait when it is set to None
        if data['trait'] == None:
            '''
            TODO: fetch the father and mother genotypes from the 'person' we're looking at
                    using the people dictionary. Then assign the appropriate value in the
                    probabilities dictionary using the trait_helper() function.
            '''
            raise NotImplementedError

# Note: This method will only work for beginners part of the project.
# Here we just walk through the gene and check what genotype the parent has
# Since it is only 0 or 2 for the beginner case, we can just return true
# Whenever one of the values of the dictionary is 1
def parent_genotype(gene):
    for key, val in gene.items():
        if val == 1:
            return key

# calculates probability of a child having a trait given parent's trait & genotype information
def trait_helper(genes1, genes2):
    to_return = {
        "gene": {
            2: 0,
            1: 0,
            0: 0
        },
        "trait": 0
    }
    '''
    TODO: Given the two genotypes passed in to this function, 
            determine the correct possible genotypes and traits 
            to return. 

            For example, if we had an example_dict that we wanted
            to return, we would fill it with the possibility it could
            have 0, 1, or 2 of the alleles of interest by labelling it with
            example_dict['gene'][0] = ? ; example_dict['gene'][1] = ? ;
            example_dict['gene'][2] = ?. We could also determine the probability
            that it could inherit the trait and store it in example_dict['trait]
            with values such as 1, 0.5, 0.25, etc.
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
