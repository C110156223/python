all=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
engpass=set(['John','Mary','Fiona','Claire','Ben','Bill'])
mathpass=set(['Mary','Fiona','Claire','Eva','Ben'])

print("英文數學都及格",engpass&mathpass)
print("數學不及格",all-mathpass) 
print("英文及格且數學不及格",engpass-mathpass) 