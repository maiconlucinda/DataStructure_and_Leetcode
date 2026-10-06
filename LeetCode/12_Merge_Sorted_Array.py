class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # Marcar quem o último elemento da fila - Vai mudando
        last = m + n - 1

        # While com duas condicoes, m (quantidade de itens da primeira lista) maior que zero e n (numeros de itens da segunda lista) maior que zero
        while m > 0 and n > 0:
            if nums1[m -1] > nums2[n -1]:
                nums1[last] = nums1[m -1]
                m -= 1
            else:
                nums1[last] = nums2[n -1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n -1]
            n, last = n - 1, last -1
            

        
        print(nums1)
            
    
solution = Solution()

solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

'''
O for é um while com uma regra embutida

O for não é a estrutura básica. Ele é um caso especial do while. Por baixo dos panos, o Python transforma isto:
for x in nums:
    print(x)


em algo assim:

it = iter(nums)
while True:
    try:
        x = next(it)    # avança 1 posição, sempre
    except StopIteration:
        break           # para quando a sequência acaba
    print(x)


Então o for toma três decisões por você:

Tem um cursor só.
Ele anda uma posição em toda volta, sem exceção.
Ele para quando a sequência acaba.
O while não decide nada disso. Você escolhe quantos cursores existem, quando cada um anda e quando o loop para.
'''


