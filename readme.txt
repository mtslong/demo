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

ʹ��github����Ŀ��վ������ʽ�ܷ���ʵ�ָ�����ҳ���Լ�������ȫ������վ�����Ӻ����ݣ�����ܿᡣ

Git�����﷨
�﷨	����˵��
git clone	��¡�汾��
git pull	����Զ�̰汾����ύ
git push	������Զ�̰汾��
git add	������ݴ���
git add�Cinteractive	����ʽ���
git apply	Ӧ�ò���
git am	Ӧ���ʼ���ʽ����
git annotate	ͬ��ʣ���ͬ�� git blame
git archive	�ļ��鵵���
git bisect	���ֲ���
git blame	�ļ�����׷��
git branch	��֧����
git cat-file	�汾������о�����
git checkout	��������������л��򴴽���֧
git cherry-pick	�ύ��ѡ
git citool	ͼ�λ��ύ���൱�� git gui ����
git clean	���������δ�����ļ�
git commit	�ύ
git config	��ѯ���޸�����
git describe	ͨ����̱�ֱ�۵���ʾ�ύID
git diff	����Ƚ�
git difftool	����ͼ�λ�����ȽϹ���
git fetch	��ȡԶ�̰汾����ύ
git format-patch	�����ʼ���ʽ�Ĳ����ļ����μ� git am ����
git grep	�ļ�����������λ����
git gui	����Tcl/Tk��ͼ�λ����ߣ������ύ�Ȳ���
git help	����
git init	�汾���ʼ��
git init-db	ͬ��ʣ���ͬ�� git init
git log	��ʾ�ύ��־
git merge	��֧�ϲ�
git mergetool	ͼ�λ���ͻ���
git mv	������
git rebase	��֧���
git rebase�Cinteractive	����ʽ��֧���
git reflog	��֧�����ñ����¼����
git remote	Զ�̰汾�����
git repo-config	ͬ��ʣ���ͬ�� git config
git reset	���øı��֧���αꡱָ��
git rev-parse	���������ñ�ʾ��ת��Ϊ��ϣֵ��
git revert	��ת�ύ
git rm	ɾ���ļ�
git show	��ʾ�������͵Ķ���
git stage	ͬ��ʣ���ͬ�� git add
git stash	����ͻָ�����
git status	��ʾ�������ļ�״̬
git tag	��̱�����