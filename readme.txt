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
  
������Ŀdemo(ע���������֮ǰ�Ѿ���github����demo��Ŀ): 
  github·����https://github.com/mtslong/demo.git
  ����·����E:\03.git\github
  ���ɿ�¡�������
  1������Ŀ¼ E:\03.git\github\��
  2������������ git Bash��
  3��ִ������ git clone https://github.com/mtslong/demo.git
  ���ɿ�������demoĿ¼��ʣ�µĲ�����git����һ����
  
demo��Ŀ������URL��ַ�� http://mtslong.github.io/demo/
����������
$ cd your_repo_root/repo_name
$ git fetch origin
$ git checkout gh-pages
���ؽ�����һ��gh-pages��֧��ԭ���Ĵ�����master��֧��

Unpublishing a project page
To unpublish a project page, delete the remote gh-pages branch:

ȡ������ git push origin --delete gh-pages
# Delete the gh-pages branch from origin
# To https://github.com/username/repo.git
# - [deleted]         gh-pages

