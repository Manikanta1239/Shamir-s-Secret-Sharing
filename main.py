import json
from sympy import symbols,expand
from itertools import combinations
import argparse
from shamir import ShamirSecretSharing

def lagrange_interpolation(points):
    x = symbols('x')
    polynomial = 0
    for i in range(len(points)):
        xi, yi = points[i]
        term = yi
        for j in range(len(points)):
            if i != j:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        polynomial += term
    return expand(polynomial)

with open('input.json') as file:
    data = json.load(file)

n = data['keys']['n']
k = data['keys']['k']

points = []
for key, value in data.items():
    if key.isdigit():
        base = int(value['base'])
        decimal_value = int(value['value'], base)
        points.append((int(key), decimal_value))

print("Points:",points)

combinations_of_points = combinations(points, k)

polynomials = []

for combo in combinations_of_points:
    polynomial = lagrange_interpolation(combo)
    polynomials.append(polynomial)
    print(f'Polynomial for {combo}: {polynomial.simplify()}')

print("Generated polynomials:",polynomials)

x_test, y_test = 1, 4
x = symbols('x')
for poly in polynomials:
    if poly.subs(x, x_test) == y_test:
        print("Found the correct polynomial:", poly)
        break
    else:
        print("Polynomial does not match the given point")

def main():
    parser = argparse.ArgumentParser(description="Shamir's Secret Sharing Implementation")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Split command
    split_parser = subparsers.add_parser('split', help='Split a secret into shares')
    split_parser.add_argument('--secret', required=True, help='Secret to split')
    split_parser.add_argument('--shares', type=int, required=True, help='Number of shares')
    split_parser.add_argument('--threshold', type=int, required=True, help='Threshold for reconstruction')
    
    # Reconstruct command
    reconstruct_parser = subparsers.add_parser('reconstruct', help='Reconstruct secret from shares')
    reconstruct_parser.add_argument('--shares', nargs='+', help='Shares in format "x,y"')
    
    args = parser.parse_args()
    sss = ShamirSecretSharing()
    
    if args.command == 'split':
        try:
            shares = sss.split_secret(args.secret, args.shares, args.threshold)
            print("Generated shares:")
            for x, y in shares:
                print(f"{x},{y}")
        except Exception as e:
            print(f"Error: {e}")
            
    elif args.command == 'reconstruct':
        try:
            # Parse shares from string format
            shares = []
            for share in args.shares:
                x, y = map(int, share.split(','))
                shares.append((x, y))
            
            secret = sss.reconstruct_secret(shares)
            print(f"Reconstructed secret: {secret}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
