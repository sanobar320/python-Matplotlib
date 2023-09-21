

from matplotlib import pyplot as plt
x =[0.25,1.25,2.25,3.25,4.25]
y =[50,40,70,80,20]
plt.bar(x,y,
label="BMW",width=.2 , color ='g')
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()







from matplotlib import style
 
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()







x=[1,2,3,4,5]
y =[10, 12 ,8,15 ,7]
a =[9,8,8,7,6]
b = [20 ,21,32,43,54]
plt.plot(a,b , color ="g" )
plt.plot(x,y , marker ='o' , color ='r' , label = 'Sales Data' , linestyle = "dotted")
plt.title("line plot ")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc='upper left')
plt.show()



plt.xlabel("months")
plt.ylabel("years")
plt.title("Yearly data")
# this line of code working same as below line 
plt.plot(x, y, color='red' ,marker='D' , linestyle="")
plt.plot(x, y , 'Dr')
plt.plot(x,y , color="red" , linewidth=6 , linestyle="dotted")
plt.show()
