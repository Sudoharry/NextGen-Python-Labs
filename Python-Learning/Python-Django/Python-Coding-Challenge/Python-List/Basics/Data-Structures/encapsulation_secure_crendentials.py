# Encapsulation – Secure Credentials

class Vault:
    def __init__(self, api_key):
        self.__api_key = "secret_key_123" # Private attribute

    def get_key(self):
        return f"Accessing the{self.__api_key}"

vault =  Vault()
print(vault.get_key())

# Accessing directly like vault.__api_key would fail
# 🧠 Concepts: Encapsulation, Access Control

