---
author: ths
comments: true
date: 2010-11-30 05:27:45+00:00
layout: post
slug: ado-net%ef%bc%88%e4%b8%8a%e4%b8%8b%e7%af%87%ef%bc%89
title: ADO.NET（上下篇）
wordpress_id: 142
categories:
- 技术
---





【转自】http://blog.csdn.net/iscan/archive/2007/12/31/2005731.aspx





**上篇**





1.什么是ADO.NET?





ADO.NET是一组用于和数据源进行交互的面向对象类库。





2.ADO.NET 的主要对象有哪些？





Connection :用于连接到数据库和管理对数据库的事务；





Command :用于对数据库发出SQL命令；





DataReader :用于从数据源读取只进数据记录流；





DataSet :用于对单层数据、XML数据和关系数据进行存储、远程处理和编程；





DataAdapter :用于将数据推入DataSet，并使数据与数据库保持一致；





3.Connection对象





访问数据 首先就要建立到操作对象的连接，这就是Connection对象，通常用到的访问SQL Server的叫SqlConnection类，访问其他的叫OleDbConnection类，如：Access，Oracle；





Connection 对象有两个主要方法：Open()和Close()





语法：Data Source＝（local）;Initial Catalog=数据库名；Integrated Security=True;Persist Security Info=False;User ID=用户名；Password=密码；





Server＝（local）;Database=数据库名；Integrated Security=True;Persist Security Info=False;UID=用户名；PWD=密码;





4.Integrated Security 与Persist Security Info 区别





Integrated Security 用于指定采用的集成安全机制





Integrated Security=SSPI 表示以当前WINDOWS系 统用户身去登录SQL SERVER服务器，





SSPI是Security Support Provider Interface（Microsoft安全支持提供器接口）的英文缩写。





Persist Security Info 持续安全信息，关键字的默认设置为 false。





如果将该关键字设置为 true 或 yes，将允许在打开连接后，从连接中获得涉及安全性的信息（包括用户标识和密码）。如果在建立连接时必须提供用户标识和密码，最安全的方法是在使用信息 打开连接后丢弃这些信息，在 Persist Security Info 设置为 false 或 no 时会发生这种情况。当您向不可信的源提供打开的连接，或将连接信息永久保存到磁盘时，这点尤其重要。如果将 Persist Security Info 保持为 false，可帮助确保不可信的源无法访问连接中涉及安全性的信息，并帮助确保任何涉及安全性的信息都不会随连接字符串信息在磁盘上持久化。





Integrated Security默认值是False，此时需要提供Uid和Pwd，即将以Sql Server 用户身份登陆数据库；如果设置为True，Yes 或 SSPI，这不能出现Uid和Pwd，将以Windows用户身份登陆数据库。强烈推荐用后一种形式，安全性更高。Integrated Security和Persist Security Info同时出现，后者设置为False，可保证信息安全。最好使用SSPI的集成安全方式连接数据库。





5.Server 和Database，Data Source和Initial Catalog配对使用的，可以互相替换





6.最佳连接数据的方式，把连接 数据库的代码写在Web.Config中的connectionStrings中:





  

      

    providerName="System.Data.SqlClient"  

    name ="testStr" connectionString ="Data Source=(local);Persist Security Info=False;Integrated Security=SSPI;UID=sa;PWD=;"  

    />





然 后在页面的加载处调用代码标识testStr:





String MyConn = System.Configuration.ConfigurationManager.ConnectionStrings["testStr"].ToString();  

    SqlConnection Conn = new SqlConnection(MyConn);





7.连接数据库的方式





protected void Page_Load(object sender, EventArgs e)  

    {





//Server与 Database同时出现  

    SqlConnection Conn = new SqlConnection("Server=LocalHost;Database=Northwind;Integrated Security=SSPI");





//Data Source与Initial Catalog同时出现  

    //SqlConnection Conn = new SqlConnection("Data Source=LocalHost;Initial Catalog=Northwind;Integrated Security=SSPI;");





//Workstation Id=MicroKing;Packet Size=4096;设置workstation  id的值只能是机器名或者IP地址；设置整个网络中使用的包的大小（以字节为单位）  

    //SqlConnection Conn = new SqlConnection("Server=LocalHost;Database=northwind;Persist Security Info=False;Integrated Security=SSPI;Workstation Id=MicroKing;Packet Size=4096;");





//UID也可是写成User ID,PWD也可以写成Password  

    //SqlConnection Conn = new SqlConnection(" UID=sa;PWD=;Initial Catalog=Northwind;Data Source=LocalHost;Connect Timeout=900");





//声明一个字符串并把在Web.Config中配置 的connectionString的属性赋予它，然后再创建连接对象；  

    //String MyConn = System.Configuration.ConfigurationManager.ConnectionStrings["testStr"].ToString();  

    //SqlConnection Conn = new SqlConnection(MyConn);





//先创建一个数据库连接对象，然后给它的 ConnectionStirng赋值；  

    //SqlConnection Conn = new SqlConnection();  

    //Conn.ConnectionString = System.Configuration.ConfigurationManager.ConnectionStrings["testStr"].ToString();





try  

    {  

    Conn.Open();  

    Response.Write(" ");  

    Conn.Close();  

    Label1.Text = "数据库已经关闭"





}  

    catch   

    {  

    Response.Write(" ");  

    }  

    }





单词：





initial ![](http://res.iciba.com/resource/yinbiao/fangkh-z.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/5.gif) ![](http://res.iciba.com/resource/yinbiao/n.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/F.gif) ![](http://res.iciba.com/resource/yinbiao/E.gif) ![](http://res.iciba.com/resource/yinbiao/l.gif) ![](http://res.iciba.com/resource/yinbiao/fangkh-y.gif) 原始的





integrated ![](http://res.iciba.com/resource/yinbiao/fangkh-z.gif) ![](http://res.iciba.com/resource/yinbiao/5.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/n.gif) ![](http://res.iciba.com/resource/yinbiao/t.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/%5E.gif) ![](http://res.iciba.com/resource/yinbiao/r.gif) ![](http://res.iciba.com/resource/yinbiao/e.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/t.gif) ![](http://res.iciba.com/resource/yinbiao/i.gif) ![](http://res.iciba.com/resource/yinbiao/d.gif) ![](http://res.iciba.com/resource/yinbiao/fangkh-y.gif) 综合的, 完整的





persist ![](http://res.iciba.com/resource/yinbiao/fangkh-z.gif) ![](http://res.iciba.com/resource/yinbiao/p.gif) ![](http://res.iciba.com/resource/yinbiao/E.gif) ![](http://res.iciba.com/resource/yinbiao/5.gif) ![](http://res.iciba.com/resource/yinbiao/s.gif) ![](http://res.iciba.com/resource/yinbiao/I.gif) ![](http://res.iciba.com/resource/yinbiao/s.gif) ![](http://res.iciba.com/resource/yinbiao/t.gif) ![](http://res.iciba.com/resource/yinbiao/fangkh-y.gif) 持久；持续





**下篇**





1.Command对象的作用：





用于对数据库发出SQL命令，从而执行添加、修改、删除等操作；





2.Comman 对象的两个主要方法：





ExecuteNonQuery方法：执行命令并返回受影响的行数；





ExecuteReader方 法：执行命令并返回生成的DataReader；





3.DataReader对象的作用？





返回一个来自数据命令的只读、只 进的数据流；





语法：SqlCommand 对象名＝new SqlCommand("SQL语句",Connection实例化对象)





4.使用Command与DataReader的数据操作实例：





protected void Page_Load(object sender, EventArgs e)  

    {  

    SqlConnection Conn = new SqlConnection("Server=LocalHost;Integrated Security=SSPI;Database=test");  

    Conn.Open();  

    //增加数据  

    SqlCommand Insert = new SqlCommand("insert into students(name,sex) values ('小赵','男')", Conn);  

    Insert.ExecuteNonQuery();





//查询数据  

    SqlCommand Comm = new SqlCommand("select * from students",Conn);  

    SqlDataReader Da1 = Comm.ExecuteReader();  

    while(Da1.Read())  

    {  

    Response.Write(Da1["id"]);  

    Response.Write(Da1["name"]);  

    Response.Write(Da1["sex"]);  

    Response.Write("  

    ");  

    }  

    Da1.Close();





//更新数据  

    SqlCommand update = new SqlCommand("update students set name='小王',sex='女' where name='小赵'", Conn);  

    update.ExecuteNonQuery();  

    // 查询数据  

    SqlDataReader Da2=Comm.ExecuteReader();  

    while(Da2.Read())  

    {  

    Response.Write(Da2["id"]);  

    Response.Write(Da2["name"]);  

    Response.Write(Da2["sex"]);  

    Response.Write("  

    ");  

    }  

    Da2.Close();





//删除数据  

    SqlCommand delete = new SqlCommand("delete from students where name='小王'", Conn);  

    delete.ExecuteNonQuery();  

    Response.Write(" 数据已经被删除");





Conn.Close();  

    }





5.什么是DataSet？





数 据集（DataSet）是独立于数据存储区且与之不同的数据结构，是一种代表关系数据的内存驻留结构；





6.为什么要使用DataSet？





将数据库读到数据集，从而进行无连接的操作；





7.关于DataSet





DataSet包含 DataTable，相当于数据库中的表，每个DataTable中又包括DataRow（行）和DataColumn（列），分别代表数据库中表的行和 列。





8.什么是DataAdapter对象？





DataAdapter对象在源数据与DataSet之间起到了桥梁的作 用；





9.DataAdapter的只要作用





DataAdapter对象会填充DataSet对象中的表，而且能读取缓存 的更改并将其提交给数据库。





10.DataAdapter对象的两个主要方法：





Fill方法：填充数据集





Update 方法：向数据库提交存储在DataSet中的更改。





实例操练：





protected void Page_Load(object sender, EventArgs e)  

    {  

    String myConn = System.Configuration.ConfigurationManager.ConnectionStrings["testStr"].ToString();  

    SqlConnection Conn = new SqlConnection(myConn);  

    Conn.Open();





SqlDataAdapter Da = new SqlDataAdapter("select * from students",Conn);  

    DataSet Ds = new DataSet();





Da.Fill(Ds, "info");//填充DataSet  

    if (Ds.Tables[0].Rows.Count==0)  

    {  

    Response.Write("数据库中无数据");  

    }  

    else  

    {  

    for (int i = 0; i < Ds.Tables[0].Rows.Count; i++)  

    {  

    Response.Write(Ds.Tables[0].Rows[i]["name"]);  

    Response.Write(Ds.Tables[0].Rows[i]["sex"]);  

    Response.Write("  

    ");  

    }  

    }





Conn.Close();  

    }





10.Update方法的原理





使用Update方法自动遍历 DataTable中所有行，以检查需要对数据库做出的变动，它为每一个发生的更改的行调用Insert、Update或Delete命令；





11.SqlCommandBuilder类：自动生成单表命令并与SqlDataAdapter相关联





12.DataTAble Rows集合的三个常用的方法





Find方法：检索行





Add方法：创建行





Delete方法：删除行





13. 实例操作：





protected void Page_Load(object sender, EventArgs e)  

    {  

    String myConn = System.Configuration.ConfigurationManager.ConnectionStrings["testStr"].ToString();  

    SqlConnection Conn = new SqlConnection(myConn);  

    Conn.Open();





SqlDataAdapter Da = new SqlDataAdapter("select * from students",Conn);  

    SqlCommandBuilder Cb = new SqlCommandBuilder(Da);//生成SQL命令并与SqlDataAdapter关联  

    DataSet Ds = new DataSet();  

    Da.Fill(Ds, "info");//填充DataSet





//添加数据  

    DataRow dr = Ds.Tables["info"].NewRow();  

    dr["name"] = "美女"  

    dr["sex"] = "女"  

    Ds.Tables["info"].Rows.Add(dr);





//修改数据  

    Response.Write(" 修改之前的数据为" + Ds.Tables["info"].Rows[0]["name"] + Ds.Tables["info"].Rows[0]["sex"]);  

    Response.Write("  

    ");  

    Ds.Tables["info"].Rows[0] ["name"]="赵王"  

    Ds.Tables["info"].Rows[0][2]="女"  

    Response.Write("修改之 后的数据为" + Ds.Tables["info"].Rows[0]["name"] + Ds.Tables["info"].Rows[0]["sex"]);  

    Response.Write("  

    ");  

    //删除数据  

    Ds.Tables["info"].Rows[0].Delete();  

    Da.Update(Ds, "info");  

    Response.Write("数据已经被删除");  

    Conn.Close();  

    }



