@echo off
 
title bing-wallpaper自动提交
echo 开始添加变更：git add .
cd E:\pythonProject\bing-wallpaper 
git add .
echo;
 
git commit -m "自动提交"
echo;
 
echo 将变更提交到远程分支
git push origin refs/heads/master:master
echo;
 
echo 执行完毕！
echo;
 
pause
