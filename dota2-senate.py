def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        queueR = deque()
        queueD = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                queueR.append(i)
            else:
                queueD.append(i)
        
        while queueR and queueD:
            r = queueR.popleft()
            d = queueD.popleft()
            if r < d:
                # Radiant acts first
                queueR.append(r + n)
            else:
                # Dire acts first
                queueD.append(d + n)
        
        return "Radiant" if queueR else "Dire"
