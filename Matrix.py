from random import randint as ri

class Matrix:
    def __init__(self, m, n):
        self.m=m
        self.n=n
        self.matr=self.matrix_gen(m, n)
        
    def matrix_gen(self, m, n):
        matrix=[]
        for i in range(m):
            matrix.append([])
            for _ in range(n):
                matrix[i].append(ri(-100, 100))
                
        return matrix
    
    def matrix_print(self):
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                print(f'{self.matr[i][j]:4}', end=' ')
            print()
            
    def matrix_transp(self):
        res=[]
        for j in range(len(self.matr[0])):
            res.append([])
            for i in range(len(self.matr)):
                res[j].append(self.matr[i][j])
        self.matr=res
        #return res
            
            

if __name__=='__main__':
    mat=Matrix(2, 3)
    print(mat.matrix_print())
    mat.matrix_transp()
    print(mat.matrix_print())
    mat.matrix_transp()
    print(mat.matrix_print())
    
    