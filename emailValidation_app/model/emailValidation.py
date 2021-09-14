from emailValidation_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__( self, data ):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_email(email):
        is_valid = True
        flash("The email address you entered (ASK HOW TO PASS IN ENTERED EMAIL ADDRESS) is a VALID email address! Thank you!", "success")
        if not EMAIL_REGEX.match(email["email"]):
            flash("Invalid email address!", "email")
            is_valid = False
        return is_valid

    @classmethod
    def add_email(cls, data):
        query="INSERT INTO emails (email) VALUES ( %(email)s );"
        results = connectToMySQL("emailValidation_schema").query_db(query, data)
        return results

    @classmethod
    def all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("emailValidation_schema").query_db(query)
        all_emails = []
        for row in results:
            all_emails.append(cls(row))
        return all_emails
