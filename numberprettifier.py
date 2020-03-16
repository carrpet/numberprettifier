from enum import IntEnum

class PrettyNumber:
   
    def __init__(self,data):
        self._data = str(data)
        self._scaleDict = {k:v for (k,v) in [(2,'M'),(3,'B'),(4,'T')]}

    def _countDigits(self) -> int:
        dpIndex = self._data.find(".")
        if dpIndex == -1:
            return len(self._data)
        else:
            return dpIndex
    
    def _round(self,leading,toRound,roundOn):
        if roundOn >= 5:
            rounded2 = (toRound + 1) % 10
            if rounded2 < toRound:
                rounded1 = (leading + 1) % 1000
                rounded1 = 1 if rounded1 == 0 else rounded1 
                return (str(rounded1),str(rounded2))
            return (str(leading),str(rounded2))
        return (str(leading), str(toRound))

    def _truncate(self):
        numDigits = self._countDigits()
        scaleDigitHash = (numDigits -1) // 3
        if scaleDigitHash in self._scaleDict:
            leadingDigits = 3 if numDigits % 3 == 0 else numDigits % 3
            first = int(self._data[0:leadingDigits])
            toRound = int(self._data[leadingDigits])
            roundOn = int(self._data[leadingDigits + 1])
            rounded = self._round(first,toRound,roundOn)
            if len(rounded[0]) != len(str(first)):
                numDigits += 1
                scaleDigitHash = numDigits // 3
            if scaleDigitHash in self._scaleDict:
                if rounded[1] == '0':
                    return '{}{}'.format(rounded[0],self._scaleDict[scaleDigitHash])
                else:
                    return '{}.{}{}'.format(rounded[0],rounded[1],self._scaleDict[scaleDigitHash])
        return self._data
    
    def __repr__(self):
        return self._truncate()



