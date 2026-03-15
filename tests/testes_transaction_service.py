from unittest import TestCase
from unittest.mock import patch
from fastapi import HTTPException

from services.transactions_service import TransactionService

class TestTransactionService(TestCase):

    @patch("services.transactions_service.TransactionsRepository.get_transaction_by_id")
    def test_get_transaction_by_id_success(self, mock_get_transaction_by_id):       
        mock_get_transaction_by_id.return_value = {
            "customer_origin": 1,
            "customer_destination": 2,
            "transaction_type": "transfer",
            "amount": 100.50
        }
        
        result = TransactionService.get_transaction_by_id(1)
        self.assertEqual(result, {
            "transaction": {
                "customer_origin": 1,
                "customer_dest": 2,
                "operation": "transfer",
                "amount": 100.50
            }
        })
    @patch("services.transactions_service.TransactionsRepository.list_transactions_by_customer")
    def test_list_transactions_by_customer(self, mock_list_transactions_by_customer):
        mock_list_transactions_by_customer.return_value = [
            {
                "customer_origin": 1,
                "customer_destination": 2,
                "transaction_type": "transfer",
                "amount": 100.50
            },
            {
                "customer_origin": 1,
                "customer_destination": 3,
                "transaction_type": "deposit",
                "amount": 200.00                                                                    
            }
        ]
        result = TransactionService.list_transactions_by_customer(1)
        
        self.assertEqual(result, {
            "transactions": [
                {
                    "customer_origin": 1,
                    "customer_dest": 2,
                    "operation": "transfer",
                    "amount": 100.50
                },
                {
                    "customer_origin": 1,
                    "customer_dest": 3,
                    "operation": "deposit",
                    "amount": 200.00                                                                    
                }
            ]
        })
        
    @patch("services.transactions_service.TransactionsRepository.list_transactions_by_customer")
    def test_list_transactions_by_customer_empty(self, mock_list_transactions_by_customer):
        mock_list_transactions_by_customer.return_value = []
        result = TransactionService.list_transactions_by_customer(1)
        self.assertEqual(result, {
            "transactions": []
        })          
        
        @patch("services.transactions_service.TransactionsRepository.get_transaction_by_id")
        def test_get_transaction_by_id_not_found(self, mock_get_transaction_by_id):
            mock_get_transaction_by_id.return_value = None

        with self.assertRaises(HTTPException) as context:
            TransactionService.get_transaction_by_id(1)

        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Transaction not found")