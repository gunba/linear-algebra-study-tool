import random
import sys

import pyperclip

# Define the list of problems
problems = [
    {
        "name": "Affine transformations",
        "category": "Geometric Applications",
        "difficulty": 65,
    },
    {
        "name": "Applications of tensors in higher-dimensional linear algebra",
        "category": "Tensor Analysis",
        "difficulty": 80,
    },
    {
        "name": "Arnoldi iteration",
        "category": "Advanced Numerical Methods",
        "difficulty": 80,
    },
    {
        "name": "Basis and dimension",
        "category": "Vectors and Spaces",
        "difficulty": 35,
    },
    {"name": "Bilinear forms", "category": "Advanced Topics", "difficulty": 55},
    {
        "name": "Change of basis",
        "category": "Linear Transformations",
        "difficulty": 50,
    },
    {
        "name": "Characteristic polynomial",
        "category": "Eigenvalues and Eigenvectors",
        "difficulty": 45,
    },
    {
        "name": "Cholesky decomposition",
        "category": "Decompositions",
        "difficulty": 45,
    },
    {
        "name": "Clifford algebras",
        "category": "Nonlinear Algebraic Structures",
        "difficulty": 75,
    },
    {
        "name": "Computer graphics transformations",
        "category": "Geometric Applications",
        "difficulty": 75,
    },
    {
        "name": "Condition numbers",
        "category": "Perturbation Theory",
        "difficulty": 75,
    },
    {
        "name": "Consistency and the number of solutions",
        "category": "Systems of Linear Equations",
        "difficulty": 45,
    },
    {
        "name": "Controllability and observability matrices",
        "category": "Control Theory Applications",
        "difficulty": 75,
    },
    {
        "name": "Convex sets and convex functions",
        "category": "Optimization",
        "difficulty": 65,
    },
    {
        "name": "Correlation matrices",
        "category": "Probability and Statistics Applications",
        "difficulty": 55,
    },
    {
        "name": "Covariance matrices",
        "category": "Probability and Statistics Applications",
        "difficulty": 50,
    },
    {
        "name": "Definition and examples of linear transformations",
        "category": "Linear Transformations",
        "difficulty": 25,
    },
    {"name": "Determinants", "category": "Matrices", "difficulty": 35},
    {
        "name": "Diagonalization of matrices",
        "category": "Eigenvalues and Eigenvectors",
        "difficulty": 50,
    },
    {
        "name": "Distance metrics",
        "category": "Norms and Metrics",
        "difficulty": 35,
    },
    {
        "name": "Dot product and cross product",
        "category": "Vectors and Spaces",
        "difficulty": 20,
    },
    {
        "name": "Dual spaces",
        "category": "Advanced Inner Product Spaces",
        "difficulty": 55,
    },
    {
        "name": "Eigenspaces",
        "category": "Eigenvalues and Eigenvectors",
        "difficulty": 50,
    },
    {
        "name": "Eigenvalue decomposition (EVD)",
        "category": "Matrix Factorization Techniques",
        "difficulty": 60,
    },
    {
        "name": "Fast Fourier Transform (FFT) and its matrix form",
        "category": "Computational Techniques",
        "difficulty": 70,
    },
    {
        "name": "Finding eigenvalues and eigenvectors",
        "category": "Eigenvalues and Eigenvectors",
        "difficulty": 40,
    },
    {
        "name": "Functions of matrices (e.g., polynomials, exponentials)",
        "category": "Matrix Functions",
        "difficulty": 70,
    },
    {
        "name": "Generalized eigenvalue problems",
        "category": "Advanced Eigenvalue Problems",
        "difficulty": 75,
    },
    {
        "name": "Gram-Schmidt process",
        "category": "Inner Product Spaces",
        "difficulty": 45,
    },
    {
        "name": "Graph theory and adjacency matrices",
        "category": "Applications",
        "difficulty": 55,
    },
    {
        "name": "Grassmann algebras",
        "category": "Nonlinear Algebraic Structures",
        "difficulty": 80,
    },
    {
        "name": "Hadamard product",
        "category": "Matrix Functions and Operations",
        "difficulty": 50,
    },
    {
        "name": "Hermitian and skew-Hermitian matrices",
        "category": "Special Matrices and Properties",
        "difficulty": 60,
    },
    {
        "name": "Hilbert spaces",
        "category": "Advanced Inner Product Spaces",
        "difficulty": 70,
    },
    {
        "name": "Homogeneous systems and particular solutions",
        "category": "Systems of Linear Equations",
        "difficulty": 40,
    },
    {
        "name": "Induced norms",
        "category": "Norms and Metrics",
        "difficulty": 45,
    },
    {
        "name": "Inner product (dot product in Euclidean space)",
        "category": "Inner Product Spaces",
        "difficulty": 20,
    },
    {
        "name": "Integer programming",
        "category": "Further Optimization Techniques",
        "difficulty": 80,
    },
    {"name": "Inverse of a matrix", "category": "Matrices", "difficulty": 40},
    {
        "name": "Isomorphisms and automorphisms",
        "category": "Advanced Linear Transformations",
        "difficulty": 60,
    },
    {
        "name": "Iterative methods for solving linear systems (e.g., Jacobi, Gauss-Seidel, Conjugate Gradient)",
        "category": "Numerical Linear Algebra",
        "difficulty": 70,
    },
    {
        "name": "Jordan canonical form",
        "category": "Advanced Topics",
        "difficulty": 70,
    },
    {
        "name": "Kalman filters",
        "category": "Control Theory Applications",
        "difficulty": 80,
    },
    {
        "name": "Kernel and image of a linear transformation",
        "category": "Linear Transformations",
        "difficulty": 35,
    },
    {
        "name": "Kronecker product",
        "category": "Matrix Functions and Operations",
        "difficulty": 55,
    },
    {
        "name": "LU decomposition",
        "category": "Decompositions",
        "difficulty": 40,
    },
    {
        "name": "Lanczos algorithm",
        "category": "Advanced Numerical Methods",
        "difficulty": 80,
    },
    {
        "name": "Laplacian matrices",
        "category": "Graph Theory Applications",
        "difficulty": 60,
    },
    {
        "name": "Least squares problems",
        "category": "Applications",
        "difficulty": 50,
    },
    {
        "name": "Linear combinations and span",
        "category": "Vectors and Spaces",
        "difficulty": 30,
    },
    {
        "name": "Linear programming",
        "category": "Optimization",
        "difficulty": 60,
    },
    {"name": "Linear regression", "category": "Applications", "difficulty": 55},
    {"name": "Markov chains", "category": "Applications", "difficulty": 60},
    {
        "name": "Markov processes",
        "category": "Stochastic Matrices and Applications",
        "difficulty": 65,
    },
    {
        "name": "Matrix addition, subtraction, and scalar multiplication",
        "category": "Matrices",
        "difficulty": 15,
    },
    {
        "name": "Matrix exponentiation",
        "category": "Matrix Functions",
        "difficulty": 65,
    },
    {
        "name": "Matrix logarithms",
        "category": "Matrix Functions",
        "difficulty": 70,
    },
    {"name": "Matrix multiplication", "category": "Matrices", "difficulty": 25},
    {
        "name": "Matrix norms (Frobenius norm, infinity norm, etc.)",
        "category": "Norms and Metrics",
        "difficulty": 40,
    },
    {
        "name": "Matrix representation of linear transformations",
        "category": "Linear Transformations",
        "difficulty": 40,
    },
    {
        "name": "Non-negative matrix factorization (NMF)",
        "category": "Matrix Factorization Techniques",
        "difficulty": 65,
    },
    {
        "name": "Norms of vectors and matrices",
        "category": "Norms and Metrics",
        "difficulty": 30,
    },
    {
        "name": "Numerical methods for eigenvalue problems (e.g., power iteration, QR algorithm)",
        "category": "Advanced Eigenvalue Problems",
        "difficulty": 80,
    },
    {
        "name": "Numerical stability and error analysis",
        "category": "Numerical Linear Algebra",
        "difficulty": 75,
    },
    {
        "name": "Orthogonality and orthonormality",
        "category": "Inner Product Spaces",
        "difficulty": 35,
    },
    {
        "name": "PageRank algorithm",
        "category": "Stochastic Matrices and Applications",
        "difficulty": 70,
    },
    {
        "name": "Perron-Frobenius theorem",
        "category": "Advanced Topics",
        "difficulty": 70,
    },
    {
        "name": "Polar decomposition",
        "category": "Advanced Decomposition Techniques",
        "difficulty": 55,
    },
    {
        "name": "Positive definite and positive semi-definite matrices",
        "category": "Special Matrices and Properties",
        "difficulty": 60,
    },
    {
        "name": "Principal Component Analysis (PCA)",
        "category": "Applications",
        "difficulty": 65,
    },
    {
        "name": "Projection onto subspaces",
        "category": "Inner Product Spaces",
        "difficulty": 50,
    },
    {
        "name": "Projective geometry",
        "category": "Geometric Applications",
        "difficulty": 70,
    },
    {
        "name": "QR decomposition",
        "category": "Decompositions",
        "difficulty": 45,
    },
    {
        "name": "Quadratic forms",
        "category": "Advanced Topics",
        "difficulty": 60,
    },
    {
        "name": "Quadratic programming",
        "category": "Optimization",
        "difficulty": 70,
    },
    {
        "name": "Quantum gates and unitary matrices",
        "category": "Quantum Computing Applications",
        "difficulty": 80,
    },
    {
        "name": "Quantum state vectors",
        "category": "Quantum Computing Applications",
        "difficulty": 80,
    },
    {"name": "Rank of a matrix", "category": "Matrices", "difficulty": 35},
    {
        "name": "Row echelon form and reduced row echelon form",
        "category": "Systems of Linear Equations",
        "difficulty": 35,
    },
    {
        "name": "Schur decomposition",
        "category": "Advanced Decomposition Techniques",
        "difficulty": 60,
    },
    {
        "name": "Semidefinite programming",
        "category": "Further Optimization Techniques",
        "difficulty": 75,
    },
    {
        "name": "Sensitivity of solutions to small changes in data",
        "category": "Perturbation Theory",
        "difficulty": 70,
    },
    {
        "name": "Similar matrices",
        "category": "Eigenvalues and Eigenvectors",
        "difficulty": 55,
    },
    {
        "name": "Singular Value Decomposition (SVD)",
        "category": "Decompositions",
        "difficulty": 50,
    },
    {
        "name": "Singular transformations",
        "category": "Advanced Linear Transformations",
        "difficulty": 55,
    },
    {
        "name": "Solving systems using Gaussian elimination",
        "category": "Systems of Linear Equations",
        "difficulty": 30,
    },
    {
        "name": "Sparse matrices and their operations",
        "category": "Computational Techniques",
        "difficulty": 65,
    },
    {
        "name": "Special types of matrices (identity, diagonal, symmetric, orthogonal, etc.)",
        "category": "Matrices",
        "difficulty": 30,
    },
    {
        "name": "Spectral graph theory",
        "category": "Graph Theory Applications",
        "difficulty": 70,
    },
    {
        "name": "Spectral theorem",
        "category": "Advanced Topics",
        "difficulty": 75,
    },
    {
        "name": "Stability of algorithms",
        "category": "Perturbation Theory",
        "difficulty": 75,
    },
    {
        "name": "State-space representation",
        "category": "Control Theory Applications",
        "difficulty": 70,
    },
    {"name": "Subspaces", "category": "Vectors and Spaces", "difficulty": 40},
    {
        "name": "Tensors and tensor operations",
        "category": "Tensor Analysis",
        "difficulty": 75,
    },
    {
        "name": "Toeplitz and circulant matrices",
        "category": "Special Matrices and Properties",
        "difficulty": 55,
    },
    {
        "name": "Transition matrices",
        "category": "Stochastic Matrices and Applications",
        "difficulty": 60,
    },
    {"name": "Transpose of a matrix", "category": "Matrices", "difficulty": 20},
    {
        "name": "Vector addition and scalar multiplication",
        "category": "Vectors and Spaces",
        "difficulty": 10,
    },
    {
        "name": "Vector norms and distances",
        "category": "Vectors and Spaces",
        "difficulty": 25,
    },
]


def generate_prompt(difficulty):
    # Filter problems by the given difficulty level
    filtered_problems = [
        problem for problem in problems if problem["difficulty"] <= difficulty
    ]

    if not filtered_problems:
        return "No problems found with the specified difficulty level."

    # Select a random problem from the filtered list
    selected_problem = random.choice(filtered_problems)

    # Generate the prompt
    prompt = f"""
    You are an AI tutor that behaves like a terminal. The user has requested problems up to a difficulty level of {difficulty}/100. 

    Please generate a problem in the category "{selected_problem["category"]}" with a focus on "{selected_problem["name"]}". Scale the difficulty of the problem to match the user's requested difficulty level of {difficulty}.

    Follow these steps:
    1. Generate a problem related to "{selected_problem["name"]}" scaled to a difficulty level of {difficulty}.
    2. Provide a basic outline of the steps to solve the problem without giving the answer.
    3. Wait for the user's answer.
    4. Check if the user's answer is correct and provide feedback.
    5. If the user types "help", provide the answer.

    Example interaction:
    You: Generate a problem.
    AI: Here's a problem: [Problem Statement]
    AI: To solve this problem, follow these steps: [Steps Outline]
    You: [Your Answer]
    AI: [Feedback if correct or incorrect]
    You: help
    AI: [Answer]

    Please generate a problem in the category "{selected_problem["category"]}" with a difficulty level of {difficulty} focusing on "{selected_problem["name"]}".
    """

    # Copy the prompt to clipboard
    pyperclip.copy(prompt)
    return "Prompt copied to clipboard."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_prompt.py <difficulty_level>")
        sys.exit(1)

    try:
        difficulty_level = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for difficulty level.")
        sys.exit(1)

    result = generate_prompt(difficulty_level)
    print(result)
