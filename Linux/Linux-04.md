1  KEY=value
    2  echo KEY
    3  echo $KEY
    4  KEY=newvalue
    5  echo $KEY
    6  3key=7
    7  key?=hello
    8  _key=5
    9  echo $_key
   10  env
   11  printenv less
   12  printenv | less
   13  echo $HOME
   14  cd
   15  ~
   16  pwd
   17  mkdir test
   18  pwd
   19  ls
   20  HOME=/home/ec2-user/test
   21  pwd
   22  cd
   23  pwd
   24  echo $HOME
   25  ENVVAR=abc
   26  export ENVVAR=abc
   27  printenv ENVVAR
   28  export MEHMET=aws
   29  printenv $MEHMET
   30  MEHMET=aws
   31  export MEHMET=aws
   32  printenv $MEHMET
   33  printenv MEHMET
   34  shellvar=def
   35  set | grep shellvar
   36  set | grep ENVVAR
   37  set | grep MEHMET
   38  unset shellvar
   39  unset ENVVAR
   40  unset MEHMET
   41  set | grep ENVVAR
   42  set | grep MEHMET
   43  grep ENVVAR
   44  export ENVAR=123
   45  printenv ENVAR
   46  shellvar=456
   47  shvar=456
   48  bash
   49  var=value
   50  printenv var
   51  export var
   52  printenv var
   53  vi test.sh
   54  echo "Welcome to lesson"
   55  chmod +x test.sh
   56  ls -l
   57  ./test.sh
   58  printenv ENVAR
   59  shlvar=456
   60  echo $shlvar
   61  printenv shlvar
   62  vi test.sh
   63  cat test.sh
   64  ./test.sh
   65  env
   66  pwd
   67  whereis ls
   68  myvar=my value
   69  myvar=my \value
   70  myvar="my value"
   71  echo $myvalue
   72  touch file{1..9}
   73  ls
   74  ls file*
   75  touch file*
   76  ls
   77  touch "file*"
   78  ls
   79  ls file*
   80  ls "file*"
   81  MYNAME=mehmet
   82  MYVAR="my name is $MYNAME"
   83  echo $MYVAR
   84  MYVAR="my name is \$MYNAME"
   85  echo $MYVAR
   86  MYVAR='my $MYNAME'
   87  echo $MYVAR
   88  rm file*
   89  ls
   90  touch myfile
   91  ls
   92  cd /
   93  ls
   94  touch myfile
   95  sudo touch myfile
   96  ls
   97  rm myfile
   98  ls
   99  sudo rm myfile
  100  ls
  101  cd
  102  ls
  103  whoami
  104  sudo su root
  105  whoami
  106  sudo su
  107  sudo su -
  108  ls
  109  who
  110  id
  111  useradd user1
  112  id user1
  113  pwd
  114  sudo useradd user1
  115  who
  116  id user1
  117  sudo su -user1
  118  whoami
  119  sudo useradd user1
  120  sudo useradd user2
  121  sudo passwd user2
  122  history >history.txt