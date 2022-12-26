class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = lambda celsius: celsius + 273.15
        fahrenheit = lambda celsius: celsius * 1.80 + 32.00
        
        ans.append(kelvin(celsius))
        ans.append(fahrenheit(celsius))
        
        return ans
        
