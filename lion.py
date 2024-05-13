import matplotlib.pyplot as plt
student=["s1","s2","s3","s4"]
markes=[90,25,35,60]
plt.title("student markes result")
plt.xlabel("student")
plt.ylabel("markes")
plt.bar(student,markes,width=0.9,color=["red","orange","blue","black"])
plt.show()
