---
author: ths
comments: true
date: 2011-03-16 08:02:00+00:00
layout: post
slug: inno-setup-%e6%95%b0%e6%8d%ae%e5%ba%93%e8%87%aa%e5%8a%a8%e5%ae%89%e8%a3%85%e4%bb%a3%e7%a0%81%ef%bc%88mysql%ef%bc%89
title: inno setup 数据库自动安装代码（mysql）
wordpress_id: 562
categories:
- 技术
- 折腾
tags:
- inno setup
- mysql
- 打包
- 自动安装
---

<





p>[Setup]  
AppID=DBUpdateTest  
AppName=E-Touch数据库安装文件  
AppVerName=E-Touch数据库安装文件 0.1  
AppPublisher=LZT, Inc.  
DefaultDirName={pf}lzt  
DefaultGroupName=lzt  
DisableDirPage=yes  
DisableProgramGroupPage=yes





<





p>PrivilegesRequired=none  
OutputDir=D:DataEntry2Dotfuscatorsetup  
;安装程序名  
OutputBaseFilename=DBInstall  
[Files]  
Source: "D:mysql.exe"; Flags: dontcopy  
Source: "D:picprocess.sql"; Flags: dontcopy





<





p>[Languages]  
Name: "english"; MessagesFile: "compiler:Default.isl"





<





p>[Code]  
var  
DBPage: TInputQueryWizardPage;





<





p>procedure InitializeWizard;  
begin  
DBPage := CreateInputQueryPage(wpReady,  
'Database Connection Information', 'Which database is to be updated?',  
'Please specify the server and the connection credentials, then click Next.');  
DBPage.Add('Server:', False);  
DBPage.Add('User name:', False);  
DBPage.Add('Password:', True);





<





p> DBPage.Values[0] := GetPreviousData('Server', '');  
DBPage.Values[1] := GetPreviousData('UserName', '');  
DBPage.Values[2] := GetPreviousData('Password', '');  
end;





<





p>function ExecScriptInMYSQL(DBHost, DBLogin, DBPass : String): Boolean;  
var  
ConnectExe: String;  
ConnectParam: String;  
ResultCode: Integer;  
StatusString: String;  
begin  
{解压临时文件}  
ExtractTemporaryFile('mysql.exe');  
ExtractTemporaryFile('picprocess.sql');  
{构造数据库连接字符串}  
ConnectExe := ExpandConstant('cmd');  
ConnectParam := ' /c "' + ExpandConstant('{tmp}') + 'mysql.exe'  
+ ' -h ' + DBHost  
+ ' -u ' + DBLogin  
+ ' -p' + DBPass  
+ ' --default-character-set=utf8'  
+ ' < ' + ExpandConstant('{tmp}') + 'picprocess.sql"';  
if Exec(ConnectExe, ConnectParam, '', SW_HIDE, ewWaitUntilTerminated, ResultCode) then begin  
Result := ResultCode = 0;  
LoadStringFromFile(ExpandConstant('{tmp}') + 'dbstatus.txt', StatusString);  
if StatusString <> '' then begin  
MsgBox(StatusString, mbError, MB_OK);  
Result := False;  
end else begin  
Result := True;  
end;  
end else begin  
MsgBox('Database update failed:'#10#10 + SysErrorMessage(ResultCode), mbError, MB_OK);  
Result := False;  
end;  
end;





<





p>procedure RegisterPreviousData(PreviousDataKey: Integer);  
begin  
ExecScriptInMYSQL(DBPage.Values[0], DBPage.Values[1], DBPage.Values[2]);  
SetPreviousData(PreviousDataKey, 'Server', DBPage.Values[0]);  
SetPreviousData(PreviousDataKey, 'UserName', DBPage.Values[1]);  
SetPreviousData(PreviousDataKey, 'Password', DBPage.Values[2]);  
end;





function NextButtonClick(CurPageID: Integer): Boolean;  
var  
ResultCode: Integer;  
begin  
Result := True;  
if CurPageID = DBPage.ID then begin  
if DBPage.Values[0] = '' then begin  
MsgBox('You must enter the server name or address.', mbError, MB_OK);  
Result := False;  
end else if DBPage.Values[1] = '' then begin  
MsgBox('You must enter the user name.', mbError, MB_OK);  
Result := False;  
end else if DBPage.Values[2] = '' then begin  
MsgBox('You must enter the user password.', mbError, MB_OK);  
Result := False;  
end;  
end;  
end; 



