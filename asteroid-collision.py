def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[]
        for i in asteroids:
            if i>0:
                st.append(i)
            else :
                pos=abs(i)
                while st and st[-1]>0 and st[-1]<pos:
                    st.pop()
                if st and st[-1]==pos:
                    st.pop()
                elif not st or st[-1]<0:
                    st.append(i) 
        return st
