class Cat:
    """
    A toy class to represent felines.

    :param __fed: indicates whether the cat is fed or not.
    :type __fed: bool
    """
    __fed = False

    def purrs(self, s: str = "pur") -> str:
        """
        Emulate feline purr.

        :param s: the purr prefix for this specific cat.
        :type s: str
        :return: the onomatopoeia of cat's purr.
        """
        return f"{s}rrr"

    def meow(self) -> str:
        """
        Emulate feline meow.

        :return: the onomatopoeia of cat's meow.
        :rtype: str
        """
        return "Meow"

    def feed(self):
        """
        Feed the cat.
        """

        if self.__fed:
            raise "Cat already fed."
        else:
            self.__fed = True
            print(self.meow())

class Meownir(Cat):
    """
    Ruoyu's cat. Child class of class Cat.
    """

    def meow(self) -> str:
        """
        Emulate Meownir meow.

        :return: the onomatopoeia of Meownir's meow.
        :rtype: str
        """
        regular_cat_sound = super().meow()
        return "Wrr" + regular_cat_sound
