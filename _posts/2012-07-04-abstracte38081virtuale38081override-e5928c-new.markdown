---
author: ths
comments: true
date: 2012-07-04 08:58:00+00:00
layout: post
slug: abstract%e3%80%81virtual%e3%80%81override-%e5%92%8c-new
title: abstract、virtual、override 和 new
wordpress_id: 823
categories:
- 技术
tags:
- abstract
- new
- override
- virtual
---

abstract、virtual、override 和 new 是在类的继承关系中常用的四个修饰方法的关键字，在此略作总结。 





1. 常用的中文名：abstract 抽象方法，virtual 虚方法，override 覆盖基类方法，new 隐藏基类方法，override 和 new 有时都叫重写基类方法。 





2. 适用场合：abstract 和 virtual 用在基类（父类）中；override 和 new 用在派生类（子类）中。 





3. 具体概念： 





abstract 抽象方法，是空方法，没有方法体，派生类必须以 override 实现此方法。 





virtual 虚方法，若希望或预料到基类的这个方法在将来的派生类中会被重写（override 或 new），则此方法必须被声明为 virtual。 





override 重写继承自基类的 virtural 方法，可以理解为拆掉老房子，在原址上建新房子，老房子再也找不到了（基类方法永远调用不到了）。 





new 隐藏继承自基类的 virtual 方法，老房子还留着，在旁边盖个新房，想住新房住新房（作为派生类对象调用），想住老房住老房（作为基类对象调用）。 





当派生类中出现与基类同名的方法，而此方法前面未加 override 或 new 修饰符时，编译器会报警告，但不报错，真正执行时等同于加了 new。 





4. abstract 和 virtual 的区别：abstract 方法还没实现，连累着基类也不能被实例化，除了作为一种规则或符号外没啥用；virtual 则比较好，派生类想重写就重写，不想重写就吃老子的。而且继承再好也是少用为妙，继承层次越少越好，派生类新扩展的功能越少越好，virtual 深合此意。 





5. override 和 new 的区别：当派生类对象作为基类类型使用时，override 的执行派生类方法，new 的执行基类方法。如果作为派生类类型调用，则都是执行 override 或 new 之后的。 





演示 override 和 new 区别的例子：




    
    <span class="rem">// Define the base class</span>
    <span class="kwrd">class</span> Car
    {
    <span class="kwrd">public</span> <span class="kwrd">virtual</span> <span class="kwrd">void</span> DescribeCar()
       {
           System.Console.WriteLine(<span class="str">"Four wheels and an engine."</span>);
       }
    }
    <span class="rem">// Define the derived classes</span>
    <span class="kwrd">class</span> ConvertibleCar : Car
    {
    <span class="kwrd">public</span> <span class="kwrd">new</span> <span class="kwrd">virtual</span> <span class="kwrd">void</span> DescribeCar()
       {
    <span class="kwrd">base</span>.DescribeCar();
           System.Console.WriteLine(<span class="str">"A roof that opens up."</span>);
       }
    }
    <span class="kwrd">class</span> Minivan : Car
    {
    <span class="kwrd">public</span> <span class="kwrd">override</span> <span class="kwrd">void</span> DescribeCar()
       {
    <span class="kwrd">base</span>.DescribeCar();
           System.Console.WriteLine(<span class="str">"Carries seven people."</span>);
       }
    }
    <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> TestCars1()
    {
       Car car1 = <span class="kwrd">new</span> Car();
       car1.DescribeCar();
       System.Console.WriteLine(<span class="str">"----------"</span>);
       ConvertibleCar car2 = <span class="kwrd">new</span> ConvertibleCar();
       car2.DescribeCar();
       System.Console.WriteLine(<span class="str">"----------"</span>);
       Minivan car3 = <span class="kwrd">new</span> Minivan();
       car3.DescribeCar();
    
       System.Console.WriteLine(<span class="str">"----------"</span>);
    
    }









输出类似如下所示：






Four wheels and an engine.






----------






Four wheels and an engine.






A roof that opens up.






----------






Four wheels and an engine.






Carries seven people.






----------






但是，如果我们声明一个从 Car 基类派生的对象的数组。此数组能够存储 Car、ConvertibleCar 和 Minivan 对象，如下所示：




    
    <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">void</span> TestCars2()
    {
        Car[] cars = <span class="kwrd">new</span> Car[3];
        cars[0] = <span class="kwrd">new</span> Car();
        cars[1] = <span class="kwrd">new</span> ConvertibleCar();
    
        cars[2] = <span class="kwrd">new</span> Minivan();
    
    }









然后用一个 foreach 循环来访问该数组中包含的每个 Car 对象，并调用 DescribeCar 方法，如下所示：





    
    <span class="kwrd">foreach</span> (Car vehicle <span class="kwrd">in</span> cars)
    {
      System.Console.WriteLine(<span class="str">"Car object: "</span> + vehicle.GetType());
      vehicle.DescribeCar();
    
      System.Console.WriteLine(<span class="str">"----------"</span>);
    
    }



此循环的输出如下所示：






Car object: YourApplication.Car






Four wheels and an engine.






----------






Car object: YourApplication.ConvertibleCar






Four wheels and an engine.






----------






Car object: YourApplication.Minivan






Four wheels and an engine.






Carries seven people.






----------






注意，ConvertibleCar 的说明可能与您的预期不同。由于使用了 new 关键字来定义此方法，所调用的不是派生类方法，而是基类方法。Minivan 对象正确地调用重写方法，并产生预期的结果。



