from typing import Tuple

class PrettyNumber:
   
    def __init__(self, data: int):
        self._data = str(data)
        def digitsToScale(i):
            return (i - 1) // 3
        # a dictionary mapping the number of digits to the scale factor 
        self._scaleDict = {(i,'M') if digitsToScale(i) == 2 else (i,'B') if digitsToScale(i) == 33 else (i,'T') for i in range(7,16)}
        

    def _countDigits(self) -> int:
        dpIndex = self._data.find(".")
        if dpIndex == -1:
            return len(self._data)
        else:
            return dpIndex
    
    # _round returns a tuple of the digits to be printed before the decimal,
    # the digit to be printed after the decimal, and a bool indicating whether
    # the number overflowed to the next magnitude 
    def _round(self, leading: int, toRound: int ,roundOn: int) -> Tuple[str,str,bool]:
        if roundOn >= 5:
            rounded2 = (toRound + 1) % 10
            # if toRound overflowed then also increment the number to the left
            if rounded2 < toRound:
                rounded1 = (leading + 1) % 1000
                rounded1 = 1 if rounded1 == 0 else rounded1 
                return (str(rounded1),str(rounded2),True)
            return (str(leading),str(rounded2), False)
        return (str(leading), str(toRound), False)

    def _truncate(self) -> str:
        numDigits = self._countDigits()
        if numDigits in self._scaleDict:
            leadingDigits = 3 if numDigits % 3 == 0 else numDigits % 3
            first = int(self._data[0:leadingDigits])
            toRound = int(self._data[leadingDigits])
            roundOn = int(self._data[leadingDigits + 1])
            rounded = self._round(first,toRound,roundOn)
            # if the number of digits is no longer the same
            # then we must have overflowed so increment the total number
            # of digits
            if len(rounded[0]) != len(str(first)):
                numDigits += 1
            if numDigits in self._scaleDict:
                # since the number of digits overflowed it must be an integer so 
                # truncate the decimal approximation
                if rounded[1]:
                    return '{}{}'.format(rounded[0],self._scaleDict[numDigits])
                else:
                    return '{}.{}{}'.format(rounded[0],rounded[1],self._scaleDict[numDigits])
        return self._data
    
    def __repr__(self):
        return self._truncate()



