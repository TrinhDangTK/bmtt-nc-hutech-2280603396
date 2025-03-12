class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, P_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail = 0
        direction = 1
        for char in P_text:
            rails[rail].append(char)
            if rail == 0:
                direction = 1
            elif rail == num_rails - 1:
                direction = -1
            reil_index += direction
        C_text = ''.join(''.join(rail) for rail in rails)
        return C_text
    
    def rail_fence_decrypt(self, C_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail = 0
        direction = 1
        
       for _ in range(len(C_text)):
           rail_lengths[rail_index] += 1
           if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(C_text[start:start+length])
            start += length
        P_text = ""
        rail = 0
        direction = 1
        
        for _ in range(len(C_text)):
            P_text += rails[rail][0]
            rails[rail] = rails[rail][1:]
            if rail == 0:
                direction = 1
            elif rail == num_rails - 1:
                direction = -1
            rail += direction
        return P_text
           