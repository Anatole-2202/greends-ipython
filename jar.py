class Jar:
    def __init__(self, capacity=12, number_of_cookies=0):
        self._capacity=capacity
        self._number_of_cookies=number_of_cookies
        if capacity < 0 :
            raise(ValueError)

    @property
    def capacity(self):
        return(self._capacity)

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if  (self._number_of_cookies + n) > self._capacity:
            raise(ValueError)
        else :
            self._number_of_cookies += n

    @property
    def size(self):
        return(self._number_of_cookies)

    def withdraw(self, n):
        if n < 0 or int(n)==False:
            raise (ValueError)
        else:
            if (self._number_of_cookies -n) < 0 :
                raise(ValueError)
            else :
                self._number_of_cookies -= n


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise (ValueError)
        self._capacity=capacity
