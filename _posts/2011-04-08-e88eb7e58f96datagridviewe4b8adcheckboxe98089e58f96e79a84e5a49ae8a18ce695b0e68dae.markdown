---
author: ths
comments: true
date: 2011-04-08 07:44:00+00:00
layout: post
slug: '%e8%8e%b7%e5%8f%96datagridview%e4%b8%adcheckbox%e9%80%89%e5%8f%96%e7%9a%84%e5%a4%9a%e8%a1%8c%e6%95%b0%e6%8d%ae'
title: 获取Datagridview中Checkbox选取的多行数据
wordpress_id: 602
categories:
- 技术
tags:
- Datagridview
---




    
    private void PrintInFo() {
       try 
         { 
            int count = 0; 
            //用?于?保?存?选?中?的?checkbox数?量?
            //DG_List为?datagridview控?件?
            for (int i = 0; i < DG_List.RowCount; i++) 
            {
                if (DG_List.Rows[i].Cells [0].EditedFormattedValue.ToString() == "True") 
                //这?里?判?断?复?选?框?是?否?选?中?
                { 
                    count++; 
                } 
             } 
             if (count == 0)
             {
                  MessageBox.Show("请?至?少?选?择?一?条?数?据?！?", "提?示?");
                  return;
             }
             else
             { 
                  if (MessageBox.Show(this, "您?要?更?新?数?据?么?？?", "提?示?", MessageBoxButtons.YesNo,    MessageBoxIcon.Information).ToString() == "Yes")
                  { 
                       for (int i = 0; i < count; i++) 
                       { 
                           ps.Pexcute(" update cf_prj_certi set FIsPrint='"+number+"' where fid='" + DG_List.Rows[i].Cells["fnn"].Value.ToString() + "'"); //执?行?SQL
                       } 
                   } else 
                    { 
                        return; 
                    } 
              } 
         } catch (Exception ex)
            {
                MessageBox.Show(ex.ToString()); 
            } this.ShowInfo(); //重?新?绑?定?datagridview
    }  



