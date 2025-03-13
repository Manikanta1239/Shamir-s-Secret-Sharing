# Shamir's Secret Sharing

## Introduction
Shamir's Secret Sharing (SSS) is a cryptographic algorithm that allows a secret to be split into multiple shares. A specified number of these shares (threshold) are required to reconstruct the secret, ensuring security and fault tolerance. This project implements Shamir's Secret Sharing scheme.

## Features
- Securely split a secret into multiple shares using polynomial interpolation
- Reconstruct the secret using Lagrange interpolation with a threshold number of shares
- Supports prime field arithmetic with configurable prime modulus
- Implementation in Python with NumPy optimization

## Installation
### Prerequisites
- Python 3.8 or higher
- NumPy >= 1.19.0
- SymPy >= 1.8.0 (for prime number operations)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Shamir-s-Secret-Sharing.git
   cd Shamir-s-Secret-Sharing
   ```
2. Install dependencies:
   ```sh
   pip install numpy sympy
   ```

## Usage
### Splitting a Secret
```sh
python shamir.py split --secret "your_secret" --shares 5 --threshold 3
```
This command generates 5 shares and requires at least 3 shares to reconstruct the secret.

### Reconstructing a Secret
```sh
python shamir.py reconstruct --shares share1 share2 share3
```
Use at least the threshold number of shares to recover the original secret.

## Example
```python
from shamir import ShamirSecretSharing
sss = ShamirSecretSharing()
shares = sss.split_secret("my_secret", 5, 3)
secret = sss.reconstruct_secret(shares[:3])
print("Recovered Secret:", secret)
```

## Security Considerations
- Ensure the field size is large enough to prevent brute-force attacks.
- Keep the threshold high enough to balance security and fault tolerance.
- Store shares securely to prevent unauthorized access.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

