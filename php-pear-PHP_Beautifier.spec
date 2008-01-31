%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Beautifier
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - beautifier for PHP
Summary(pl.UTF-8):	%{_pearname} - upiększacz dla PHP
Name:		php-pear-%{_pearname}
Version:	0.1.11
Release:	3
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4903b1dd1752b35010bdc19b3d81a584
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/PHP_Beautifier/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(tokenizer)
Requires:	php-common >= 3:5
Requires:	php-pear >= 4:1.0-7
Requires:	php-pear-Log >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Console/Getopt.*)' 'pear(Archive/Tar.*)'

%description
This program reformat and beautify PHP source code files
automatically.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten program automatycznie przeformatuje i upiększy kod źródłowy
aplikacji napisanych w PHP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
cp -a ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/php_beautifier
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
