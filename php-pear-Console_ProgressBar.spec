%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	ProgressBar
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides an easy-to-use interface to progress bars
Summary(pl):	%{_pearname} - ³atwy w u¿yciu interfejs do pasków postêpu
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fe75f11dd310106e6e8703a8627834bb
URL:		http://pear.php.net/package/Console_ProgressBar/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class allows you to display progress bars in your terminal. You can
use this for displaying the status of downloads or other tasks that take
some time.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± tej klasy mo¿liwe jest wy¶wietlanie pasków postêpów w
terminalu. Mo¿liwe jest wy¶wietlenie statusu ¶ci±gania b±d¼ innych zadañ
trwaj±cych przez pewien czas.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
