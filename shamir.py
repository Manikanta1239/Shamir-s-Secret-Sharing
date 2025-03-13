import numpy as np
from sympy import randprime
from typing import List, Tuple

class ShamirSecretSharing:
    def __init__(self, prime: int = None):
        """Initialize with an optional prime number for the field"""
        self.prime = prime or randprime(2**127, 2**128)
    
    def _generate_polynomial(self, secret: int, degree: int) -> List[int]:
        """Generate a random polynomial with given secret as free term"""
        coefficients = [secret]
        coefficients.extend(np.random.randint(0, self.prime, degree))
        return coefficients
    
    def _evaluate_polynomial(self, coefficients: List[int], x: int) -> int:
        """Evaluate polynomial at point x"""
        result = 0
        for coeff in reversed(coefficients):
            result = (result * x + coeff) % self.prime
        return result
    
    def split_secret(self, secret: str, n_shares: int, threshold: int) -> List[Tuple[int, int]]:
        """Split a secret into n shares with threshold requirement"""
        if threshold > n_shares:
            raise ValueError("Threshold cannot be greater than number of shares")
        
        # Convert secret to integer
        secret_int = int.from_bytes(secret.encode(), 'big')
        
        # Generate polynomial coefficients
        coeffs = self._generate_polynomial(secret_int, threshold - 1)
        
        # Generate shares
        shares = []
        for i in range(1, n_shares + 1):
            shares.append((i, self._evaluate_polynomial(coeffs, i)))
        
        return shares
    
    def _lagrange_interpolation(self, shares: List[Tuple[int, int]]) -> int:
        """Reconstruct secret using Lagrange interpolation"""
        secret = 0
        for i, (x_i, y_i) in enumerate(shares):
            numerator = denominator = 1
            for j, (x_j, _) in enumerate(shares):
                if i != j:
                    numerator = (numerator * (-x_j)) % self.prime
                    denominator = (denominator * (x_i - x_j)) % self.prime
            
            secret = (secret + y_i * numerator * pow(denominator, -1, self.prime)) % self.prime
        
        return secret
    
    def reconstruct_secret(self, shares: List[Tuple[int, int]]) -> str:
        """Reconstruct the original secret from shares"""
        secret_int = self._lagrange_interpolation(shares)
        
        # Convert back to string
        secret_bytes = secret_int.to_bytes((secret_int.bit_length() + 7) // 8, 'big')
        return secret_bytes.decode()
