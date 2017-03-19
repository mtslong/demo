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

Git基本语法
语法	功能说明
git clone	克隆版本库
git pull	拉回远程版本库的提交
git push	推送至远程版本库
git add	添加至暂存区
git add–interactive	交互式添加
git apply	应用补丁
git am	应用邮件格式补丁
git annotate	同义词，等同于 git blame
git archive	文件归档打包
git bisect	二分查找
git blame	文件逐行追溯
git branch	分支管理
git cat-file	版本库对象研究工具
git checkout	检出到工作区、切换或创建分支
git cherry-pick	提交拣选
git citool	图形化提交，相当于 git gui 命令
git clean	清除工作区未跟踪文件
git commit	提交
git config	查询和修改配置
git describe	通过里程碑直观地显示提交ID
git diff	差异比较
git difftool	调用图形化差异比较工具
git fetch	获取远程版本库的提交
git format-patch	创建邮件格式的补丁文件。参见 git am 命令
git grep	文件内容搜索定位工具
git gui	基于Tcl/Tk的图形化工具，侧重提交等操作
git help	帮助
git init	版本库初始化
git init-db	同义词，等同于 git init
git log	显示提交日志
git merge	分支合并
git mergetool	图形化冲突解决
git mv	重命名
git rebase	分支变基
git rebase–interactive	交互式分支变基
git reflog	分支等引用变更记录管理
git remote	远程版本库管理
git repo-config	同义词，等同于 git config
git reset	重置改变分支“游标”指向
git rev-parse	将各种引用表示法转换为哈希值等
git revert	反转提交
git rm	删除文件
git show	显示各种类型的对象
git stage	同义词，等同于 git add
git stash	保存和恢复进度
git status	显示工作区文件状态
git tag	里程碑管理
