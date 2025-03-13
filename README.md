# Shamir's Secret Sharing

## Introduction
Shamir's Secret Sharing (SSS) is a cryptographic algorithm that enables secure distribution of sensitive information across multiple parties. Developed by Adi Shamir in 1979, this scheme allows you to split a secret (like a password, private key, or confidential document) into distinct shares, where a predefined number of shares are required to reconstruct the original secret.

### Real-World Applications
- **Cryptocurrency Wallet Security**: Protecting private keys
- **Banking Systems**: Securing access to vault combinations
- **Corporate Access Control**: Managing privileged access credentials
- **Data Recovery Systems**: Implementing secure backup mechanisms

## Features
- **Flexible Share Generation**
  - Create any number of shares from a secret
  - Configure custom threshold requirements
  - Support for both text and binary secrets
  
- **Strong Security Guarantees**
  - Information-theoretic security
  - No computational assumptions required
  - Impossible to recover secret with fewer than threshold shares
  
- **Advanced Implementation**
  - Optimized polynomial interpolation
  - Efficient prime field arithmetic
  - Built-in input validation and error handling

## How It Works
1. **Secret Splitting Process**
   - Convert secret to numerical form
   - Generate random polynomial coefficients
   - Evaluate polynomial at different points to create shares

2. **Reconstruction Process**
   - Collect threshold number of shares
   - Use Lagrange interpolation to recover polynomial
   - Extract original secret from polynomial

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

3. Verify installation:
   ```sh
   python -c "import shamir; print(shamir.__version__)"
   ```

## Detailed Usage Guide
### Creating Shares
```python
from shamir import ShamirSecretSharing

# Initialize with custom prime modulus (optional)
sss = ShamirSecretSharing(prime_modulus=2**127 - 1)

# Split secret into shares
secret = "MySecretPassword123"
total_shares = 5      # Total number of shares to generate
threshold = 3         # Minimum shares needed to reconstruct

shares = sss.split_secret(secret, total_shares, threshold)
print("Generated Shares:")
for i, share in enumerate(shares, 1):
    print(f"Share {i}: {share}")
```

### Reconstructing Secret
```python
# Reconstruct using any threshold number of shares
received_shares = shares[:threshold]  # Using first 3 shares
recovered_secret = sss.reconstruct_secret(received_shares)
print(f"Original Secret: {secret}")
print(f"Recovered Secret: {recovered_secret}")
```

## Security Best Practices
1. **Share Distribution**
   - Distribute shares through different channels
   - Never store all shares in one location
   - Use secure transmission methods

2. **Threshold Selection**
   - Choose threshold > n/2 (where n is total shares)
   - Consider business requirements and risk level
   - Balance security with operational needs

3. **Share Storage**
   - Encrypt individual shares when stored
   - Implement access controls for share holders
   - Regular audit of share possession

## Troubleshooting
Common issues and solutions:

1. **Invalid Share Format**
   - Ensure shares are in correct format
   - Verify share data hasn't been corrupted
   - Check for proper encoding/decoding

2. **Reconstruction Failures**
   - Verify threshold number of shares
   - Ensure shares are from same secret
   - Check for share corruption

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Submit pull request

### Code Style
- Follow PEP 8 guidelines
- Include docstrings for new functions
- Add unit tests for new features

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Adi Shamir for the original algorithm
- Contributors to the project
- Open source cryptography community

