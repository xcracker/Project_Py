import os
import sys
import nester
man=[]
other=[]
try:
    data=open('sketch.txt')
    print(data.readline(),end='')
    print(data.readline(),end='')
    data.seek(0)
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("This data file is missing")

try:
    m_file=open("man_data.txt","w")
    o_file=open("other_data.txt","w")
    print(man,file=m_file)
    print(other,file=o_file)
    m_file.close()
    o_file.close()
except IOError:
    print("This data file is missing")
finally:
    m_file.close()
    o_file.close()