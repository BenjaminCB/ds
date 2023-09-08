"""This module contains the code for the first exercise of the course."""

from emulators.Device import Device
from emulators.Medium import Medium
from emulators.MessageStub import MessageStub
import random


class GossipMessage(MessageStub):
    """A message that can be sent between devices in the gossip protocol."""

    def __init__(self, sender: int, destination: int, secrets):
        super().__init__(sender, destination)
        # we use a set to keep the "secrets" here
        self.secrets = secrets

    def __str__(self):
        return f'{self.source} -> {self.destination} : {self.secrets}'


class Gossip(Device):
    """A device that can participate in the gossip protocol."""

    def __init__(self, index: int, number_of_devices: int, medium: Medium):
        super().__init__(index, number_of_devices, medium)
        # for this exercise we use the index as the "secret",
        # but it could have been a new routing-table (for instance)
        # or sharing of all the public keys in a cryptographic system
        self._secrets = set([index])

    def _update_secrets(self):
        secrets = map(lambda msg: msg.secrets, self.medium().receive_all())
        secret_set = set()
        for secret in secrets:
            secret_set = secret_set.union(secret)
        self._secrets = self._secrets.union(secret_set)

    # tried some different stuff, this is not the prettiest solution with this result
    # but cant be botherd to change it now
    # it is essentially just a nested loop that sends the message to all devices
    def run(self):
        count = self.index() + 1
        while True:
            self._update_secrets()

            if count % self.number_of_devices() != self.index():
                msg = GossipMessage(self.index(), count % self.number_of_devices(), self._secrets)
                self.medium().send(msg)
                count += 1

            if len(self._secrets) == self.number_of_devices() and count % self.number_of_devices() == self.index():
                return

    def print_result(self):
        print(f'\tDevice {self.index()} got secrets: {self._secrets}')
