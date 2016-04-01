#!/usr/bin/env perl
use strict;
# 加载 DBI 模块
use DBI;
use DBI qw(:sql_types);

# 主机名
my $dbname = "boss20hg";
# 数据库名
my $user = "ng_pocjf";
# 密码
my $passwd = "ng_pocjf";

=pod
建立一个数据库数据库连接
函数原型：connect($data_source, $username, $password)
$password: 如果含有特殊字符，需要使用 \ 进行转义
$data_source值格式为：DBI:driver_name:$dbname
AutoCommit，当为true时，事务处理会自动提交。但如果数据库不支持事务处理，设置AutoCommit为false将导致严重错误。
RaiseError，在DBI遇到错误时调用croak $DBI::errstr。PrintError，它将调用DBI的warn $DBI::errstr。
当有错误发生时，DBI 会把错误讯息存放在 package variable $DBI::errstr 之中
=cut

my $dbh = DBI->connect("dbi:Oracle:$dbname", $user, $passwd, { RaiseError => 1, AutoCommit => 0 }) 
	or die "can't connect to database:$DBI::errstr\n";

=pod
# 建立SQL查询字符串

# 可以使用 prepare() 和 do() 方法来建立 SQL 查询字符串
# prepare() 和 execute() 方法针对的是 SELECT 查询
# do()方法是针对于一次性使用的INSERT，UPDATE或者DELETE查询
# 成功的 SELECT 查询将返回一个结果对象，成功的 INSERT/UPDATE/DELETE 将返回受影响的行数，而不成功的查询将返回一个错误。
# execute方法执行一个准备好的语句。对非SELECT语句，execute返回受影响的行数。
# 如果没有行受影响，execute返回"0E0"，Perl将它视作零而不是真。
# 对于SELECT语句，execute只是在数据库中启动SQL查询；你需要使用在下面描述的fetch_*方法之一检索数据。
# do方法准备并且执行一条SQL语句并且返回受影响的行数。
# 如果没有行受到影响，do返回"0E0"，Perl将它视为零而不是真。
# 这个方法通常用于事先无法准备好(由于驱动程序的限制)或不需要执行多次(插入、删除等等)的非SELECT语句。
=cut

# 删除数据表
my $drop = "BEGIN EXECUTE IMMEDIATE 'DROP TABLE employees'; EXCEPTION WHEN OTHERS THEN NULL; END;";
$dbh->do($drop) or die "Can't do $drop: $dbh->errstr\n";
$dbh->commit();

# 创建数据表
my $create = qq{ CREATE TABLE employees (id integer not null, name varchar(128), title varchar(128), phone char(11)) };
$dbh->do($create) or die "Can't do $create: $dbh->errstr\n";
$dbh->commit();

# 插入数据
my $insert = "insert into employees(id, name, title, phone) values (9527, 'zhouxingxing', 'Traitor', '13800138000')";
my $rows = $dbh->do($insert) or die "Can't do $insert: $dbh->errstr\n";
print "Insert data successfully: $rows lines\n";
$dbh->commit();

# 异常处理机制
my @data = (
	[0, "Larry Wall",      "Perl Author", "555-0101"],
	[1, "Tim Bunce",       "DBI Author",  "555-0202"],
	[2, "Doug MacEachern", "Apache Man",  "555-0404"]
);

my $sql = "insert into employees values(?, ?, ?, ?)";
my $sth = $dbh->prepare($sql) or die "Can't prepare $sql: $DBI::errstr\n";
for (@data)
{
	eval
	{
		# 绑定变量
		$sth->bind_param(1, $_->[0], SQL_INTEGER);
		$sth->bind_param(2, $_->[1], SQL_VARCHAR);
		$sth->bind_param(3, $_->[2], SQL_VARCHAR);
		$sth->bind_param(4, $_->[3], SQL_VARCHAR);
		$sth->execute();
		$dbh->commit();
	};
	if($@)
	{
		warn "Database error: $DBI::errstr\n";
		$dbh->rollback();
	}
}

# 查询
my $select = "select * from employees where rownum <= 10";
$sth = $dbh->prepare($select) or die "Can't prepare $select: $dbh->errstr\n";
$sth->execute() or die "can't execute the query: $sth->errstr\n";

# 得到一行数据
# fetchrow_array 作为一个字段数组取出下一行
# 其它取出数据的方式请使用以下命令查阅：perldoc DBI
while(my @data = $sth->fetchrow_array())
{
	print "id    -> $data[0]\n";
	print "name  -> $data[1]\n";
	print "title -> $data[2]\n";
	print "phone -> $data[3]\n";
}



# 释放资源
$sth->finish();

# 断开数据库连接
$dbh->disconnect;
