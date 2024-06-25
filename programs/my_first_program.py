from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Secure comparison
    is_greater = my_int1 > my_int2
    is_equal = my_int1 == my_int2
    is_less = my_int1 < my_int2

    # Create outputs for the comparison results
    output_greater = Output(is_greater, "is_greater", party1)
    output_equal = Output(is_equal, "is_equal", party1)
    output_less = Output(is_less, "is_less", party1)

    return [output_greater, output_equal, output_less]

# Create the program with the new secure comparison logic
nada_main()
