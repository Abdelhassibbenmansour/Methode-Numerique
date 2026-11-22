
# Matrix Operations in Python

A menu-driven Python application developed for **TP N°01 – Initiation au langage Python**. This lab focuses on implementing fundamental matrix operations and matrix-property checks using Python functions, nested lists, loops, conditional statements, and a command-line menu.

## Project Structure

The lab is implemented in a single Python file:

```text
TP-01/
└── main.py
└── TP-01.pdf
```

The `main.py` file contains the matrix input/output functions, matrix-operation functions, property checks, and the main menu.

## Functions

### 1. Matrix Input

#### `lire_matrice()`

**How it works:**
1. Reads the number of rows (`n`) and columns (`m`).
2. Initializes an `n × m` matrix filled with zeros.
3. Uses nested loops to read each element.
4. Returns the completed matrix.

#### `lire_matrice_carree()`

**How it works:**
1. Reads the matrix order (`n`).
2. Creates an `n × n` matrix.
3. Reads each element using nested loops.
4. Returns the square matrix.

### 2. Matrix Display

#### `afficher_matrice(matrice, n, m)`

Displays a matrix with `n` rows and `m` columns. Each element is displayed with its row and column indexes.

#### `afficher_matrice_carree(matrice, n)`

Displays a square matrix of order `n`.

#### `afficher_matrice_identite(matrice, n)`

Transforms the supplied `n × n` matrix into an identity matrix, then displays it.

An identity matrix contains `1` on its main diagonal and `0` everywhere else.

**Important:** This function modifies the matrix passed to it.

### 3. Matrix Arithmetic

#### `calculer_somme_matrice(matrice1, matrice2, n)`

Calculates the sum of two square matrices of order `n`.

Each result element is calculated using:

\[
C[i][j] = A[i][j] + B[i][j]
\]

The function displays the resulting matrix. The main menu checks that both input matrices have the same order before calling it.

#### `calculer_produit_matrice(matrice1, matrice2)`

Calculates the product of two matrices when their dimensions are compatible.

If matrix `A` has dimensions `n × p` and matrix `B` has dimensions `p × m`, the resulting matrix `C` has dimensions `n × m`.



**Compatibility condition:** the number of columns in the first matrix must equal the number of rows in the second matrix.

If the dimensions are incompatible, the function displays an error message instead of calculating the product.

### 4. Matrix Transposition

#### `transposee_carree(matrice)`

Calculates the transpose of a square matrix **in place**.

The transpose is obtained by exchanging rows and columns:

\[
T[i][j] = A[j][i]
\]
### 5. Matrix Property Checks

The following functions return a Boolean value:

- `True` if the matrix satisfies the tested property.
- `False` otherwise.

#### `triangulaire_superieure(matrice)`

Checks whether a square matrix is upper triangular.

A matrix is upper triangular when every element **below the main diagonal** is zero

#### `triangulaire_inferieure(matrice)`

Checks whether a square matrix is lower triangular.

A matrix is lower triangular when every element **above the main diagonal** is zero
#### `diagonal(matrice)`

Checks whether a square matrix is diagonal.

A matrix is diagonal when all elements outside its main diagonal are zero
#### `symetrique(matrice)`

Checks whether a square matrix is symmetric.

A matrix is symmetric when it is equal to its transpose:

\[
A[i][j] = A[j][i]
\]

for every pair of indexes `i` and `j`.
## Usage

When the program starts, it displays a menu similar to the following:

```text
========== MENU ==========
1 - Lire une matrice carree
2 - Afficher une matrice carree
3 - Afficher la matrice identite
4 - Calculer la somme de deux matrices
5 - Calculer le produit de deux matrices
6 - Calculer la transposee d'une matrice
7 - Tester si une matrice est triangulaire superieure
8 - Tester si une matrice est triangulaire inferieure
9 - Tester si une matrice est diagonale
10 - Tester si une matrice est symetrique
0 - Quitter

Entrer votre choix :
```

For example, to calculate the sum of two 2 × 2 matrices, select option `4`, enter the values of the first matrix, then enter the values of the second matrix. The program displays their sum if their dimensions match.

---

**Lab:** TP N°01 – Initiation au language Python  
**Topic:** Matrix manipulation and fundamental operations  
**Language:** Python 
