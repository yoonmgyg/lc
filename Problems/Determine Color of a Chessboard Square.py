class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in 'aceg':
            if coordinates[1] in '1357':
                return False
            else:
                return True
        else:
            if coordinates[1] in '1357':
                return True
            else:
                return False
