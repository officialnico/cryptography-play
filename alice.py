
class ProofGame:

    def __init__(self, prover: Prover, verifier: Verifier):
        self.prover = prover
        self.verifier = verifier

    def play(self):
        ...

class Prover:

    def __init__(self, discrete_log_key: dict = None, private_ID: int = None):
        self.discrete_log_key = discrete_log_key
        self.private_ID = private_ID

        self.generator = discrete_log_key.get(generator)
        self.prime = discrete_log_key.get(prime)
        self.output = discrete_log_key.get(output)

    def generate_ID(self, generator: int):
        