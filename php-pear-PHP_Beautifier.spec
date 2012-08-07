%define		class		PHP
%define		subclass	Beautifier
%define		status		beta
%define		_pearname	%{class}_%{subclass}
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - beautifier for PHP
Summary(pl.UTF-8):	%{_pearname} - upiększacz dla PHP
Name:		php-pear-%{_pearname}
Version:	0.1.15
Release:	4
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	43aaf77521c5efb353bd7d46d20fe158
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/PHP_Beautifier/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(tokenizer)
Requires:	php-common >= 3:5
Requires:	php-pear >= 4:1.0-7
Requires:	php-pear-Log >= 1.8
Suggests:	php-bz2
Suggests:	php-pear-Archive_Tar
Suggests:	php-pear-Console_Getopt
Suggests:	php-pear-PHP_DocBlockGenerator
Obsoletes:	php-pear-PHP_Beautifier-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Console/Getopt.*)' 'pear(Archive/Tar.*)' pear(PHP/DocBlockGenerator.*)

%description
This program reformat and beautify PHP source code files
automatically.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten program automatycznie przeformatuje i upiększy kod źródłowy
aplikacji napisanych w PHP.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1

mv docs/%{_pearname}/examples .
rm ./%{_bindir}/php_beautifier.bat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}
cp -a examples/*  $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/php_beautifier
%{php_pear_dir}/%{class}/*.php
%{php_pear_dir}/%{class}/%{subclass}

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}
