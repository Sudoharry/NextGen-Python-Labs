# Abstraction – CloudService Blueprint

from abc import ABC, abstractmethod


class CloudService(ABC):
    @abstractmethod
    def deploy(self):
        pass


class AWS(CloudService):
    def deploy(self):
        return "Provision infrastructure on AWS EC2"
    
class GCP(CloudService):
    def deploy(self):
        return "Provision infrastructure on GCP Compute Enginer"


providers = [AWS(), GCP()]

for p in providers:
    print(p.deploy())

# 🧠 Concepts: Abstraction (via ABC), Interface-like behavior, Polymorphism