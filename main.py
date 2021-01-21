# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger, operation
from unittest import main


print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True))
# print(arithmetic_arranger("300 - 6485"))
# print(operation(5, 7, '-'))


# Run unit tests automatically
main(module='test_module', exit=False)