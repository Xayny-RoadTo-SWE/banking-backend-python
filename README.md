# Bank API - Banking System Backend
A banking backend application developed in Python that simulates core banking operations such as deposits, withdrawals, transfers, and account management. The project focuses on business rules implementation, transaction consistency, and secure financial operations.

## Business Rules
- Deposits must be greater than zero
- Withdrawals cannot exceed account balance
- Transfers are executed within a database transaction
- Transfers cannot be made to the same account
- All operations are recorded in transaction history

## Example Operations
- Create a new account
- Check account balance
- Deposit funds
- Withdraw funds
- Transfer money between accounts

## Tech Stack
- Python 3
- Postgres
- Docker
- CLI-based interface

## Architecture
The project follows a layered architecture:

- CLI / API Layer
- Service Layer
- Repository Layer
- Database Layer

# Technical Challenges
  This project was created to practice:

- Transaction management
- Database consistency
- Error handling
- Layered architecture
- Business rule implementation

## Project Status
This project is currently under active development.

Current implementation includes:

- User management
- Account operations
- Deposits
- Withdrawals
- Transfers

Future versions will focus on:

- Authentication and authorization
- Improved business rules
- Automated testing
- Docker deployment

## What I Learned
Through this project I practiced:

- Database transactions
- Backend architecture
- Error handling
- Business rule modeling
- State consistency

## How to Run

1. Clone the repository
```bash
git clone https://github.com/Alexsandra127/banking-backend-python.git
cd banking-backend-python
