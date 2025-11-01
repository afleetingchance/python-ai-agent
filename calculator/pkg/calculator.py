class Calculator:
    def evaluate(self, expression):
        parts = expression.split()
        
        # Perform multiplication first
        i = 1
        while i < len(parts) - 1:
            if parts[i] == '*':
                num1 = float(parts[i-1])
                num2 = float(parts[i+1])
                result = num1 * num2
                parts = parts[:i-1] + [str(result)] + parts[i+2:]
                i = 1 # Reset index after multiplication
            else:
                i += 2
        
        # Perform addition
        i = 1
        while i < len(parts) - 1:
            if parts[i] == '+':
                num1 = float(parts[i-1])
                num2 = float(parts[i+1])
                result = num1 + num2
                parts = parts[:i-1] + [str(result)] + parts[i+2:]
                i = 1 # Reset index after addition
            else:
                i += 2
        
        if len(parts) == 1:
            return float(parts[0])
        else:
            return "Invalid expression"
