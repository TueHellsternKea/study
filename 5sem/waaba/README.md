[Home](../README.md)
# Together with "Working as a Business Analyst"

![](./kea_retail_consult.png)

# Content
- [Date](#dates)
- [Case description](#case-description)
- [Your assignment day 1](#your-assignment-day-1)
- [Your assignment day 2](#your-assignment-day-2)
- [Groups](#groups)
- [Files](#files)
- [Videos](#videos)

## Dates
- 21-09-2022 - Wednesday
- 30-11-2022 - Wednesday

## Case description
The company “KEA Retail Consult” sells software to supermarkets in Europe. The software is installed at the cash registers in the supermarkets. KEA Consult has more than 30 consultants employed visiting supermarkets all over Europe. Their job is to install or update the software.   

Each consultant must pay for his own food, travel and accommodation when she is on the road. The expenses are reimbursed afterwards.  

For KEA Retail Consult to reimburse expenses each consultant must register her expenses and attach a receipt as proof. There are typically three types of expenses: meals (breakfast, lunch and dinner), accommodation (hotel, b&b, etc) and transport (flight, car, train, bus).   

It is a very slow and not very streamlined approval process. Sometimes it takes months before the consultants are reimbursed and the money is put into their account.  With 10-20 travelling days a month it sometimes creates liquidity problems for the consultants.  

When a consultant has registered his expenses in their common spreadsheet, it must be approved by his manager. The consultant therefor sends a mail to his manager asking him to approve.  

The manager will make sure that the expenses were held at a time where she was travelling and that the type of expense and the amount is reasonable. If not or receipts are missing the manager will email the employee and ask him to update or change his registration.  

Once the expense has been approved the manager will forward the mail to the accounting department and ask them to transfer the money to the consultant’s bank account.   

The accounting department contacts the consultant before transferring the money to make sure that the bank account they have registered is correct.   

Both the managers and the accounting department must state in the spreadsheet, when they have approved and paid out the amount, but they quite often forget to do so.  

The employees are frustrated because they have no way of knowing how far in the approval process their request is, so they must call or email their manager or the accounting department to get the information.  

The managers and the director of KEA Retail Consult would like to have a better overview of the expenses on a monthly basis, so they can keep track of the different expenses. They would also like to keep an eye on how many requests that are awaiting approval or payment.  

The Excel file that “KEA Retail Consult” is using right now: [expence_data.xlsx](./files/expence_data.xlsx)

## Your assignment Day 1:
Based on the description about the current processes and the data in the spreadsheet, make a requirement specification for a new system to support the reimbursement process in KEA Retail consult.  

Your specification should include the following:     

- System scope
- Business needs  
- The identified users  
- Relevant user stories  
- Identified problems and gaps in the current processes (as-is)  
- Identified business rules/decisions  
- Illustration of the to-be process  
- Data required in the system  
- Flow of data in the system  
- How data should be structured when at rest (E/R diagram)  
- List functional requirements

You also need to create a database in MySQL based on your E/R diagram and import data from the spreadsheet  

Your SQL file, that can be used to create the database and insert data into the database, and the requirement specification must be handed in as a group assignment on Fronter. **If you are not done by the end of today's lectures, hand it in at the latest on October 5th**.  

## Your assignment Day 2:
Implement based on Requirement spec and database from other group – make an application that can handle the needs of both consultants and managers.

## Groups
We have created the groups for the 2 days:
- [Groups](./files/KNY-WaaB.pdf)

## Files
The Excel file that “KEA Retail Consult” is using right now:
- [expence_data.xlsx](./files/expence_data.xlsx)

## Videos

### Ekstra
- [Real-World Examples of Microsoft Power Automate in Action - 55 minutter](https://videos.microsoft.com/cloud/watch/b3RqhL5q11xD7EBQTqLrpg?)


## Guides

### Import from Excel into MySQL
First you have to svare the Excel files as CSV.

<div style="position: relative; padding-bottom: 71.23287671232877%; height: 0;"><iframe src="https://www.loom.com/embed/ad9bf3a19b6c4b2c868e1b692f08cfea" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Then you have to import the CSV file in MySQL

