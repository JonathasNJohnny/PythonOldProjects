import random
class BST:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)
        else: 
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)

    def selfPrint(self):
        lines, *_ = self.selfPrintCoWorker()
        for line in lines:
            print(line)

    def selfPrintCoWorker(self):
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left.selfPrintCoWorker()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '=' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right.selfPrintCoWorker()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '=' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left.selfPrintCoWorker()
        right, m, q, y = self.right.selfPrintCoWorker()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '=' + s + y * '=' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def getLeafCount(self, node):
        if node is None:
            return 0 
        if(node.left is None and node.right is None):
            return 1 
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)
    
op = 0
quantity = 0
myBST = BST(50)
while(op < 1 or op > 2):
    op = int(input("\nDigite\n1 - Para Manualmente\n2 - Para Automáticamente\n\nComo deseja gerar os valores da BST?: "))
    print("Quantos valores quer", "gerar" if (op == 2) else "digitar", "?: ", end="")
    quantity = int(input())
if (op == 2):
    for i in range(quantity):
        myBST.insert(random.randint(0, 100))
else:
    for i in range(quantity):
        print("Digite o ", i+1, "º valor: ", sep="", end="")
        myBST.insert(int(input()))
print()
myBST.selfPrint()
myBSTCounter = myBST.getLeafCount(myBST)
print("\nQuantidade de nós folhas:", myBSTCounter)
