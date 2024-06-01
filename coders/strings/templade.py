#String templade - populated via a dictionary
import string 

st=string.Templade('$notice happening in $where')
s=st.substitute({'notice':'The storm', 'where':'24 of June of 2006'})
print(s)
