import random

class Tank(object):
   __name='坦克' 
   __attack=1
   __defence=1
   __hp=100
   @property
   def n(self):
        #print('%s' % self.__name)
        return self.__name
    
   @n.setter
   def n(self,value):
       self.__name=value
   
   @property
   def a(self):
        #print('%s 攻击力：%d' %(self.__name,self.__attack))
        return self.__attack
    
   @a.setter
   def a(self,value):
       self.__attack=value

   @property
   def d(self):
       #print('%s 防御力：%d' %(self.__name,self.__defence))
       return self.__defence

   @d.setter
   def d(self,value):
       self.__defence=value

   @property
   def h(self):
       #print('%s 血量：%d' %(self.__name,self.__hp))
       return self.__hp
    
   @h.setter
   def h(self,value):
       self.__hp=value


class Atank(Tank):
   _Tank__name='A型坦克' 
   #_Tank__attack=50
   #_Tank__defence=30
   _Tank__hp=150

class Btank(Tank):
   _Tank__name='B型坦克' 
   #_Tank__attack=80
   #_Tank__defence=50
   _Tank__hp=120

def ap(tank1,tank2):
    print('[%s] 攻击 [%s]' %(tank1.n,tank2.n))
    h = tank2.h
    a = random.randint(1,10)
    result = h - a
    if result > 0:
        tank2.h = result
        print('%s 剩余血量：%d' %(tank2.n,result))
    else:
        tank2.h = result
        print('[%s]已被击毁' % tank2.n)


