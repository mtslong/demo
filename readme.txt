Global setup:
  git config --global user.name "Your Name"
  git config --global user.email mofeng@netease.com
      
Next steps:
  mkdir demo
  cd demo
  git init
  touch README
  git add README
  git commit -m 'first commit'
  git remote add origin git@github.com:mtslong/demo.git

  git pull origin master
  git push -u origin master
  
测试项目demo(注：下面操作之前已经在github创建demo项目): 
  github路径：https://github.com/mtslong/demo.git
  本地路径：E:\03.git\github
  生成克隆库操作：
  1、进入目录 E:\03.git\github\；
  2、进入命令行 git Bash；
  3、执行命令 git clone https://github.com/mtslong/demo.git
  即可看到生成demo目录。剩下的操作和git操作一样。
  
测试发现HelloWorld项目在github网页上的内容更新太慢了。
  