from Game import Game
import math

class SubtractSquares(Game):
    """A class of subtract square game state objects.
    
    Inherits from the generic Game class.
    
    ****INSTRUCTIONS HERE****
    
    """
    
    def __init__(self, max_choice, players):
        """ (SubtractSquares, int, list) -> None
        
        Initialize a subtract squares game state.
        """
        
        Game.__init__(self, players)
        self.state = max_choice

        options = []
        for i in range(1, math.ceil(math.sqrt(self.state))):
            options.append(i**2)
        self.options = options
        #produce the list of options
        
    def __eq__(self, other):
        """ (SubtractSquares, SubtractSquares) -> Bool
        
        Determine whether two game states are equal.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Abe'])
        >>> b = SubtractSquares(65, ['Kasra', 'Abe'])
        >>> a == b
        False
        >>> b = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a == b
        True
        """
        
        return self.state == other.state
    
    def __str__(self):
        """ (SubtractSquares) -> str
        
        Return a string representation of the game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> print(str(a))
        78: Kasra
        """
        
        return '{}: {}'.format(self.state, self.players[0])


if __name__ == '__main__':
    import doctest
    doctest.testmod()