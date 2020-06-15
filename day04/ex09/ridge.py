import numpy as np
import random as rd
from functools import wraps #garder les docstring des fonctions decorer

class Ridge():
    """
    Description:
    My personnal ridge regression class to fit like a boss.
    """
    def __init__(self, theta, alpha=0.001, max_iter=100000, lambda_=0.5):
        #if type(theta) != np.ndarray or type(alpha) != float or type(max_iter) != int \
        #        or type(lambda_) != float:
         #   print("Error init")
         #   exit(1)
        #elif np.shape(theta)[0] != 1 | np.shape(theta)[1] != 1:
        #    print("Theta isn't a vector")
        #    exit(1)
        self.alpha = alpha #learning rate
        self.max_iter = max_iter #nombre de training
        self.theta = theta #coeficient
        self.lambda_ = lambda_ #coef de regularisation

    def errno_(func):
        @wraps(func)
        def inner(*args):
            if len(args) >= 2  and type(args[1]) != np.ndarray:
                print("X are not numpy array")
                exit(1)
            elif len(args) >= 3 and type(args[2]) != np.ndarray:
                print("y isn't numpy array")
                exit(1)
            elif len(args) == 4 and type(args[3]) != float:
                print("Proportion isn't a float")
                exit(1)
            elif len(args) >= 3 and (np.shape(args[2])[0] != 1 \
                    | np.shape(args[2])[1] != 1):
                print("y not a vector")
                exit(1)
            return func(*args)
        return inner

    @errno_
    def zscore_(self, X):
        """
        La cote Z correspond au nombre d'écarts types séparant un résultat de la moyenne,
        utile pour le Gradient Descent (eviter nan)
        Args:
        X: has to be a numpy.ndarray, a matrix of dimesion m * n.
        Returns:
        A numpy.ndarray, a matrix of dimension m * n
        """
        mean = sum(X) / len(X) #moyenne
        std = std = (sum((X - mean) ** 2))/ len(X) #Standard deviation
        return (X - mean) / (std ** (1 / 2))

    @errno_
    def data_spliter_(self, X, y, proportion):
        """
        Creer des training set pour entrainer le model et des test set pour le tester
        Args:
        X: has to be a numpy.ndarray, a matrix of dimesion m * n.
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        proportion: has to be a float, taille du training set par rapport au set de base
        Returns:
        A tuple of list, all the sets
        """
        x_train, x_test, y_train, y_test = [], [], [], [] 
        index = [i for i in range(len(X))]
        rd.shuffle(index)
        total_size = len(X)
        prop = proportion * total_size
        for i in range(total_size):
            if i < prop:
                x_train.append(X[index[i]]), y_train.append(y[index[i]])
            else:
                x_test.append(X[index[i]]), y_test.append(y[index[i]])
        return (np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test))

    def add_polynomial_features_(self, x, power):
        """
        Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        power: has to be an int, the power up to which the columns of matrix x are 
        going to be raised.
        Returns:
        The matrix of polynomial features as a numpy.ndarray, of dimension m * (np), 
        containg the polynomial feature values for all training examples.
        None if x is an empty numpy.ndarray.
        """
        if type(x) != np.ndarray or type(power) != int:
            print("polynomial arguments invalid")
            exit(1)
        elif len(x) == 0:
            return None
        result = []
        for row in x:
            row_ = []
            i = 1
            while i <= power:
                for xi in row:
                    row_.append(xi ** i)
                i += 1
            result.append(row_)
        return np.array(result)

    @errno_
    def predict_(self, x):
        """
        Hypothese de X par theta, correspond au valeur predite sous forme de vecteur
        Args:
        X: has to be a numpy.ndarray, a matrix of dimesion m * n.
        Returns:
        A numpy.ndarray, a vector of size n * 1, hypothesis or y_hat
        """
        y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], self.theta)
        return y_hat

    @errno_
    def normal_equation_(self, X, y):
        """
        Trouve le theta le plus optimiser sans en avoir un de base, pas besoin de
        normaliser les X et prends trop de temps sur des sets trop large
        Args:
        X: has to be a numpy.ndarray, a matrix of dimesion m * n.
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        A numpy.ndarray, a vector of n * 1, theta
        """
        X = np.c_[np.ones((len(x), 1)), x]
        result_inv = np.linalg.inv(np.dot(np.transpose(X), X)) #linealg = inverse
        result = np.dot(np.dot(result_inv, np.transpose(X)), y)
        result = np.squeeze(result) #transforme en vecteur ligne
        self.theta = result
        return result

    @errno_
    def fit_(self, x, y):
        """
        Trouve le meilleur theta a partir d'un theta de base et faisant une descente
        de gradient (deriver de la fonction de perte) sur max_iter (n_cycle) avec un
        learning rate
        Args:
        x: has to be a numpy.ndarray, a matrix of dimesion m * n.
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        A numpy.ndarray, a vector of dimension n * 1 (new theta)
        """
        m = len(x)
        X = np.c_[np.ones((len(x), 1)), x]
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        i = 0
        while i < self.max_iter:
            theta_prime = np.copy(self.theta)
            theta_prime[0] = 0
            gradient = (1 / m) * (np.dot(np.transpose(X), \
                    (np.dot(X, self.theta) - y)) + (self.lambda_ * theta_prime))
            self.theta = self.theta - self.alpha * gradient
            i += 1
        return self.theta

    @errno_
    def cost_(self, x, y):
        """
        Fonction de perte, equivqlent a l'erreur quadratique moyenne, permet de
        connaitre de calculer l'efficacité du model
        Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        x: has to be a numpy.ndarray, a matrix of dimesion m * n.
        Returns:
        A float, valeur d'efficacité
        """
        m = len(x)
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        theta_p2 = self.theta * self.theta
        theta_p2[0] = 0
        return (sum((y_hat - y) ** 2) + (self.lambda_ * sum(theta_p2))) / (2 * m)

