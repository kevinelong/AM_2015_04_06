function Employee( options ) {
    this.firstName = options.firstName;
    this.lastName = options.lastName;
    this.wage = options.wage;
    this.hireDate = options.hireDate;
    this.contactPhone = options.contactPhone;
}


function EmployeeFactory() {}
EmployeeFactory.prototype.createEmployee = function createEmployee ( options ) {
    return new Employee( options );
}

var anEmployeeFactory = new EmployeeFactory();
var newHire = anEmployeeFactory.createEmployee(
    {
        firstName : "Michael",
        lastName : "Fish",
        wage : 13.50,
        hireDate : "05/05/15"
    }
);

var raise_wage = function(employee, raise) {
    employee.wage += raise;
};

raise_wage(newHire, 1);

console.log(newHire.wage);

console.log(newHire.contactPhone);