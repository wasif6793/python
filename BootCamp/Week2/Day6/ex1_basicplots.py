import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y,label ="Asie hi exercise", color="magenta", marker = "o")
plt.xlabel("x-axiswa")
plt.ylabel("y-axiswa")
plt.legend()
plt.show()

#Bar chart

cate = ["fruit","ration","veggies","coldrinks"]
amount = [12,15,10,40]
plt.bar(cate,amount,label = "Home saman", color = "Yellow")
plt.title("pta nhi")
plt.xlabel("Categoriya")
plt.ylabel("Paisa")
plt.legend()
plt.show()


# Scatter chart

plotsize = [1000,1200,1400,1600,1800,2000]
amountplot = [1.2,1.4,1.6,1.9,2.1,2.4]
plt.scatter(plotsize,amountplot, label ="PLot khareed lo", color = "green",marker="o")
plt.xlabel("Plot ka size")
plt.ylabel("Plot ka daam")
plt.title("Plot ki keemat")
plt.legend()
plt.show()