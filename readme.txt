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
  
demo项目发布的URL地址： http://mtslong.github.io/demo/
发布操作：
$ cd your_repo_root/repo_name
$ git fetch origin
$ git checkout gh-pages
本地将建立一个gh-pages分支，原来的代码在master分支。

Unpublishing a project page
To unpublish a project page, delete the remote gh-pages branch:

取消发布 git push origin --delete gh-pages
# Delete the gh-pages branch from origin
# To https://github.com/username/repo.git
# - [deleted]         gh-pages

使用github的项目网站发布方式很方便实现个人主页。自己可以完全控制网站的链接和内容，这个很酷。

