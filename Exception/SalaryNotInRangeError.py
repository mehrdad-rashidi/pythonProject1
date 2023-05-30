class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message.
# Then, the constructor of the parent Exception class is called manually with the self.message argument using super().
# The custom self.salary attribute is defined to be used later.
# The inherited __str__ method of the Exception class is then
# used to display the corresponding message when SalaryNotInRangeError is raised.

