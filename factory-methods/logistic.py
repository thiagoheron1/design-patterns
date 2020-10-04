from __future__ import annotations
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def planDelivery(self) -> str:
        transport = self.create_transport()
        print(transport.deliver())

# Logistics Classes
class RoadLogistic(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistic(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Transport Classes
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

class Truck(Transport):
    def deliver(self) -> str:
        return {"Deliver by Truck"}

class Ship(Transport):
    def deliver(self) -> str:
        return {"Deliver by Ship"}

# Client Code
def client_code(logistics: Logistics) -> None:
    logistics.planDelivery()


if __name__ == "__main__":
    print("App: Launched with Road Logistic")
    client_code(RoadLogistic())

    print("App: Launched with Sea Logistic")
    client_code(SeaLogistic())