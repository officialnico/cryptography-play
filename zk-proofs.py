
"""This is a module related to Discrete Log and Zero Knowledge Proofs. 

The goal is to make this document computable:
https://people.eecs.berkeley.edu/~jfc/cs174/lecs/lec24/lec24.pdf
"""

class ProofGame:
    """
    This simuates a game between the Prover and the Verifier as outlined 
    in the paper. 


    """

   def __init__(self, prover: Prover, verifier: Verifier):
      self.prover = prover
      self.verifier = verifier

   def play(self):
        self.prover.set_random_value()
        initial_value = self.prover.generate_initial_value()
        self.verifier.set_random_bit()
        response_value = self.prover.generate_response_value(self.verifier.bit)

        is_verified = self.verifier.verify_identity(self.prover.public_key, initial_value, response_value)

        return is_verified, initial_value, response_value

class Prover:
    """
    This agent is responsible for proving they know something. 
    """

    def __init__(self, discrete_log_key: dict = None, private_ID: int = None):
        """
        Initialize 
        """

        self.discrete_log_key = discrete_log_key
        self.private_ID = private_ID 

        self.generator = discrete_log_key.get(generator) 
        self.prime = discrete_log_key.get(prime)
        self.output = discrete_log_key.get(output)

        
    def generate_private_ID(self, generator: int, ):
        """
        Generate an ID that can be used in a particular context. 
        """

        #TODO

    def generate_initial_value(self, rand_value=None):
        A = self.public_key['generator']
        p = self.public_key['prime']
        if rand_value is None:
            r = self.random_value
        else:
            r = rand_value
        h = pow(A, r, p)
        return h

    def generate_response_value(self, bit_b: int) -> int:
        p = self.public_key['prime']
        x = self.secret_id
        r = self.random_value
        s = (r + bit_b * x) % (p - 1)
        return s

    def set_random_value(self):
        self.random_value = random.randint(1, self.public_key['prime'])


class Verifier:
    """
    This agent is responsible for verifying that a Prover has the knowledge they claim. 
    """
    def __init__(self, bit, prime):
        self.bit = bit
        self.prime = prime

    def set_random_bit(self):
        self.bit = random.randint(0, 1)

    def verify_identity(self, public_key=None, initial_val=None, response_val=None):
        s = response_val
        A = public_key.get('generator')
        h = initial_val
        B = public_key.get('output')
        p = self.prime
        b = self.bit
        first_val = pow(A, s, p)
        second_val = (h * pow(B, b, p)) % p
        truth_val = (first_val == second_val)
        return truth_val


class Assistant:
    """
    This is a helper class for doing intermediate calculations related to the game. 
    """


