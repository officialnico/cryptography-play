
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
      # TODO: implement the logic 

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

        
        

    def generate_ID(self, generator: int, ):
        """
        Generate an ID that can be used in a particular context. 
        """

class Verifier:
    """
    This agents verifies another agent's proof of certain knowledge.  
    """

class Assistant:
    """
    
    """

