[Home](../README.md)
# Together with "Working as a Business Analyst"

## Dates
- 21-09-2022 - Wednesday
- 30-11-2022 - Wednesday

## Case description
The company “KEA Retail Consult” sells software to supermarkets in Europe. The software is installed at the cash registers in the supermarkets. KEA Consult has more than 30 consultants employed visiting supermarkets all over Europe. Their job is to install or update the system.  

Each consultant must pay for his food, travel and accommodation when she is on the road. The expenses are reimbursed afterwards. 

In order for KEA Retail Consult to reimburse expenses each consultant has to register her expenses and attach a receipt as proof. There are typically three types of expenses: meals (breakfast, lunch and dinner), accommodation (hotel, b&b, etc) and transport (flight, car, train, bus).  

It is a very slow and not very streamlined approval process. Sometimes it takes months before the consultants are reimbursed and the money is put into their account.  With 10-20 travelling days a month it sometimes creates liquidity problems for the consultants. 

When a consultant has registered his expenses in their common spreadsheet, it first has to be approved by his manager. The consultant therefor sends a mail to his manager asking him to approve. 

The manager will make sure that the expenses were held at a time where she was travelling and that the type of expense and amount is reasonable. If not or receipts are missing the manager will email the employee and ask him to update or change his registration. 

Ones it has been approved the manager will forward the mail to the accounting department and ask them to transfer the money to the consultant’s bank account.  

The accounting department contacts the consultant before transferring the money to make sure that the bank account they have registered is correct.  

Both the managers and the accounting department must state in the spreadsheet, when they have approved and paid out the amount, but they quite often forget to do so. 

The managers and the director of KEA Retail Consult would like to have a better overview of the expenses on a monthly basis, so they know what kind of expenses there has been and how many requests that are awaiting approval or payment.  

The employees are frustrated because they have no way of knowing how far in the approval process their request is, so they must call or email their manager or the accounting department to get the information. 

## Files
The Excel file that “KEA Retail Consult” is using right now:

[expence_data.xlsx](./files/expence_data.xlsx)

## Your assignment Day 1:
Make a requirement spec for a new system to support the process. It has to be based on the data in the spreadsheet, but you are more than welcome to suggest improvements. 

Describe the users and context and the scope:
- List functional requirements 
- List requirements for improved processes
- Draw a datamodel 
- Create database in MySQL based on your datamodel and import data from the spreadsheet 
- Create an SQL file for creating the database and inserting data into the database

## Your assignment Day 2:
Implement based on Requirement spec and database from other group – make an application that can handle the needs of both consultants and managers