class FSM:
    def __init__(self):
        self.state = 'START'  
    
    def transition(self, char):
        """Transition the state based on input character."""
        if self.state == 'START':
            if char == 'a':
                self.state = 'STATE_A'
            elif char == 'b':
                self.state = 'STATE_B'
            else:
                self.state = 'INVALID'
        
        elif self.state == 'STATE_A':
            if char == 'b':
                self.state = 'STATE_B'
            else:
                self.state = 'INVALID'
        
        elif self.state == 'STATE_B':
            if char == 'a':
                self.state = 'STATE_A'
            else:
                self.state = 'INVALID'
        
        elif self.state == 'INVALID':
            pass  
    
    def is_valid(self, input_string):
        """Process input string and check if it’s valid."""
        for char in input_string:
            self.transition(char)
            if self.state == 'INVALID':
                return False
        return self.state in {'STATE_A', 'STATE_B'}  
fsm = FSM()


