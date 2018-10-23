# 绘制极坐标图
import matplotlib.pyplot as plt
import numpy as np

theta=np.arange(0,2*np.pi,0.02)
ax1 = plt.subplot(131, projection='polar')
ax2 = plt.subplot(132)
ax1.plot(theta,theta/6,'--',lw=2)
# 设置反向
# ax1.set_theta_direction(-1)
# 设置网格
ax1.set_thetagrids(np.arange(0.0, 360.0, 30.0))
# 设置标签路径
# ax1.set_rlabel_position('90')
ax2.plot(theta,theta/6,'--',lw=2)
ax2.grid(linestyle=':')
# plt.show()

N=20
theta=np.linspace(0,2*np.pi,N,endpoint=False)#均分角度
print(theta)
radii=10*np.random.rand(N)#随机角度
width=np.pi/4*np.random.rand(N)#随机宽度
 
ax=plt.subplot(133,projection='polar')#极坐标图绘制
bars=ax.bar(theta,radii,width=width,bottom=0.0)#哪个角度画，长度，扇形角度,从距离圆心0的地方开始画
 
for r,bar in zip(radii,bars):
    #添加颜色
    bar.set_facecolor(plt.cm.viridis(r/10.0))
    bar.set_alpha(0.5)    
     
 
plt.title('polar')
plt.show()