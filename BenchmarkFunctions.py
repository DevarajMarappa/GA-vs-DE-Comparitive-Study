import numpy as np

def evaluate_functions(id,x):
    match id: #each case statement has logic for benchmark functions, refer return stmt for funcation name
        case 1: 
            if x is None:
                return None, "Elliptic func"
            else:
                dim = len(x)
                return np.sum(10**6 ** ((i - 1) / (dim - 1)) * x[i-1]**2 for i in range(1, dim+1)) , "Elliptic func"
        case 2:
            if x is None:
                return None,"Bent Cigar function"
            else:
                dim = len(x)
                return x[0]**2 + 10**6 * np.sum(x[i]**2 for i in range(1, dim)),"Bent Cigar function"
        case 3: 
            if x is None:
                return None,"Discus function"
            else:
                dim = len(x)
                return 10**6 * x[0]**2 + np.sum(x[i]**2 for i in range(1, dim)),"Discus function"
        case 4:
            if x is None:
                return None,"Rosenbrock's function"
            else:
                dim = len(x)
                return np.sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(dim-1)),"Rosenbrock's function"
        case 5:
            if x is None:
                return None,"Ackley's function" 
            else:
                dim = len(x)
                term1 = -0.2 * np.sqrt((1/dim) * np.sum(np.power(x,2)))
                term2 = (1/dim) * np.sum(np.cos(np.multiply(2 * np.pi , x)))
                return -20 * np.exp(term1) - np.exp(term2) + 20 + np.exp(1),"Ackley's function"     
        case 6:
            if x is None:
                return None,"Griewank's function"
            else:
                dim = len(x)
                term1 = np.sum(np.power(x,2)) / 4000
                term2 = np.prod(np.cos(x / np.sqrt(np.arange(1, dim + 1))))
                return 1 + term1 - term2,"Griewank's function"
        case 7:
            if x is None:
                return None,"Rastrigin's function"
            else:
                dim = len(x)
                return 10 * dim + np.sum( np.power(x,2) - 10 * np.cos(2 * np.multiply(np.pi , x))),"Rastrigin's function"
        case 8:
            if x is None:
                return None,"Weierstrass function"
            else:
                dim = len(x)
                result = 0
                a=0.5
                b=3
                k_max=20
                for i in range(dim):
                    term1 = 0
                    term2 = 0
                    for k in range(k_max + 1):
                        term1 += np.power(a,k) * np.cos(2 * np.pi * np.power(b,k) * (x[i] + 0.5))
                        term2 += np.power(a,k) * np.cos(2 * np.pi * np.power(b,k) * 0.5)
                    result += term1 - dim * term2
                return result,"Weierstrass function"

